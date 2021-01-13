"""
SPEC Quickstart
===============

Quickly setup stub for new SPEC proposal.
"""

from datetime import datetime


def input_(
        prompt,
        optional=False,
        validate=lambda x: x if x else None
):
    def valid(s):
        if optional and not s:
            return ""
        try:
            return validate(s)
        except (ValueError, TypeError):
            print('Invalid input; please try again.')
            return None

    optional_flag = ' [optional]' if optional else ''
    while (ans := valid(input(f'{prompt}{optional_flag}: '))) is None:
        pass

    return ans


now = datetime.now()
author = input_("Your Name")
email = input_("Your Email Address")
number = input_("SPEC number", validate=lambda x: int(x))
title = input_("SPEC title")
discussion = input_("Discussion number",
                    optional=True, validate=lambda x: int(x))

filename = f"spec-{number:04d}.md"
text = f"""---
title: "SPEC {number} — {title}"
date: {now.strftime("%Y-%m-%d")}
draft: false
author:
  - "{author} <{email}>"
discussion: {f'https://github.com/scientific-python/specs/discussions/{discussion}' if discussion else ''}
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
