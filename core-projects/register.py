"""
Core Project Registration
=========================

Register your core project.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.tools"))
from tools import prompt


project = prompt("Project Name")
project_lower = project.lower()
logo = prompt("Project Logo (from your GitHub organization profile pic)")
default_home = f"https://{project_lower}.org"
homepage = prompt("Project Homepage", default=default_home)
repository = prompt(
    "Repository", default=f"https://github.com/{project_lower}/{project_lower}"
)
pypi = prompt("PyPI page", default=f"https://pypi.org/project/{project_lower}")
license = prompt("License URL", default=f"{repository}/blob/main/LICENSE.txt")
license_type = prompt("License", default="3-clause BSD")
contact = prompt("List the GitHub handles of developers to contact about SPECs")

filename = f"{project.lower()}.md"
text = f"""---
title: "{project}"
avatar: {logo}
homepage: {homepage}
repository: {repository}
pypi: {pypi}
libraries-io: https://libraries.io/pypi/{pypi.split("/")[-1]}
license: {license}
license-type: {license_type}
contact: {contact}
---
"""

with open(filename, "w") as file:
    file.write(text)
