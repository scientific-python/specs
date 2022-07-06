---
title: "SPEC 1 — Lazy Loading for Submodules"
date: 2020-12-17
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jon Crall <jon.crall@kitware.com>"
  - "Dan Schult <dschult@colgate.edu>"
discussion: https://discuss.scientific-python.org/t/spec-1-lazy-loading-for-submodules/25
endorsed-by:
---

## Description

Early on, most scientific Python packages explicitly imported their submodules.
For example, you would be able to do:

```python
import scipy as sp

sp.linalg.eig(...)
```

This was convenient: it had the simplicity of a flat namespace, but with the organization of a nested one.
However, there was one drawback: importing submodules, especially large ones, introduced unacceptable slowdowns.

For a while, SciPy had a lazy loading mechanism called `PackageLoader`.
It was eventually dropped, because it failed frequently and in confusing ways—especially when used with interactive prompts.

Thereafter, most libraries stopped importing submodules and relied on documentation to tell users which submodules to import.

Commonly, code now reads:

```python
from scipy import linalg
linalg.eig(...)
```

Since the `linalg` submodule often conflicts with similar instances in other libraries, users also write:

```python
# Invent an arbitrary name for each submodule
import scipy.linalg as sla
sla.eig(...)
```

or

```python
# Import individual functions, making it harder to know where they are from
# later on in code.
from scipy.linalg import eig
eig(...)
```

This SPEC proposes a lazy loading mechanism—targeted at libraries—that avoids import slowdowns and brings back explicit submodule exports, but without slowing down imports.

For example, it allows the following behavior:

```python
import skimage as ski  # cheap operation; does not load submodules

ski.filters  # cheap operation; loads the filters submodule, but not
             # any of its submodules or functions

ski.filters.gaussian(...)  # loads the file in which gaussian is implemented
                           # and calls that function

```

This has several advantages:

1. It exposes a **nested namespace that behaves as a flat namespace**.
   This avoids carefully having to import exactly the right combination of submodules, and allows interactive exploration of the namespace in an interactive terminal.

2. It **avoids having to optimize for import cost**.
   Currently, developers often move imports inside of functions to avoid slowing down importing their module.
   Lazy importing makes imports at any depth in the hierarchy cheap.

3. It provides **direct access to submodules**, avoiding local namespace conflicts.
   Instead of doing `import scipy.linalg as sla` to avoid clobbering a local `linalg`, one can now assign a short name to each library and access its members directly: `import scipy as sp; sp.linalg`.

### Usage

