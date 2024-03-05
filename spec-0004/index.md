---
title: "SPEC 4 — Using and Creating Nightly Wheels"
date: 2022-09-05
author:
  - "Brigitta Sipőcz <brigitta.sipocz@gmail.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Matthew Feickert <matthew.feickert@cern.ch>"
  - "Matthias Bussonnier <bussonniermatthias@gmail.com>"
  - "Mridul Seth <mail@mriduls.com>"
  - "Olivier Grisel <olivier.grisel@ensta.org>"
  - "Tim Head <betatim@gmail.com>"

discussion: https://discuss.scientific-python.org/t/spec-4-nightly-wheels/474
endorsed-by:
  - ipython
  - networkx
  - numpy
  - scikit-image
  - scipy
  - xarray
  - scikit-learn
---

## Description

This SPEC describes how to test against nightly wheels of several widely used
projects and how to create nightly wheels for your project. The document uses the word
_nightly_ to refer to some semi regular interval, like daily, weekly, or every three days.

Regularly running your project's tests while using the nightly version of your
dependencies allows you to spot problems caused by upstream changes before a new release
is made. This way potential issues can be resolved before they find their way
into a release, at which point it becomes much harder to change or revert
something.

Regularly creating nightly wheels for your project allows projects that depend on
you to give feedback about upcoming changes. As with testing against nightlies of
your dependencies this gives your dependents a chance to report problems before they
find their way into a release.

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Implementation

This section outlines how to implement using and building nightly wheels. We assume your
project already has some amount of CI infrastructure and that you will have to fit this
in with the existing setup. In the notes section we link to the projects who have implemented
this in their setup to give you examples of complete setups.

### Test with Nightly Wheels

We recommend that projects add a weekly cron job to run their tests using nightly versions
of their dependencies. The cron job should automatically open an issue on your repository
when it encounters an error.

If you spot a problem please investigate if this is due to a known deprecation or
bug fix. If you think it is neither, please report it to the relevant upstream project.

To install the nightly version of your dependencies check which of them are available
at https://anaconda.org/scientific-python-nightly-wheels/. For example to install the NumPy and SciPy nightlies use:

```
python -m pip install --pre --upgrade --extra-index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple numpy scipy
```

Complete examples of how projects implement this in their CI setup are linked in the Notes section.

### Build Nightly Wheels

There are a few steps to implementing this for your project:

1. Get access to https://anaconda.org/scientific-python-nightly-wheels/, the location used to host nightly wheels
2. Setup a CI step that builds wheels for your project
3. Setup a CI step that uploads wheels to https://anaconda.org/scientific-python-nightly-wheels/

For step (1), visit https://github.com/scientific-python/upload-nightly-action and create an issue
requesting access. List the project you maintain and would like to upload nightlies for. We
will reply to the issue and let you know what happens next.

The work for step (2) depends on your project. You are probably already doing this for your
releases. The part to remember is building wheels regularly, at least once a week.

For step (3), there is a GitHub Action that you can use. You can find the action at
https://github.com/scientific-python/upload-nightly-action.
To use it in your "build wheels workflow", add the following lines as an additional step:

```
- name: Upload wheel
  uses: scientific-python/upload-nightly-action@main
  with:
    artifacts_path: dist/
    anaconda_nightly_upload_token: ${{ secrets.UPLOAD_TOKEN }}
```

Complete examples of how projects implement this in their CI setup are linked in the Notes section.

#### Artifact cleanup-policy at https://anaconda.org/scientific-python-nightly-wheels

To avoid hosting outdated development versions, as well as to clean up space, we do have a
retention policy of:

- Latest **N versions**
- Artifacts newer than **M days**

Any versions beyond these are automatically removed as part of a daily cron job. Projects may
have reasons to request to be added to the list exempt from this automated cleanup, however in that
case the responsibility of cleaning-up old, unused versions fall back on the individual project.

Note: The actual values for `N` and `M` are defined and documented in the
https://github.com/scientific-python/upload-nightly-action repository.

#### Process for Adding New Projects

The site admins are drawn from active members from the scientific Python community.
Ideally, the collection of admins comprises a broad selection of community
members across different projects and underlying organizations.
This is to ensure community ownership of the wheel-hosting infrastructure and
administration governed by consensus, as opposed to unilateral
decision-making by any individual, project, or organization.
Adding new administrators requires opening an issue.
After a project creates an issue on https://github.com/scientific-python/upload-nightly-action
requesting access to upload wheels, an admin has to respond to the request.

We wish to stay open to new projects uploading wheels with us. At the same time, we need to
perform some due diligence before giving access since approved projects gain the broad exposure
within the Scientific Python ecosystem. This could be abused by malicious actors.

A project's chosen representatives should each create an
account on https://anaconda.org and share their usernames with the
admins of the Scientific Python organization on Anaconda.
To increase resilience, we suggest that each project have at least two registered
representatives.

The representative can then generate a personal access token at
https://anaconda.org/[user]/settings/access and use it in CI to upload
wheels.
The token should only have the "Allow uploads to Standard Python repositories",
"Allow read access to the API site" and "Allow write access to the API site" scope.
The creation of tokens at the organization level should be avoided for security reasons.

The next step is to make an initial upload of a wheel to create the package listing on anaconda.org.
Once this operation is done, you can revoke your token and add the new user to its project.
Each project should have at least one user who is also an admin of the project.

At that point, let the user know that they have been added and that they can create a personal
access token (as outlined above.) They can now upload new wheels and perform maintenance
actions on their project.

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->

- [GitHub Action workflow for building and uploading scikit-learn wheels](https://github.com/scikit-learn/scikit-learn/blob/f034f57b1ad7bc5a7a5dd342543cea30c85e74ff/.github/workflows/wheels.yml)
  as an example of how to build wheels and upload them to the nightly area.
- [GitHub Action workflow for building and uploading NumPy wheels](https://github.com/numpy/numpy/blob/cc0abd768575d7f9e862de0b4912af27f6e9690d/.github/workflows/wheels.yml)
- Example of [a GitHub Action workflow that creates a tracking issue for failed CI runs](https://github.com/scikit-learn/scikit-learn/blob/689efe2f25356aa674bd0090f44b0914aae4d3a3/.github/workflows/update_tracking_issue.yml)
- Example of using [this action in NetworkX](https://github.com/networkx/networkx/blob/main/.github/workflows/nightly.yml) to publish a nightly release.
- Example of [a Jupyter notebook based tutorial repo](https://github.com/numpy/numpy-tutorials/blob/main/tox.ini) to test with multiple version combination, including using the nightly wheels for the development version.
- `astropy` ships [its own nightly wheel](https://docs.astropy.org/en/latest/install.html#installing-pre-built-development-versions-of-astropy)
  using [a workflow that relies on OpenAstronomy](https://github.com/astropy/astropy/blob/main/.github/workflows/publish.yml).
  Its direct dependency, `pyerfa`, also has nightly wheel [here](https://pypi.anaconda.org/liberfa/simple).
