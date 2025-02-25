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
  - "Jarrod Millman <millman@berkeley.edu>"
endorsed-by:
  - networkx
  - numpy
  - scikit-image
  - scikit-learn
---

## Description

<!--
Briefly and clearly describe the recommendation.
https://github.com/scientific-python/summit-2024/issues/9
-->

Open source libraries constitute a significant portion of the world's digital infrastructure. Securing the Open Source supply chain (OSSC) is therefore an increasing concern, with examples of sophisticated attacks against the ecosystem (e.g., the 2024 [`xz` utils backdoor](https://en.wikipedia.org/wiki/XZ_Utils_backdoor)) and [malware attacks on PyPI](https://blog.pypi.org/posts/2024-04-10-domain-abuse/) highlighting the need for supply chain security to be taken seriously.
The Python Software Foundation (PSF) is also taking the importance of the OSSC seriously, as demonstrated by the [creation of the PSF Security Developer in Residence position in 2023](https://pyfound.blogspot.com/2023/06/announcing-our-new-security-developer.html).

With the [Supply-chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/) and [OpenID Connect (OIDC) standard](https://openid.net/developers/how-connect-works/) being widely adopted, several high level developer tools, maintained by professional security teams, have been created with clear recommendations on how to use them.

This SPEC outlines pragmatic recommendations for adopting these security tools and recommendations on how to publish release artifacts securely.
Securely _building_ release artifacts will be covered in a later SPEC. This set of recommendations complements the recommendations from [SPEC 6 — Keys to the Castle](https://github.com/scientific-python/specs/blob/main/spec-0006/index.md).

While this SPEC is written with GitHub in mind, the same recommendations apply to other services, such as GitLab.

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

- It is also strongly recommended that the repository requires [signed commits](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits) so that each release corresponds to a verified commit.
- The branch from which the release is made should also be protected.

#### Restrict permissions in CI runners to the minimum required

To restrict the attack surface area of arbitrary code execution in CI runners, the _default_ runner permissions should be restricted to the minimum possible (read access). In the GitHub Action workflow, this is accomplished by defining the following workflow global permissions block before any jobs are defined.

```yaml
permissions:
  contents: read
```

Elevating permissions beyond this should be done at the job level by redefining the permissions block in the job.

#### Restrict permitted actions in workflows

GitHub allows restricting the actions that workflows can use via the repository actions permissions settings at `https://github.com/$ORG/$PROJECT/settings/actions`.
A reasonable default is to select the

- Allow `$ORG`, and select `non-$ORG`, actions and reusable workflows

option and the suboptions:

- Allow actions created by GitHub
- Allow specified actions and reusable workflows

Consult [Managing GitHub Actions permissions for your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#managing-github-actions-permissions-for-your-repository) for more details.

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

GitHub actions must be pinned using full commit SHA corresponding to the release version being used.
Using versions or small hashes is susceptible to attacks.

```yaml
- uses: actions/some-action@1fe14e04876783b259436247a3898d2fe7d5548f #vX.Y.Z
```

Dependabot can be used to automatically update the hashes.
It is important that this happens as part of a reviewed process.

```yaml!
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

### Adopt SLSA through use of GitHub Attestations

A component of SLSA is [software attestation](https://slsa.dev/attestation-model) which allows for public validation of software artifacts and provenance.
GitHub provides the [`actions/attest-build-provenance`](https://github.com/actions/attest-build-provenance) GitHub Action which implements SLSA to generate signed build provenance attestations for workflow artifacts.
Attestations are published to the project GitHub under `https://github.com/$ORG/$PROJECT/attestations/`.

```yaml
- uses: actions/attest-build-provenance@<full action commit SHA> # vX.Y.Z
  with:
    subject-path: "dist/<package name>-*"
```

GitHub has also added the [`gh attestation verify`](https://cli.github.com/manual/gh_attestation_verify) command to the GitHub CLI utility, which verifies the integrity and provenance of an artifact using its associated cryptographically signed attestations.
This can be used by individual users and also in GitHub Actions workflows where the GitHub CLI utility is installed by default.

```yaml
- name: Verify artifact attestation
  env:
    GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  shell: bash
  run: |
    for artifact in dist/*; do
        echo "# ${artifact}"
        gh attestation verify "${artifact}" --repo ${{ github.repository }}
    done
```

### Adopt OIDC through the use of PyPI Trusted Publishers

[Trusted Publishers](https://docs.pypi.org/trusted-publishers/) provide a way to securely establish a short lived authentication token between a project repository and a distribution platform &mdash; such as PyPI.
It replaces the need to use a long lived token to authenticate, reducing the security risks associated with authentication tokens (e.g., tokens being compromised, the need to rotate tokens).

Trusted Publishers can be used in GitHub Actions by using the [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish) GitHub Action defaults in a GitHub Actions environment.

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
      # retrieve your distributions here
      # ...

      - name: Publish distribution to PyPI
        uses: pypa/gh-action-pypi-publish@<full action commit SHA> # vX.Y.Z
        with:
          print-hash: true
```

### Example workflow

The following is a complete example of a workflow which can be used as a starting point:

```yaml
name: publish distributions

on:
  workflow_dispatch:

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

permissions:
  contents: read

jobs:
  publish:
    name: Publish Python distribution to PyPI
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      attestations: write
    environment:
      name: publish-package

    steps:
      # - name: Collect built artifacts
      # ...

      - name: Generate artifact attestation for sdist and wheels
        uses: actions/attest-build-provenance@<full action commit SHA> # vX.Y.Z
        with:
          subject-path: "dist/<package name>-*"

      - name: Verify artifact attestation
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        shell: bash
        run: |
          for artifact in dist/*; do
              echo "# ${artifact}"
              gh attestation verify "${artifact}" --repo ${{ github.repository }}
          done

      - name: Publish distribution to PyPI
        uses: pypa/gh-action-pypi-publish@<full action commit SHA> # vX.Y.Z
        with:
          print-hash: true
```

## Notes

- [Concise Guide for Developing More Secure Software from the OpenSSF](https://best.openssf.org/Concise-Guide-for-Developing-More-Secure-Software)
- [GitHub Blog: Introducing Artifact Attestations–now in public beta](https://github.blog/2024-05-02-introducing-artifact-attestations-now-in-public-beta/)
