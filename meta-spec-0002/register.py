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
homepage = input_("Project Homepage")
decision = input_("Adopted by approval URL")
vcs = input_("Version control URL")
pypi = input_("Project name on https://pypi.org/project/")
coc = input_("Code of Conduct URL")
contributor_guide = input_("Contributor Guide URL")
roadmap = input_("Roadmap URL")
mailing_list = input_("Mailing List URL")
governance_guide = input_("Governance Guide URL")
license = input_("License URL")
license_type = input_("License (e.g., 3-clause BSD, GPL)")
api_reference = input_("API Documentation URL")
test_coverage = input_("Test Coverage URL")
adopters = input_("List the github handles of developers who can adopt SPECs")
# first_release =  # maybe just read from PyPI?
discussion = input_("Discussion number",
                    optional=True, validate=lambda x: int(x))

filename = f"projects/{project.lower()}.md"
text = f"""---
title: "{project}"
homepage: {homepage}
date: {now.strftime("%Y-%m-%d")}
draft: false
decision: {decision}
vcs: {vcs}
pypi: {f'https://pypi.org/project/{pypi}'}
coc: {coc}
contributor_guide: {contributor_guide}
roadmap: {roadmap}
mailing_list: {mailing_list}
governance_guide: {governance_guide}
license: {license}
license_type: {license_type}
api_reference: {api_reference}
test_coverage: {test_coverage}
adopters: {adopters}
discussion: {f'https://github.com/scientific-python/specs/discussions/{discussion}' if discussion else ''}
---

# What is {project}?

<!--
In one or two sentences, describe what your package does.
-->

# How is it used in scientific research?

<!--
In one or two paragraphs, describe how this project is used in scientific research.
-->

# What is the development community like? 

<!--
In one or two paragraphs, describe your developer team.
How many people are on the core developer team?
Where do developers come from (e.g., do new contributors just show up or are they hired)?
Is it all voluteers?
How do new contributors become core developers?
-->

# How does it exchange data with projects in the ecosystem? 

<!--
Briefly describe how data is exchanged between your projects and other
projects in the ecosystem.
-->

"""

with open(filename, "w") as file:
    file.write(text)
