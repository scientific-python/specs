---
title: "SPEC 9 — Governance"
number: 9
date: 2024-06-04
author:
  - "Sanket Verma <svsanketverma5@gmail.com>"
discussion: https://discuss.scientific-python.org/t/spec-9-governance/1229
endorsed-by:
---

## Description

This SPEC describes what governance is, and offers recommendations for choosing a
governance model for open-source projects.

Open-source project communities are amalgamations of software and the humans who
use and maintain it. Governance models define methods for decision-making within a
project, roles for the community members imbued with decision-making authority, and
processes for filling (and if needed, vacating) those leadership roles.
In the context of open-source software projects, governance models often also define the
granting of necessary permissions or access to organization secrets necessary for the
implementation of project-related decisions. Governance models are complementary to
Codes of Conduct and Community Guidelines, which define the expectations and
responsibilities of all participants in a project (including users of the software),
regardless of their status as a project leader (cf. SPEC XXX).

Having a robust system in place ensures the long-term sustainability of the
project.

The OS communities interact and contribute through various mediums, such as
distributed version control systems, chat platforms, social media, blog posts, etc. Having clear guidelines
for participation helps maintain a continuous stream of contributions.

This SPEC outlines the definition of governance, various open-source governance
models, the steps to choose the right governance model, and what needs to be
done post-adoption.

Please note that these are recommendations and not bylaws. If you have
suggestions/thoughts, we're more than happy to consider them.

### Core Project Endorsement

<!--
Briefly discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Briefly discuss what it means for a project to adopt this SPEC.
-->

## Implementation

### Choosing a governance model

When you define governance for a project, you need to identify a few things:

- What roles does maintainers, core team, contributors, and community members
  play in the project?
- What duties, privileges, and authority are associate with each role?
- How do people get assigned to and removed from roles?
- How decisions are made and documented within the project?
- What are the methods for resolving conflicts?

There are few **pre-defined models** for governance used across open-source
projects. We'll mention them here for reference:

- BDFL
  - BDFL stands for 'Benevolent Dictator for Life.' Under this structure, one
    person (usually the project's initial author) has the final say on all
    major project decisions. Smaller projects are BDFL by default because
    there are only one or two maintainers.
  - BDFL model template → http://oss-watch.ac.uk/resources/benevolentdictatorgovernancemodel
- Meritocracy / Do-ocracy
  - Decisions are made by contributors who have demonstrated merit through
    their contributions to the project. Merit is often gained through
    contributions of code, documentation, or other significant efforts.
  - Meritocracy model template → http://oss-watch.ac.uk/resources/meritocraticgovernancemodel
- Self appointing council / committee / board
  - This model appoints a board or committee to govern various aspects of a
    project. Those groups are often called the steering committee, committer
    council, technical operation committee, board of directors, etc. This
    model might be helpful for projects that need a sponsoring foundation,
    and establishing electoral mechanisms is challenging.
- Electoral
  - The electoral governance model in open-source projects is a structured
    approach in which the community elects the leadership or decision-making
    body. This model aims to ensure that those who guide the project's
    direction and make crucial decisions are chosen democratically,
    representing the broader community's interests.
- Corporate backed / Single vendor
  - A single company or organization controls the project, often making
    decisions internally. The company might appoint maintainers and decide
    the project's direction.
- Foundation backed
  - A non-profit foundation oversees the project, and its governance
    structures often include a board of directors, technical committees, and
    working groups.

**Other governance models**

- Liberal contribution
  - Under a liberal contribution model, the people who do the most work are
    recognized as influential. Major project decisions are made based on a
    consensus-seeking process (discussing major grievances) rather than pure
    vote, and the team strives to include as many community perspectives as
    possible.
  - Example: Node.js liberal contribution policy → https://medium.com/the-node-js-collection/healthy-open-source-967fa8be7951
- C4 (Collective Code Construction Contract)
  - https://rfc.zeromq.org/spec/22/

### Choosing the right governance model

Choosing the right governance model for your open-source project involves
considering several factors to ensure the structure aligns with your project’s
goals, community, and resources. Most open-source projects start with the BDFL
model; eventually, they grow and adopt more open models.

A few things you should consider while choosing the right model:

- **Project lifecycle stage**
  - Early stage
  - Growth stage
  - Mature stage
- **Assess your project's needs and goals**
  - Project size and complexity
  - Community involvement
- **Evaluate available resources**
  - Leadership and management capacity
- **Community dynamics**
  - Large, diverse communities might benefit from democratic or meritocratic
    models to represent various interests
  - Smaller, homogeneous communities are more suited for a BDFL model
- **Technical and Operational Complexity**
  - Complex projects with numerous sub-projects or components may need a
    structured governance model to manage them effectively
- **Flexibility and Adaptability**
  - Choose a model that allows for future adjustments as the project evolves
  - Implement mechanisms for regular feedback from the community on governance
    effectiveness
- **External Stakeholders**
  - Consider how partnerships with other projects, organizations, or companies
    might influence governance
- **Legal and financial considerations**
  - If the project needs to be incorporated as a non-profit, foundation, or
    under a company
  - Assess the sources of funding and how they influence governance

### What to do after the adoption?

Once a project has adopted a governance model, the several important steps could
be followed to ensure smooth implementation and operation.

- **Document the governance model**
  - Clearly document the governance model, including roles, responsibilities,
    decision-making processes, and procedures for conflict resolution.
  - https://communityrule.info/templates/ offers an excellent interface where
    you can create a `.md` for your governance model
- **Communicate to the Community**
  - Make a public announcement about the adoption of the new governance model
  - Provide an overview of how the governance model works, why it was chosen,
    and what it means for the community
- **Implement the governance structure**
  - Assign initial roles and responsibilities
  - Form any necessary committees, councils, or boards as defined by the
    governance model
- **Fostering community engagement and ensuring transparency and
  accountability**
  - Provide regular updates and reports to the community on governance
    activities, decisions, and project progress
  - Establish mechanisms for the community to provide feedback on the
    governance model and its implementation
  - Maintain transparency by making all governance-related documentation,
    meeting minutes, and decisions publicly available. You can use public
    repository or a website for this.
- **Establish Conflict Resolution Processes**
  - Implement formal mechanisms for resolving conflicts within the community
    and governance bodies. Ensure these mechanisms are fair, transparent,
    account for diversity and inclusion, and accessible to all community
    members.

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
