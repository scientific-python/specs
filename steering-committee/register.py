"""
Steering Committee Registration
===============================

Register as a steering committee member.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.tools"))
from tools import prompt


name = prompt("Name")
github_handle = prompt("GitHub Handle")
avatar = prompt("Avatar")

filename = f"{name.lower().replace(' ', '_')}.md"
text = f"""---
title: {name}
repository: https://github.com/{github_handle}
avatar: {avatar}
---
"""

with open(filename, "w") as file:
    file.write(text)
