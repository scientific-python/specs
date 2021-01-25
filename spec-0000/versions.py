from datetime import datetime, timedelta

plus36 = timedelta(days=int(365 * 3))
plus24 = timedelta(days=int(365 * 2))

# Release data

py_releases = {
    3.7: "Jun 27, 2018",
    3.8: "Oct 14, 2019",
    3.9: "Oct 5, 2020",
}

np_releases = {
    1.17: "Jul 26, 2019",
    1.18: "Dec 22, 2019",
    1.19: "Jun 20, 2020",
}

sp_releases = {
    1.3: "May 17, 2019",
    1.4: "Dec 16, 2019",
    1.5: "Jun 21, 2020",
    1.6: "Dec 31, 2020",
}

mpl_releases = {
    3.1: "May 18, 2019",
    3.2: "Mar 4, 2020",
    3.3: "Jul 16, 2020",
}

# Get support window


def support_window(project, releases, support_time):
    windows = []
    for version, release_date in releases.items():
        release = datetime.strptime(release_date, "%b %d, %Y")
        drop = release + support_time
        windows.append((project, version, release, drop))
    return windows


py_support_window = support_window("Python", py_releases, plus36)
np_support_window = support_window("NumPy", np_releases, plus24)
sp_support_window = support_window("SciPy", sp_releases, plus24)
mpl_support_window = support_window("Matplotlib", mpl_releases, plus24)


# Print Gantt chart


def gantt_section(window, prefix):
    section = ""
    for project, version, release, drop in window:
        version_name = prefix + str(version).replace(".", "")
        release_date = release.strftime("%Y-%m-%d")
        drop_date = drop.strftime("%Y-%m-%d")
        section += f"{version}  :     {version_name}, {release_date},{drop_date}\n"
    return section


py_gantt_section = gantt_section(py_support_window, "py")
np_gantt_section = gantt_section(np_support_window, "np")
sp_gantt_section = gantt_section(sp_support_window, "sp")
mpl_gantt_section = gantt_section(mpl_support_window, "mpl")

gantt = f"""
<!-- prettier-ignore-start -->
{{{{<mermaid>}}}}
gantt
dateFormat  YYYY-MM-DD
axisFormat  %m / %Y
title Support Window

section Python
{py_gantt_section}
section NumPy
{np_gantt_section}
section SciPy
{sp_gantt_section}
section Matplotlib
{mpl_gantt_section}
{{{{</mermaid>}}}}
<!-- prettier-ignore-end -->
"""

print(gantt)

# Print drop schedule


def get_drop_dates(window):
    return {" ".join([proj, str(ver)]): [rel, drop] for proj, ver, rel, drop in window}


py_drop = get_drop_dates(py_support_window)
np_drop = get_drop_dates(np_support_window)
sp_drop = get_drop_dates(sp_support_window)
mpl_drop = get_drop_dates(mpl_support_window)

releases = py_drop | np_drop | sp_drop | mpl_drop
releases = dict(sorted(releases.items(), key=lambda item: item[1][1]))

for package, dates in releases.items():
    print(
        f"On {dates[1].strftime('%b %d, %Y')} drop support for {package} "
        f"(initially released on {dates[0].strftime('%b %d, %Y')})"
    )
