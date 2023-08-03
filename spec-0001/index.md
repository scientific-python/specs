---
title: "SPEC 1 — Lazy Loading of Submodules and Functions"
date: 2020-12-17
author:
  - "Stéfan van der Walt <stefanv@berkeley.edu>"
  - "Jon Crall <jon.crall@kitware.com>"
  - "Dan Schult <dschult@colgate.edu>"
discussion: https://discuss.scientific-python.org/t/spec-1-lazy-loading-for-submodules/25
endorsed-by:
  - networkx
  - scikit-image
  - scipy
shortcutDepth: 3
---

## Description

This SPEC recommends a lazy loading mechanism—targeted at libraries—that avoids import slowdowns
and provides explicit submodule exports.

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
   Lazy importing, when implemented through out a library, makes all imports cheap.

3. It provides **direct access to submodules**, avoiding local namespace conflicts.
   Instead of doing `import scipy.linalg as sla` to avoid clobbering a local `linalg`, one can now import each library and access its members directly: `import scipy; scipy.linalg`.

### Core Project Endorsement

Endorsing this SPEC means agreeing, in principle, with the advantages of lazy loading described above.

### Ecosystem Adoption

Adopting this SPEC means implementing, using the `lazy_loader` package or any other mechanism (such as module `__getattr__`), lazy loading of subpackages and, if desired, subpackage attributes.

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

## Implementation

### Background

Early on, most scientific Python packages explicitly imported their submodules.
For example, you would be able to do:

```python
import scipy

scipy.linalg.eig(...)
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

Python 3.7, with [PEP 562](https://www.python.org/dev/peps/pep-0562/), introduces the ability to override module `__getattr__` and `__dir__`.
In combination, these features make it possible to again provide access to submodules, but without incurring performance penalties.

### `lazy_loader`

To make it easier for projects to implement lazy loading of submodules and functions, we provide a utility
library, called `lazy_loader`. It is implemented at
https://github.com/scientific-python/lazy_loader and is
installable from [pypi](https://pypi.org/project/lazy_loader/) and [conda-forge](https://anaconda.org/conda-forge/lazy_loader).

#### Usage

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

#### Type checkers

The lazy loading shown above has one drawback: static type checkers
(such as [mypy](http://mypy-lang.org) and
[pyright](https://github.com/microsoft/pyright)) will not be able to
infer the types of lazy-loaded modules and functions.
Therefore, `mypy` won't be able to detect potential errors, and
integrated development environments such as [VS
Code](https://code.visualstudio.com) won't provide code completion.

To work around this limitation, we provide an alternative way to define lazy
imports.
Instead of importing modules and functions in `__init__.py`
file with `lazy.attach`, you instead specify those imports in a `__init__.pyi`
file—called a "type stub".
Your `__init__.py` file then loads imports from the stub using `lazy.attach_stub`.

Here's an example of how to convert this `__init__.py`:

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

Add a [type stub (`__init__.pyi`) file](https://mypy.readthedocs.io/en/stable/stubs.html) in the same directory as the `__init__.py`.
Type stubs are ignored at runtime, but used by static type checkers.

```python
# mypackage/__init__.pyi
from .edges import sobel as sobel, sobel_h as sobel_h, sobel_v as sobel_v
```

The explicit import naming `sobel as sobel` is [necessary due to PEP 484](https://github.com/microsoft/pyright/issues/3989#issuecomment-1260194688).
Alternatively, you can manually provide an `__all__`:

```python
# mypackage/__init__.pyi
__all__ = ['sobel', 'sobel_h', 'sobel_v']
from .edges import sobel, sobel_h, sobel_v
```

Replace `lazy.attach` in `mypackage/__init__.py` with a call to `attach_stub`:

```python
import lazy_loader as lazy

# this assumes there is a `.pyi` file adjacent to this module
__getattr__, __dir__, __all__ = lazy.attach_stub(__name__, __file__)
```

_Note that if you use a type stub, you will need to take additional action to add the `.pyi` file to your sdist and wheel distributions.
See [PEP 561](https://peps.python.org/pep-0561/) and the [mypy documentation](https://mypy.readthedocs.io/en/stable/installed_packages.html#creating-pep-561-compatible-packages) for more information._

#### Caveats

Thus far, we are aware of one corner case in which lazy loading does not work.
This is when you define a lazily loaded function, say `my_func`, in a file of the same name (`my_func.py`) **AND** run doctests.
Somehow, the doctest collector modifies the parent module's `__dict__` to include `my_func` (the module, not the function), essentially short circuiting the lazy loader and its ability to provide `my_module.my_func` (the function).
Fortunately, there is an easy way to address this that already aligns with common practice: define `my_func` inside `_my_func.py` instead (note the underscore).

#### YAML files

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

## Notes

- The [lazy loading blog post by Brett Cannon](https://snarky.ca/lazy-importing-in-python-3-7/) showed the feasibility of the concept, and informed our design.

- Technical improvements happened around the [scikit-image PR](https://github.com/scikit-image/scikit-image/pull/5101)

- [mkinit](https://github.com/Erotemic/mkinit) is a tool that automates the generation of `__init__.py` files, and supports this lazy loading mechanism.
  See, e.g., [NetworkX PR #4496](https://github.com/networkx/networkx/pull/4496).

- The lazy loading discussion was initiated in [NetworkX PR #4401](https://github.com/networkx/networkx/pull/4401).
