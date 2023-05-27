---
title: "SPEC 4 — Using and Creating Nightly Wheels"
date: 2022-09-05
author:
  - "Matthew Feickert <matthew.feickert@cern.ch>"
  - "Olivier Grisel <olivier.grisel@ensta.org>"
  - "Tim Head <betatim@gmail.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-4-nightly-wheels/474
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

This SPEC describes how to test against nightly wheels of several widely used
projects and how to create nightly wheels for your project.

Regularly running your project's tests while using the nightly version of your
dependencies allows you to spot problems caused by upstream changes before a new release
is made. This way potential issues can be resolved before they find their way
into a release, at which point it becomes much harder to change or revert
something.

Regularly creating nightly wheels for your project allows projects that depend on
you to give feedback about upcoming changes. As with testing against nightlies of
your dependencies this gives your dependents a chance to report problems before they
find their way into a release.

## Implementation

This section outlines how to implement using and building nightly wheels. We assume your
project already has some amount of CI infrastructure and that you will have to fit this
in with the existing setup. In the notes section we link to projects who have implemented
this in their setup to give you examples of complete setups.

### Test with Nightly Wheels

We recommend that projects add a weekly cron job to run their tests using nightly versions
of their dependencies. The cron job should automatically open an issue on your repository
when it encounters an error.

If you spot a problem please investigate if this is due to a known deprecation or
bug fix. If you think it is neither, please report it to the relevant upstream project.

To install the nightly version of your dependencies check which of them are available
at https://anaconda.org/scientific-python-nightly-wheels/. For example to install the NumPy and scipy nightlies use:

```
pip install --pre --upgrade --extra-index https://pypi.anaconda.org/scientific-python-nightly-wheels/simple numpy scipy
```

Complete examples of how projects implement this in their CI setup are linked in the Notes section.

### Build Nightly Wheels

There are a few steps to implementing this for your project:

1. Get access to https://anaconda.org/scientific-python-nightly-wheels/, the location used to host nightly wheels
2. Setup a CI step that builds wheels for your project
3. Setup a CI step that uploads wheels to https://anaconda.org/scientific-python-nightly-wheels/

For step (1) visit https://github.com/scientific-python/upload-nightly-action and create an issue
requesting access. List the project you maintain and would like to upload nightlies for. Someone
will reply to the issue and let you know what happens next.

The work for step (2) depends on your project. You are probably already doing this for your
releases. The new thing to add is that building wheels is run on a schedule every night or
once a week.

For step (3) there is a GitHub Action that you can use. You can find the action at
https://github.com/scientific-python/upload-nightly-action. To use it in your "build wheels
workflow" add the following lines as an additional step:

```
- name: Upload wheel
  uses: scientific-python/upload-nightly-action@main
  with:
    artifacts_path: dist/
    anaconda_nightly_upload_token: ${{ secrets.UPLOAD_TOKEN }}
```

Complete examples of how projects implement this in their CI setup are linked in the Notes section.

#### Process for Adding New Projects

After someone creates an issue on https://github.com/scientific-python/upload-nightly-action
requesting access to upload wheels a human/admin has to respond to that request.

Admins are people from the community who are ideally not part of the same organizations nor
project. This is to prevent malicious activities from a given group of actors and ensure a
diverse and healthy community. Adding new people to the list requires of admins requires at
least an issue to be openned.

We want to be open to projects uploading wheels but at the same time need to perform some
amount of due dilligence before giving people access. This is because once a user is given
access their work will be broadcasted through the broad exposure of Scientific Python. This
could be abused to publish malicious packages.

Once you have established who the person is and that they represent the project they want
to upload wheels for ask the person to create an account on https://anaconda.org and tell
you the username. We suggest that projects have a least 2 representatives and ideally they
should not be part of the same organization to ensure a diverse community.

You (as an admin) can then generate a personal access token at
https://anaconda.org/[user]/settings/access.
The token should only have the "Allow uploads to Standard Python repositories" and
"Allow write access to the API site" scope. The creation of tokens at the organization
level should be avoided for security reasons.

Then you need to do a first upload of a wheel to create the package listing on anaconda.org.
Once this operation is done, you can revoke your token and add the new user to its project.
For a given project, at leat one user should be admin of that project.

At that point, let the user know that they have been added and that they can create a personal
access token (as outlined above.) They can now upload new wheels and perform maitenance
actions on their project.

## Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

## Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->

- You can use [scikit-learn's GitHub Action wheels building workflow](https://github.com/scikit-learn/scikit-learn/blob/f034f57b1ad7bc5a7a5dd342543cea30c85e74ff/.github/workflows/wheels.yml)
  as an example of how to build wheels and upload them to the nightly area.
- [numpy's GitHub Action workflow for building wheels and uploading them](https://github.com/numpy/numpy/blob/cc0abd768575d7f9e862de0b4912af27f6e9690d/.github/workflows/wheels.yml)
- An example of [a GitHub Action workflow that creates a tracking issue for failed CI runs](https://github.com/scikit-learn/scikit-learn/blob/689efe2f25356aa674bd0090f44b0914aae4d3a3/.github/workflows/update_tracking_issue.yml)
- An example of using [this action in NetworkX](https://github.com/networkx/networkx/blob/main/.github/workflows/nightly.yml) to publish a nightly release.