Python 3.7, with [PEP 562](https://www.python.org/dev/peps/pep-0562/), introduces the ability to override module `__getattr__` and `__dir__`.
In combination, these features make it possible to again provide access to submodules, but without incurring performance penalties.

We propose a [utility library](https://pypi.org/project/lazy_loader/) for easily setting up so-called "lazy imports" so that submodules are only loaded upon accessing them.

As an example, we will show how to set up lazy importing for `skimage.filters`.
In the library's main `__init__.py`, specify which submodules are lazily loaded:

```python
import lazy_loader as lazy

submodules = [
    ...
    'filters',
    ...
]

__getattr__, __dir__, _ = lazy.attach(__name__, submodules)
```

Then, in each submodule's `__init__.py` (in this case, `filters/__init__.py`), specify which functions are to be loaded from where:

```python
import lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach(
    __name__,
    submodules=['rank']
    submod_attrs={
        '_gaussian': ['gaussian', 'difference_of_gaussians'],
        'edges': ['sobel', 'sobel_h', 'sobel_v',
                  'scharr', 'scharr_h', 'scharr_v',
                  'prewitt', 'prewitt_h', 'prewitt_v',
                  'roberts', 'roberts_pos_diag', 'roberts_neg_diag',
                  'laplace',
                  'farid', 'farid_h', 'farid_v']
    }
)
```

The above would be equivalent to:

```python
from . import rank
from ._gaussian import gaussian, difference_of_gaussians
from .edges import (sobel, sobel_h, sobel_v,
                    scharr, scharr_h, scharr_v,
                    prewitt, prewitt_h, prewitt_v,
                    roberts, roberts_pos_diag, roberts_neg_diag,
                    laplace,
                    farid, farid_h, farid_v)
```

The difference being that the submodule is loaded only once it is accessed:

```python
import skimage
dir(skimage.filters)  # This works as usual
```

Furthermore, the functions inside of the submodule are loaded only
once they are needed:

```python
import skimage

skimage.filters.gaussian(...)  # Lazy load `gaussian` from
                               # `skimage.filters._gaussian`

skimage.filters.rank.mean_bilateral(...)  # Loaded once `rank` is accessed
```

One disadvantage is that erroneous or missing imports no longer fail immediately.
During development and testing, the `EAGER_IMPORT` environment variable can be set to disable lazy loading, so that errors like these can be spotted.

#### External libraries

The `lazy_loader.attach` function is an alternative to setting up package internal imports.
We also provide `lazy_loader.load` so that projects can lazily import external libraries:

```python
linalg = lazy.load('scipy.linalg')  # `linalg` will only be loaded when accessed
```

By default, import errors are postponed until usage. Import errors can
be immediately raised with:

```python
linalg = lazy.load('scipy.linalg', error_on_import=True)
```

## Implementation

Lazy loading is implemented at
https://github.com/scientific-python/lazy_loader and is
pip-installable as
[lazy_loader](https://pypi.org/project/lazy_loader/).

Once a lazy import interface is implemented, other interesting options
become available (but is not implemented in `lazy_loader`).
For example, instead of specifying sub-submodules and functions the way we do above, one could do this in YAML files:

```
$ cat skimage/filters/init.yaml

submodules:
- rank

functions:
- _gaussian:
  - gaussian
  - difference_of_gaussians
- edges:
  - sobel
  - sobel_h
  - sobel_v
  - scharr

...
```

Ultimately, we hope that lazy importing will become part of Python itself, but the developers have indicated that this is highly unlikely [^cannon].
In the mean time, we now have the necessary mechanisms to implement it ourselves.

[^cannon]: Cannon B., personal communication, 7 January 2021.

### Caveats

While this pattern has benefits at runtime, it does have one specific drawback:

Static type checkers (such as [mypy](http://mypy-lang.org) and
[pyright](https://github.com/microsoft/pyright)) will not be able to infer the
types and locations dynamically-loaded modules and functions. This means that some
integrated development environments (e.g.
[VS Code](https://code.visualstudio.com)) will not be able to provide code
completion, parameter hints, documentation, or other features for any objects in your module.

You can direct static type checkers to the actual location of dynamically loaded objects in one of two ways:

1. Use an [`if
   typing.TYPE_CHECKING`](https://docs.python.org/3/library/typing.html#typing.TYPE_CHECKING)
   clause .

   ```python
    from typing import TYPE_CHECKING

    import lazy_loader as lazy

    if TYPE_CHECKING:
        from .edges import sobel, sobel_h, sobel_v

    __getattr__, __dir__, __all__ = lazy.attach(
        __name__,
        submod_attrs={
            'edges': ['sobel', 'sobel_h', 'sobel_v']
        }
    )
    ```

    `typing.TYPE_CHECKING` is a special variable that is set to `False` at runtime, and has negative runtime impact. 

2. Use a [type stub (`.pyi`) file](https://mypy.readthedocs.io/en/stable/stubs.html). Type stubs are ignored at runtime, but used
by static type checkers. This method entails adding a new file with a `.pyi` extension in the same directory as your actual `.py`. For example:

    ```python
    # mypackage/__init__.py
    import lazy_loader as lazy

    __getattr__, __dir__, __all__ = lazy.attach(
        __name__,
        submod_attrs={
            'edges': ['sobel', 'sobel_h', 'sobel_v']
        }
    )
    ```

    ```python
    # mypackage/__init__.pyi
    from .edges import sobel, sobel_h, sobel_v
    ```

    Note that if you use a type stub, you will need to take additional action to add the `.pyi` file to your sdist and wheel distributions.  See [PEP 561](https://peps.python.org/pep-0561/) and the [mypy documentation](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages) for more information.

    It is also sometimes harder to keep `.pyi` in sync with `.py` files, as they more often go unnoticed by contributors.

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

Lazy loading has been adopted by
[scikit-image](https://github.com/scikit-image/scikit-image/pull/5101)
and [NetworkX](https://github.com/networkx/networkx/pull/4909).
SciPy implements a [subset of lazy
loading](https://github.com/scipy/scipy/pull/15230) which exposes only
subpackages lazily.
A prototype implementation of `lazy_loader` was adapted for
[napari](https://github.com/napari/napari/pull/2816).

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

- The [lazy loading blog post by Brett Cannon](https://snarky.ca/lazy-importing-in-python-3-7/) showed the feasibility of the concept, and informed our design.

- Technical improvements happened around the [scikit-image PR](https://github.com/scikit-image/scikit-image/pull/5101)

- [mkinit](https://github.com/Erotemic/mkinit) is a tool that automates the generation of `__init__.py` files, and supports this lazy loading mechanism.
  See, e.g., [NetworkX PR #4496](https://github.com/networkx/networkx/pull/4496).

- The lazy loading discussion was initiated in [NetworkX PR #4401](https://github.com/networkx/networkx/pull/4401).
