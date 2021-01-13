"""
SPE Registration
================

Register your project as a SPE.
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
project = input_("Project Name")
pypi = input_("What name is it register under on https://pypi.org/project/")
discussion = input_("Discussion number",
                    optional=True, validate=lambda x: int(x))

filename = f"{project.lower()}.md"
text = f"""---
project-name: "{project}"
date: {now.strftime("%Y-%m-%d")}
draft: false
discussion: {f'https://github.com/scientific-python/specs/discussions/{discussion}' if discussion else ''}
---

# Use in scientific research

<!--
Briefly describe how this project is used in scientific research.
-->

"""

with open(filename, "w") as file:
    file.write(text)
