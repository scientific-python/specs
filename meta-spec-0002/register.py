"""
SPE Registration
================

Register your project as a SPE.
"""

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


project = input_("Project Name")
homepage = input_("Project Homepage")
decision = input_("Adopted by approval URL")
repository = input_("Version control URL")
pypi = input_("Project name on https://pypi.org/project/")
license = input_("License URL")
license_type = input_("License (e.g., 3-clause BSD, GPL)")
adopters = input_("List the GitHub handles of developers who can adopt SPECs")

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
