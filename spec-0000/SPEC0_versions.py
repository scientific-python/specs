from datetime import datetime, timedelta

import pandas as pd
import requests
from packaging.version import Version

py_releases = {
    "3.8": "Oct 14, 2019",
    "3.9": "Oct 5, 2020",
    "3.10": "Oct 4, 2021",
    "3.11": "Oct 24, 2022",
    "3.12": "Oct 2, 2023",
}
core_packages = [
    # Path(x).stem for x in glob("../core-projects/*.md") if "_index" not in x
    "numpy",
    "scipy",
    "matplotlib",
    "pandas",
    "scikit-image",
    "networkx",
    "scikit-learn",
    "xarray",
    "ipython",
]
plus36 = timedelta(days=int(365 * 3))
plus24 = timedelta(days=int(365 * 2))

# Release data

now = datetime.now()


def get_release_dates(package, support_time=plus24):
    releases = {}
    response = requests.get(f"https://pypi.org/pypi/{package}/json").json()

    for ver, ver_files in response["releases"].items():
        try:
            version = Version(ver)
        except:
            continue

        if version.is_prerelease or version.micro != 0:
            continue

        upload_time = min(
            (release_file["upload_time_iso_8601"] for release_file in ver_files),
            default=None,
        )
        if upload_time is None:
            continue

        release_date = None
        for format in ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"]:
            try:
                release_date = datetime.strptime(upload_time, format)
            except:
                pass

        if not release_date:
            continue

        drop_date = release_date + support_time
        if drop_date >= datetime.now():
            releases[ver] = {
                "release_date": release_date,
                "drop_date": drop_date,
            }

    return releases


package_releases = {
    "python": {
        version: {
            "release_date": datetime.strptime(release_date, "%b %d, %Y"),
            "drop_date": datetime.strptime(release_date, "%b %d, %Y") + plus36,
        }
        for version, release_date in py_releases.items()
    }
}
package_releases |= {package: get_release_dates(package) for package in core_packages}

# filter all items whos drop_date are in the past

package_releases = {
    package: {
        version: dates
        for version, dates in releases.items()
        if dates["drop_date"] > now
    }
    for package, releases in package_releases.items()
}


# Print Gantt chart

print(
    """<!-- prettier-ignore-start -->
{{<mermaid>}}
gantt
dateFormat  YYYY-MM-DD
axisFormat  %m / %Y
title Support Window
"""
)

for name, releases in package_releases.items():
    print(f"\nsection {name}")
    for version, dates in releases.items():
        print(
            f"{version}  :     {dates['release_date'].strftime('%Y-%m-%d')},{dates['drop_date'].strftime('%Y-%m-%d')}"
        )

print("{{</mermaid>}}\n<!-- prettier-ignore-end -->")

# Print drop schedule

rel = {}
for name, releases in package_releases.items():
    rel |= {
        " ".join([name, str(ver)]): [dates["release_date"], dates["drop_date"]]
        for ver, dates in releases.items()
    }


current_quarter = pd.to_datetime(datetime.fromisoformat("1970-01-01")).to_period("Q")
rel = dict(sorted(rel.items(), key=lambda item: item[1][1]))
for package, dates in rel.items():
    qt = pd.to_datetime(dates[1]).to_period("Q")
    if qt != current_quarter:
        print(str(qt).replace("Q", " – Quarter "), "drop support for:")
        current_quarter = qt
    print(
        f"    {dates[1].strftime('%d %b %Y')} drop {package} (initially released on {dates[0].strftime('%b %d, %Y')})"
    )
