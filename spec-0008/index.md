---
title: "SPEC 8 — Securing the Release Process"
number: 8
date: 2024-06-04
author:
  - "Matthew Feickert <matthew.feickert@cern.ch>"
  - "Pamphile Roy <roy.pamphile@gmail.com>"
  - "Juanita Gomez <juanitagomezr2112@gmail.com>"
  - "Seth Larson <sethmichaellarson@gmail.com>"
  - "Lars Grüter <lagru@mailbox.org>"
  - "Henry Schreiner <HenrySchreinerIII@gmail.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
endorsed-by:
  - networkx
  - numpy
  - pysal
  - scikit-image
  - scikit-learn
---

## Description

<!--
Briefly and clearly describe the recommendation.
https://github.com/scientific-python/summit-2024/issues/9
-->

Open source libraries constitute a significant portion of the world's digital infrastructure.
Securing the open source supply chain is therefore an increasing concern, with sophisticated attacks such as the 2024 [`xz` utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor) and [malware attacks on PyPI](https://blog.pypi.org/posts/2024-04-10-domain-abuse/) highlighting the need for stronger safeguards.
The Python Software Foundation (PSF) has also prioritized this work, including through the [creation of the PSF Security Developer in Residence position in 2023](https://pyfound.blogspot.com/2023/06/announcing-our-new-security-developer.html).

The [Supply-chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/) and [OpenID Connect (OIDC) standard](https://openid.net/developers/how-connect-works/) provide foundations for tools and practices that help projects secure their release processes.

This SPEC offers pragmatic recommendations for publishing release artifacts securely.
Specifically, we recommend:

- Document the release process.
- Require another maintainer's approval before publishing.
- Separate building from publishing, and give each job only the permissions it needs.
- Use approved workflow components pinned to immutable revisions, and review updates.
- Authenticate publishing workflows with short-lived credentials rather than stored, long-lived tokens.
- Publish digital attestations that allow others to verify the publishing identity and artifact integrity.

Securely _building_ release artifacts will be covered in a later SPEC.
These recommendations complement [SPEC 6 --- Keys to the Castle](https://github.com/scientific-python/specs/blob/main/spec-0006/index.md).

The implementation examples use GitHub Actions and PyPI, but the general recommendations apply more broadly to release workflows and distribution services.
The specific mechanisms depend on the services used.

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.
{{< spec_badge number="8" title="Securing the Release Process" >}}
To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).

## Implementation

With a focus on securing the release artifact distribution process, the following processes and standards should be adopted.

### Document the release process

The release process should be clearly and fully documented in the developer documentation and describe each step to make a release and the permissions required to do so.
It is recommended that this is a dedicated page in the developer section of the documentation website, though providing instructions in a `RELEASING.md` in the top level of the repository is also a common approach.

### Hardening workflow environment permissions

- Workflows that publish release artifacts should have _run triggers_ that require intentional actions by the release team (e.g., `workflow_dispatch` in GitHub Actions) and require multiple release team members to approve the workflow to run (c.f. "Use GitHub Actions environments" section below).
  This is to safeguard the project from any one maintainer having the ability to commit to the default branch and make a release directly.

- It is also strongly recommended that release managers use [signed commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits), so that each release corresponds to a verified commit.
  It can be difficult to enforce this via GitHub permissions without requiring all contributors to sign their commits.
- The branch from which the release is made should also be protected.

#### Separate building from publishing

Release artifacts should be built in a separate job from the job that publishes them.
The build job should upload the completed distributions as workflow artifacts, and the publishing job should only download those artifacts and upload them to a package index, e.g. PyPI.
This separation ensures that build and test code does not run with publishing credentials and that the artifacts tested are the same artifacts that are published.

When a workflow checks out the repository, set `persist-credentials: false` unless later steps explicitly require the checkout credentials.

```yaml
- uses: actions/checkout@<full action commit SHA> # vX.Y.Z
  with:
    persist-credentials: false
```

#### Restrict permissions in CI runners to the minimum required

To restrict the attack surface area of arbitrary code execution in CI runners, the _default_ runner permissions should be set to none.
In the GitHub Actions workflow, this is accomplished by defining the following workflow-level permissions block before any jobs are defined.

```yaml
permissions: {}
```

Each job should then grant only the permissions it requires.
For example, a build job that checks out a private repository may need `contents: read`, while the PyPI publishing job needs `id-token: write` for trusted publishing.

#### Restrict permitted actions in workflows

GitHub allows restricting the actions that workflows can use via the repository actions permissions settings at `https://github.com/$ORG/$PROJECT/settings/actions`.
A reasonable default is to select the

- Allow `$ORG`, and select `non-$ORG`, actions and reusable workflows

option and the suboptions:

- Allow actions created by GitHub
- Allow specified actions and reusable workflows

Consult [Managing GitHub Actions permissions for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository) for more details.

#### Use GitHub Actions environments

Use a [GitHub Actions environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)

```yaml
environment:
  name: publish-package
```

and enforce additional review by at least one other release team maintainer to run a GitHub Actions workflow that publishes to PyPI.
Additional reviewer requirements can be configured per GitHub Actions environment under `https://github.com/$ORG/$PROJECT/settings/environments/` in the "Deployment protection rules" section.

![github-actions-environment](https://hackmd.io/_uploads/S1SErQ0EC.png)

### Pin GitHub Actions release workflows to their full release commit SHAs

GitHub Actions must be pinned using the full commit SHA corresponding to the release version being used.
Using versions, branches, tags, or abbreviated hashes is susceptible to attacks.
Include the corresponding release version in a comment, and update pinned actions regularly through a reviewed process so that related actions remain compatible.
Use a tool, like zizmor, to ensure that hashes are actually from the repository and not from a fork.

```yaml
- uses: actions/some-action@1fe14e04876783b259436247a3898d2fe7d5548f # vX.Y.Z
```

Dependabot can be used to automatically propose updates to the hashes.
It is important that updates are carefully reviewed before being merged.

```yaml
# .github/dependabot.yml
version: 2
updates:
  # Maintain dependencies for GitHub Actions
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "monthly"
    groups:
      actions:
        patterns:
          - "*"
```

### Adopt OIDC through the use of PyPI Trusted Publishers

[Trusted Publishers](https://docs.pypi.org/trusted-publishers/) provide a way to securely establish a short-lived authentication token between a project repository and a distribution platform &mdash; such as PyPI.
This replaces the need to use a long-lived token to authenticate, reducing the security risks associated with authentication tokens (e.g., tokens being compromised or needing to be rotated).

Trusted Publishers can be used in GitHub Actions by using the [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish) GitHub Action defaults in a GitHub Actions environment.
When used with Trusted Publishing, this action generates and uploads [PEP 740](https://peps.python.org/pep-0740/) digital attestations by default, so a separate attestation step is not required.
The published provenance can be retrieved through PyPI's [Integrity API](https://docs.pypi.org/api/integrity/) and verified using tools such as [`pypi-attestations`](https://github.com/pypa/pypi-attestations).

```yaml
jobs:
  publish:
    name: Publish release to PyPI
    runs-on: ubuntu-latest
    environment: publish-package
    permissions:
      # IMPORTANT: this permission is mandatory for trusted publishing
      id-token: write
    steps:
      # Download distributions built by a separate job here.
      # ...

      - name: Publish distribution to PyPI
        uses: pypa/gh-action-pypi-publish@<full action commit SHA> # vX.Y.Z
        with:
          print-hash: true
```

Projects that cannot use Trusted Publishing should still generate and publish provenance attestations where their build and distribution services support them.
For example, GitHub's [`actions/attest-build-provenance`](https://github.com/actions/attest-build-provenance) can generate SLSA build provenance for artifacts produced by GitHub Actions.

### Example workflow

The following is a complete example of a workflow which can be used as a starting point:

```yaml
name: publish distributions

on:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions: {}

jobs:
  publish:
    name: Publish Python distributions to PyPI
    # Distributions will have been built in a previous job
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: publish-package
    permissions:
      id-token: write

    steps:
      - name: Download distributions
        uses: actions/download-artifact@<full action commit SHA> # vX.Y.Z
        with:
          name: python-package-distributions
          path: dist/

      - name: Publish distributions to PyPI
        uses: pypa/gh-action-pypi-publish@<full action commit SHA> # vX.Y.Z
        with:
          print-hash: true
```

## Notes

- [Concise Guide for Developing More Secure Software from the OpenSSF](https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software)
- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)
- [PyPI Digital Attestations](https://docs.pypi.org/attestations/)
- [PyPI Integrity API](https://docs.pypi.org/api/integrity/)
