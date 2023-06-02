import requests
import itertools
import collections
from datetime import datetime, timedelta

import pandas as pd
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

    print(f"Querying pypi.org for {package} versions...", end="", flush=True)
    response = requests.get(
        f"https://pypi.org/simple/{package}",
        headers={"Accept": "application/vnd.pypi.simple.v1+json"},
    ).json()
    print("OK")

    file_date = collections.defaultdict(list)
    for f in response["files"]:
        ver = f["filename"].split("-")[1]
        try:
            version = Version(ver)
        except:
            continue

        if version.is_prerelease or version.micro != 0:
            continue

        release_date = None
        for format in ["%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ"]:
            try:
                release_date = datetime.strptime(f["upload-time"], format)
            except:
                pass

        if not release_date:
            continue

        file_date[version].append(release_date)

    release_date = {v: min(file_date[v]) for v in file_date}

    for ver, release_date in sorted(release_date.items()):
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

# filter all items whose drop_date are in the past
package_releases = {
    package: {
        version: dates
        for version, dates in releases.items()
        if dates["drop_date"] > now
    }
    for package, releases in package_releases.items()
}


# Save Gantt chart

print("Saving Mermaid chart to chart.md")
with open("chart.md", "w") as fh:
    fh.write(
        """gantt
dateFormat YYYY-MM-DD
axisFormat %m / %Y
title Support Window"""
    )

    for name, releases in package_releases.items():
        fh.write(f"\n\nsection {name}")
        for version, dates in releases.items():
            fh.write(
                f"\n{version} : {dates['release_date'].strftime('%Y-%m-%d')},{dates['drop_date'].strftime('%Y-%m-%d')}"
            )
    fh.write("\n")

# Print drop schedule

rel = {}
for name, releases in package_releases.items():
    rel |= {
        " ".join([name, str(ver)]): [dates["release_date"], dates["drop_date"]]
        for ver, dates in releases.items()
    }


print("Saving drop schedule to schedule.md")
with open("schedule.md", "w") as fh:
    current_quarter = None

    # Sort by drop date
    rel = dict(sorted(rel.items(), key=lambda item: item[1][1]))

    for package, dates in rel.items():
        qt = pd.to_datetime(dates[1]).to_period("Q")

        # If drop date is in a new quarter, write out a heading
        if qt != current_quarter:
            if current_quarter != None:
                fh.write("\n")
            fh.write(f'{str(qt).replace("Q", " – Quarter ")}:\n\n')
            current_quarter = qt

        fh.write(
            f"- {dates[1].strftime('%d %b %Y')}: drop {package} (initially released on {dates[0].strftime('%b %d, %Y')})\n"
        )
