"""
SPEC Quickstart
===============

Quickly setup stub for new SPEC proposal.
"""

from datetime import datetime

now = datetime.now()
author = input("Enter your name: ")
email = input("Enter your email address: ")
number = input("Enter the SPEC number: ")
title = input("Enter the SPEC title: ")
discussion = input("Enter the discussion number: ")

filename = f"spec-{number:04d}.md"
text = f"""---
title: "SPEC {number} — {title}"
date: {now.strftime("%Y-%m-%d")}
draft: false
author:
  - "{author} <{email}>"
discussion: https://github.com/scientific-python/specs/discussions/{discussion}
adopted-by:
---

# Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be
used, intended use-cases, and pseudo-code illustrating its use.
-->

# Implementation

<!--
Discuss how this would be implemented by projects.
-->

# Notes

<!--
Include a bulleted list of annotated links, comments, and other ancillary
information as needed.
-->
"""

with open(filename, "w") as file:
    file.write(text)
