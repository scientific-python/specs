from datetime import datetime, timedelta
from tabulate import tabulate

data = """Jun 27, 2018: Python 3.7
Oct 14, 2019: Python 3.8
Oct 5, 2020: Python 3.9
Jul 23, 2018: NumPy 1.15
Jan 13, 2019: NumPy 1.16
Jul 26, 2019: NumPy 1.17
Dec 22, 2019: NumPy 1.18
Jun 20, 2020: NumPy 1.19
Dec 17, 2018: SciPy 1.2
May 17, 2019: SciPy 1.3
Dec 16, 2019: SciPy 1.4
Jun 21, 2020: SciPy 1.5
Dec 31, 2020: SciPy 1.6
Sep 18, 2018: Matplotlib 3.0
May 18, 2019: Matplotlib 3.1
Mar 4, 2020: Matplotlib 3.2
Jul 16, 2020: Matplotlib 3.3
"""

releases = []

plus42 = timedelta(days=int(365 * 3.5 + 1))
plus24 = timedelta(days=int(365 * 2 + 1))

for line in data.splitlines():
    date, project_version = line.split(":")
    project, version = project_version.strip().split(" ")
    release = datetime.strptime(date, "%b %d, %Y")
    if project.lower() == "python":
        drop = release + plus42
    else:
        drop = release + plus24
    releases.append((drop, project, version, release))

releases = sorted(releases, key=lambda x: x[0])


def version_numbers(release):
    return [int(num) for num in release[2].split(".")]


py_versions = sorted(version_numbers(r) for r in releases if r[1] == "Python")
py_major, py_minor = py_versions[-1]
py_min = f"{py_major}.{py_minor+1}+"

np_versions = sorted(version_numbers(r) for r in releases if r[1] == "NumPy")
np_major, np_minor = np_versions[-1]
np_min = f"{np_major}.{np_minor+1}+"

sp_versions = sorted(version_numbers(r) for r in releases if r[1] == "SciPy")
sp_major, sp_minor = sp_versions[-1]
sp_min = f"{sp_major}.{sp_minor+1}+"

mpl_versions = sorted(version_numbers(r) for r in releases if r[1] == "Matplotlib")
mpl_major, mpl_minor = mpl_versions[-1]
mpl_min = f"{mpl_major}.{mpl_minor+1}+"


drop_dates = [""]
support_table = []
for d, p, v, r in releases[::-1]:
    df = d.strftime("%b %d, %Y")
    drop_dates.append(
        f"On {df} drop support for {p} {v} "
        f"(initially released on {r.strftime('%b %d, %Y')})"
    )
    support_table.append([df, py_min, np_min, sp_min, mpl_min])
    if p == "Python":
        py_min = v + "+"
    elif p == "NumPy":
        np_min = v + "+"
    elif p == "SciPy":
        sp_min = v + "+"
    elif p == "Matplotlib":
        mpl_min = v + "+"

for e in drop_dates[-4::-1]:
    print(e)

headers = ["Date", "Python", "NumPy", "SciPy", "Matplotlib"]
support_table.reverse()
print(tabulate(support_table, headers, tablefmt="github"))
