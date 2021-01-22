"""
SPE Registration
================

Register your project as a SPE.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../.tools'))
from tools import prompt


project = prompt("Project Name")
homepage = prompt("Project Homepage")
decision = prompt("Adopted by approval URL")
repository = prompt("Version control URL")
pypi = prompt("Project name on https://pypi.org/project/")
license = prompt("License URL")
license_type = prompt("License (e.g., 3-clause BSD, GPL)")
adopters = prompt("List the GitHub handles of developers who can adopt SPECs")

filename = f"projects/{project.lower()}.md"
text = f"""---
title: "{project}"
draft: false
homepage: {homepage}
repository: {repository}
pypi: https://pypi.org/project/{pypi}
libraries-io: https://libraries.io/pypi/{pypi}
license: {license}
license_type: {license_type}
adopters: {adopters}
---

"""

with open(filename, "w") as file:
    file.write(text)
