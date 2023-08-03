---
title: "SPEC 2 — API Dispatch"
date: 2021-12-16
author:
  - "Ivan Yashchuk <ivan.yashchuk@quansight.com>"
  - "Ralf Gommers <rgommers@quansight.com>"
  - "Jarrod Millman <millman@berkeley.edu>"
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
discussion: https://discuss.scientific-python.org/t/spec-2-api-dispatch/173
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the recommendation.
Explain the general need and the advantages of this specific recommendation.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

We propose mechanisms for:

(a) wholesale reimplementations of library functions, and
(b) function dispatch based on foreign data structures.

This would allow groups outside of, say, `scipy` to (a) provide new
functions to replace parts of SciPy, or (b) provide data structures
that can pass through SciPy's existing computational pipelines.

Concretely, (a) is akin to monkey-patching, but with the advantage
that libraries can coordinate dispatching and report which backend is
being used. And (b) is similar to using the [Array API standard](https://data-apis.org/array-api/latest/index.html), so that
pure-Python algorithm implementations can operate on foreign array types
without rewriting code.

This SPEC focuses on the rationale for these mechanisms, and provides
links to implementations related technical discussions.

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->

- [A vision for extensibility to GPU & distributed support for SciPy, scikit-learn, scikit-image and beyond](https://labs.quansight.org/blog/2021/11/pydata-extensibility-vision/)
- [A proposed design for supporting multiple array types across SciPy, scikit-learn, scikit-image and beyond](https://discuss.scientific-python.org/t/a-proposed-design-for-supporting-multiple-array-types-across-scipy-scikit-learn-scikit-image-and-beyond/131)
- [Support for array types other than NumPy](https://discuss.scientific-python.org/t/support-for-array-types-other-than-numpy/134)
- [Default dispatching behavior for supporting multiple array types across SciPy, scikit-learn, scikit-image](https://discuss.scientific-python.org/t/default-dispatching-behavior-for-supporting-multiple-array-types-across-scipy-scikit-learn-scikit-image/135)
- [Requirements and discussion of a type dispatcher for the ecosystem](https://discuss.scientific-python.org/t/requirements-and-discussion-of-a-type-dispatcher-for-the-ecosystem/157)
