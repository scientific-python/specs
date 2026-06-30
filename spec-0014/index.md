---
title: "SPEC 14 — Interactive Documentation"
shortcutDepth: 3
number: 14
date: 2025-05-07
author:
  - "Agriya Khetarpal <agriyakhetarpal@outlook.com>"
  - "Albert Steppi <albert.steppi@gmail.com>"
  - "Matthias Bussionnier <bussonniermatthias@gmail.com>"
  - "Melissa Weber Mendonça <melissawm@gmail.com>"
  - "Ralf Gommers <ralf.gommers@gmail.com>"
is-draft: true
discussion: https://discuss.scientific-python.org/t/spec-14-interactive-documentation/1910
endorsed-by:
  # TODO: ask for formal approval from projects that have adopted interactive docs during/after SPEC review/merging.
  - scikit-learn
  - scipy
  - numpy
---

## Description

A common barrier for beginners trying to get started with Scientific Python projects is their difficulty of installation. Even for experienced Python programmers, it can take a nontrivial amount of time to install an unfamiliar package correctly.

In-browser interactive documentation offers users a chance to try out and explore projects without taking the effort to install them locally. Even when users can install projects, interactive documentation provides a smoother experience than copying and pasting code snippets into a local REPL, IDE/editor or Notebook. It can thus offer benefits for beginners and more experienced programmers alike.

The [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/) project enables running Python code in the browser via [WebAssembly](https://webassembly.org/), such as code snippets in API examples, and/or narrative (long-form) documentation such as notebooks, tutorials, and how-to guides.

This SPEC offers a primer on how Core Projects in the Scientific Python ecosystem can make their documentation interactive through JupyterLite, together with a WebAssembly-based Python runtime provided by the [Pyodide](https://pyodide.org/en/stable/) or the [emscripten-forge](https://emscripten-forge.org/) distributions. It primarily focuses on Sphinx-based, HTML documentation workflows for projects with a Python API; however, brief recommendations are also made for other ways of documentation tooling, such as MkDocs, MyST-JS, and Quarto.

---

{{< figure >}}

src = "./NumPy-interactive-example.png"
alt = "The image shows the NumPy documentation page for the numpy.hsplit function. At the top is the NumPy logo and navigation bar with links to the User Guide, API reference, and other documentation sections. The left sidebar contains a list of related NumPy array manipulation functions. The main content focuses on the numpy.hsplit function, which splits an array into multiple sub-arrays horizontally (column-wise). The function signature shows numpy.hsplit(ary, indices_or_sections). The documentation explains that hsplit is equivalent to split with axis=1, and for 1-D arrays, it splits at axis=0. Prominently featured here is a detailed interactive example showing how to use numpy.hsplit in a numpydoc-based Examples section. A blue 'Try it in your browser!' button above the code snippet and below the Examples heading that allows users to run the code in a JupyterLite kernel directly within the documentation page without leaving the site. The example demonstrates splitting a 4x4 array into two parts and how to use hsplit with specific indices."

caption = "A screenshot of an interactive example in the NumPy documentation. The blue button labeled 'Try it in your browser!' allows users to run the code in a JupyterLite kernel directly within the documentation page without leaving the site."

title = "An interactive example for the numpy.hsplit() function"

{{< /figure >}}

---

{{< figure >}}

src = "./NumPy-interactive-example-opened.png"
alt = "This image shows the interactive JupyterLite notebook that has been opened and executed after clicking the 'Try it in your browser!' button from the NumPy hsplit documentation. The notebook is running directly within the same documentation page in an iframe, allowing users to experiment with the function without leaving the documentation. The JupyterLite UI is visible with standard notebook controls (File, Edit, View, Run, Kernel, Settings, Help) at the top. Below that is a warning message in an orange box stating that 'NumPy's interactive examples are experimental and may not always work as expected, with high load times, especially on low-resource platforms, and the version of NumPy might not be in sync with the one you are browsing the documentation for. The notebook shows three executed code cells, demonstrating how numpy.hsplit works with different parameters. The first cell imports NumPy and creates a 4x4 array, the second cell applies hsplit(x, 2) to split the array into two equal parts, and the third cell shows hsplit(x, np.array([3, 6])) to split the array at specific column indices."

caption = "The interactive JupyterLite notebook that has been opened and executed after clicking the 'Try it in your browser!' button from the NumPy hsplit documentation. The notebook is running directly within the same documentation page in an iframe, allowing users to experiment with the function without leaving the documentation."
title = "Running the interactive example within the documentation page"

{{< /figure >}}

### Core Project Endorsement

Core projects endorsing this SPEC would mean that they:

1. enable interactivity within applicable sections of their documentation websites, such as
   - the API reference sections (e.g., for "Examples" sections for public API methods and classes)
   - narrative long-form content (tutorials, how-to guides, etc., that are usually written in the form of notebooks)
2. further encourage other Scientific Python projects to adopt similar interfaces to make their documentation websites interactive, and
3. take interactive documentation deployments into account when making decisions about the future of their documentation, and
4. consider the suggestions made in this SPEC when doing so, wholly or in part.

### Ecosystem Adoption

#### Badges

Projects can highlight their adoption of this SPEC by including a SPEC badge.

{{< spec_badge number="14" title="Interactive Documentation" >}}

To indicate adoption of multiple SPECS with one badge, see [this](../purpose-and-process/#badges).

## Implementation

### Assumptions

- The target project has a hosted documentation website served over static HTML, built with the Sphinx documentation framework.
- Compatibility:
  - For projects with compiled extensions: WebAssembly binaries for the target project and its dependencies are available with either the [Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html) or [emscripten-forge](https://emscripten-forge.org/) distributions, or can be made available with a reasonable amount of effort if not yet available.
  - For pure Python projects: their dependencies—if any—are [compatible with WebAssembly](#11-how-to-assess-compatibility-with-webassembly) and are [available with either Pyodide or emscripten-forge](#12-what-does-adding-support-for-webassembly-look-like).

### Recommendations

This SPEC document makes the following recommendations:

1. [Support the WebAssembly platform by adding a CI job](#1-support-the-webassembly-platform-by-adding-a-pyodide-ci-job)
   <br>
   1.1. [How to assess compatibility with WebAssembly](#11-how-to-assess-compatibility-with-webassembly)
   <br>
   1.2. [What does adding support for WebAssembly look like?](#12-what-does-adding-support-for-webassembly-look-like)
2. [Enabling WASM builds for use in interactive documentation](#2-enabling-wasm-builds-for-use-in-interactive-documentation)
3. [Enabling interactive documentation deployments](#3-enabling-interactive-documentation-deployments)
   <br>
   3.1. [Configuration](#31-configuration)

#### 1. Support the WebAssembly platform by adding a Pyodide CI job

{{< admonition note >}}
While this step is not required to enable interactive documentation deployments alone, it is recommended to ensure that projects work properly in the WebAssembly environments used for such deployments and to facilitate their maintenance. We recommend that both pure Python projects and those with compiled extensions do this.

{{< /admonition >}}

##### 1.1. How to assess compatibility with WebAssembly

Two major projects currently provide ports of CPython to a WebAssembly runtime through the Emscripten compiler toolchain: Pyodide and emscripten-forge. They are largely compatible with CPython similar to how it runs on a standard Linux machine, albeit with a few differences, limitations, and exceptions.

[Most Core Projects are already available in the Pyodide distribution](https://pyodide.org/en/stable/usage/packages-in-pyodide.html), thanks to the work collectively done by the Pyodide maintainers, the emscripten-forge team, and several external collaborators.

Consider the following when assessing compatibility with WebAssembly:

- The bitness is 32-bit, with 64-bit memory indices left for future iterations of the WebAssembly specification
- CPython is directly compiled to WASM, specifically, the `wasm32-unknown-emscripten` target triplet, and the Python virtual machine that runs Python programs itself runs inside browsers' WebAssembly virtual machine implementations. While the Emscripten compiler toolchain provides JavaScript glue code that integrates with web-based elements in browsers, POSIX standard compliance—while generally high—is implemented differently due to browsers' file system and memory sandboxing features.

This means that specific modules from the Python standard library are unavailable and have been removed, and there is a lack of support for the `threading` and `multiprocessing` modules. Projects relying on parallel programming functionality such as pthreads or OpenMP must adapt their code accordingly.

For more details, refer to [the Pyodide documentation on "Pyodide Python compatibility"](https://pyodide.org/en/stable/usage/wasm-constraints.html).

##### 1.2. What does adding support for WebAssembly look like?

First, Core Projects should check if they are already supported, as [many Scientific Python projects are now well-tested for usage and interoperability in a WebAssembly runtime provided by Pyodide and emscripten-forge](https://github.com/Quansight-Labs/czi-scientific-python-mgmt/issues/18).

Compatibility can be established by implementing a CI job that builds wheels for a project and runs the test suite with them in a WebAssembly environment provided by the Pyodide distribution: https://pyodide.org/en/stable/development/building-and-testing-packages.html.

We consider a project well-tested if there exists a CI job, which:

- builds the source code for the project:
  - for projects with compiled extensions: using the Emscripten compiler toolchain for the `wasm32-unknown-emscripten` target into Pyodide-tagged wheels,
  - for pure Python projects: building wheels through existing build frontends such as `pip` or `pypa/build`
- subsequently, runs the entire test suite or applicable portions with these wheels installed into a Pyodide virtual environment provided with `pyodide venv`

#### 2. Enabling WASM builds for use in interactive documentation

After establishing WebAssembly compatibility, the next step is to make binaries available through the appropriate pathways; i.e., through the Pyodide distribution or the emscripten-forge channel.

Pyodide provides an entire distribution of packages along with its runtime through the jsDelivr CDN as its package index. Packages are bundled as WebAssembly-tagged wheels, which can be installed with [`micropip`](https://github.com/pyodide/micropip/), Pyodide's in-browser package manager. Similarly, [the `emscripten-forge` channel](https://emscripten-forge.org/) also has a growing collection of packages that support the `wasm32-unknown-emscripten` target, often mirroring Pyodide in terms of the collection of the packages available and their versions. The distinction is that emscripten-forge uses `conda`-based packaging standards and file formats, while Pyodide builds on those for PyPI (designed around Python wheels).

We will discuss further the differences between the Pyodide and `emscripten-forge` distributions when we suggest how to choose between them later in this document.

For a project not yet available via Pyodide or emscripten-forge, once it and its dependencies are established as compatible with WebAssembly (as discussed above), it is relatively straightforward to add it to one or both of these distributions. The process is described in their respective documentation websites:

1. https://pyodide.org/en/stable/development/new-packages.html
2. https://emscripten-forge.org/development/adding_packages/

See ["Background and additional context"](#background-and-additional-context) for more details.

Additionally, during this process, this SPEC recommends that [project contacts](https://github.com/pyodide/pyodide/issues/4506) volunteer as recipe maintainers for the packages they are core developers and/or maintainers of, so that they can help with builds or testing issues that may occur when the Pyodide or emscripten-forge maintainers try to upgrade packages, or with usage issues that may arise when users try to use Pyodide or emscripten-forge.

#### 3. Enabling interactive documentation deployments

Once a project's WebAssembly binaries and dependencies are available through Pyodide and/or emscripten-forge, the project may start using them in interactive documentation deployments.

We recommend [the JupyterLite project](https://jupyterlite.readthedocs.io/en/stable/) due to its multiple features and surrounding tooling to ease such deployments.

JupyterLite is a serverless variant of the JupyterLab project that runs entirely in the browser on the client side via WebAssembly. JupyterLite sites are distributed as static assets and can be built using the `jupyter lite` CLI. It supports various JupyterLab extensions, plugins, kernels, and surrounding projects for browser-based use cases. Particularly, the project provides the following:

- [`jupyterlite-sphinx`](https://jupyterlite-sphinx.readthedocs.io/en/stable/): a Sphinx extension that provides mechanisms to embed a JupyterLite site within Sphinx documentation, and offers documentation-focused abstractions to customise them via a Pythonic interface.
- Two browser-based Python kernels, `jupyterlite-pyodide-kernel` and `jupyterlite-xeus`: these ship with support for the Pyodide and the emscripten-forge distributions, respectively, and need to be installed alongside `jupyterlite-sphinx`. Documentation website owners may choose between the two kernels, with the differences between them noted as a part of the JupyterLite documentation: https://jupyterlite.readthedocs.io/en/stable/howto/configure/kernels.html#adding-a-python-kernel

We recommend installing and configuring `jupyterlite-sphinx` and one of the two kernels within Core Projects’ Sphinx-based documentation workflows in order to build a JupyterLite deployment and interact with it through Sphinx.

##### 3.1. Configuration

Next, we discuss configuring JupyterLite, jupyterlite-sphinx, and the installed kernel(s) of choice together.

We have observed that documentation for Scientific Python projects typically comes in two forms:

- API reference documentation, and
- narrative long-form content

For both of these, we recommend different approaches to enable interactivity:

###### API documentation

`jupyterlite-sphinx` offers the [`try_examples` directive](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html), which can make "Examples" sections within API documentation interactive. This directive adds buttons which swap the rendered code snippets in place with an interactive mini-notebook that can be executed without leaving the page. There is an option to have the directives inserted into "Examples" sections automatically for documentation that uses [numpydoc](https://numpydoc.readthedocs.io/), and with [`sphinx.ext.napoleon`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) supported on a best-effort basis. The look, shape, feel, text, and inclusion of these buttons across the documentation can be configured through user-defined options.

###### Narrative documentation and tutorials (long-form content)

For longer-form narrative content such as tutorials, how-to guides, and explanatory documentation:

- `jupyterlite-sphinx` offers directives to render long-form content written in notebooks (the [`jupyterlite` directive](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/jupyterlite.html), the [`notebooklite` directive](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/notebooklite.html), and so on), which can be configured to open notebooks in new tabs or iframes within the same tab. It supports both traditional IPyNB files and [MyST Markdown notebooks](https://myst-nb.readthedocs.io/en/stable/authoring/text-notebooks.html). Unlike the `try_examples` directive, these directives do not work with reST-based content. We recommend using MyST Markdown notebooks, as they integrate well with version control.
- The Sphinx-Gallery project offers a [JupyterLite integration, built with `jupyterlite-sphinx`](https://sphinx-gallery.github.io/stable/configuration.html#jupyterlite) which enables a "JupyterLite" button in the secondary sidebar to open a notebook in the JupyterLite deployments. It provides a `notebook_modification_function` configuration option via `conf.py` that can be used to configure code cells or Markdown cells at the top of a notebook, with custom `%pip`-install commands, imports from other libraries, or extra admonitions.

---

Once interactive documentation has been configured and deployed, the ["Updating package and kernel versions for Pyodide-powered or emscripten-forge-powered websites"](#updating-package-and-kernel-versions-for-pyodide-powered-or-emscripten-forge-powered-websites) section contains information on how to increment the packages' and distribution/kernel's versions.

An end-to-end example of the above steps is also available; see [the `jupyterlite-sphinx-demo` project](#an-end-to-end-example).

#### What distribution should projects choose: Pyodide or emscripten-forge?

To help projects make an informed decision between the Pyodide and emscripten-forge distributions, we provide a comparison of their key features below that are relevant to interactive documentation deployments:

| Feature                                            | Pyodide                                                                          | emscripten-forge                                                                                                                     |
| -------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Package format**                                 | Python wheels                                                                    | conda packages                                                                                                                       |
| **ABI compatibility**                              | Uses specific Emscripten version and is updated often                            | Uses a different Emscripten version and is updated less often                                                                        |
| **Kernel used in JupyterLite**                     | `jupyterlite-pyodide-kernel`                                                     | Xeus loader for the `xeus-python` kernel                                                                                             |
| **Dynamically installing packages in the browser** | Yes, via `%pip install` magics with `piplite`/`micropip`                         | Not currently available (an in-browser package manager [`picomamba`](https://github.com/mamba-org/picomamba) may soon address this). |
| **Pre-installation**                               | Individual packages can be pre-specified but have to be installed in the browser | Uses an environment file to pre-install packages into the web environment                                                            |
| **Programming language support**                   | Python only                                                                      | Multiple languages via Xeus kernels                                                                                                  |
| **Package update frequency**                       | Packages are tied to Pyodide releases (changing in v0.28+)                       | More frequent updates                                                                                                                |

The Pyodide distribution may be chosen if:

- the project is already available in the Pyodide distribution
- installing packages during runtime is required, say, for interactive examples that rely on data files or other packages (see ["Resolving common issues with web requests in the browser"](#resolving-common-issues-with-web-requests-in-the-browser) below)

The emscripten-forge distribution may be chosen if:

- support for programming languages beyond Python or projects not available in Pyodide is required
- more frequent updates than Pyodide release cycles are required (see ["The lack of synchronisation between a Core Project’s documentation version and the version of the available binaries (Pyodide kernel only)"](#the-lack-of-synchronisation-between-a-core-projects-documentation-version-and-the-version-of-the-available-binaries-pyodide-kernel-only) below)
- one needs more control over the pre-installed environment

See [the JupyterLite documentation on "Adding a Python kernel"](https://jupyterlite.readthedocs.io/en/stable/howto/configure/kernels.html#adding-a-python-kernel) for more.

### Runtime considerations

During the process, we must discuss common aspects and scenarios that should be considered when enabling interactive documentation deployments.

#### WebAssembly computation is serverless and runs in the browser

- As Pyodide and emscripten-forge are based on WebAssembly, all computation happens entirely in the users' browsers without any server-side processing required or any user data being shared with any third party. This serverless approach means minimal maintenance costs for documentation maintainers – once deployed, the interactive documentation can be hosted purely as static files.
- Core Projects will not need to provision, maintain, or manage external servers to handle users’ computation requests. This is inherently more scalable than a central hub with server-side computation like Binder.

#### Bandwidth usage and browser limitations

[Pyodide currently requires a 6.4 MiB download and a few seconds of loading time, with additional overhead from the Pyodide kernel](https://pyodide.org/en/stable/project/roadmap.html#reducing-download-sizes-and-initialization-times). Scientific Python projects—especially ones containing large amounts of compiled code—can be substantial in size: a typical environment including NumPy, SciPy, and pandas can require approximately 80 MiB of bandwidth. This renders interactive documentation utilities unsuitable for low-resource platforms, like mobile or tablet devices or for viewers without a stable internet connection. Taking note of this, `jupyterlite-sphinx` currently disables the examples completely for such platforms.

JupyterLite is also best supported on more conventional platforms and browser configurations:

- For example, iOS's WASM runtime is not well supported upstream and unexpected problems may occur.
- Firefox in incognito mode does not have proper support for accessing the Emscripten file system, because service workers, which JupyterLite uses, are not supported.

First-time visitors may experience a longer loading time, as large resources such as WASM wheels and other static assets are fetched. However, browsers will cache downloaded wheels, substantially reducing bandwidth requirements for JupyterLite and subsequent loading times for interactive examples.

#### The lack of synchronisation between a Core Project’s documentation version and the version of the available binaries (Pyodide kernel only)

At the moment, Pyodide version 0.27 (and previous versions) as an entire distribution bundles the versions of the packages available within it, along with the Pyodide runtime.

This creates a problem for documentation website maintainers, as they will want to use up-to-date wheels for their interactive documentation deployments, but those wheels might not be available as part of Pyodide. This means that users may experience a mismatch: the interactive example runs version $x$, whereas the documentation is for a different version $y$. This lack of synchronisation can show up in the following scenarios:

- when a user browses the documentation for a stable version of a project, and the project's WebAssembly wheels have not been updated to match that version
- when a user browses the documentation for a hosted "latest" or "dev" version, for which WebAssembly wheels may not be available yet
- when working on the documentation and serving it locally

The best way to address point (1) is to upgrade to as recent a version of Pyodide available via `jupyterlite-pyodide-kernel` as possible, and upgrade the version of the relevant Core Project(s), or assist the Pyodide maintainers in doing so, so that Pyodide releases can include as up-to-date package versions as possible.

To address point (2), nightly Pyodide wheels for various packages are now being uploaded on [the Scientific Python Nightly Wheels channel on Anaconda.org](https://anaconda.org/scientific-python-nightly-wheels). They can be installed with [`piplite`](https://jupyterlite.readthedocs.io/en/stable/howto/pyodide/packages.html#installing-packages-at-runtime). See ["SPEC 4 — Using and Creating Nightly Wheels"](../spec-0004/) for more.

It is also possible to bundle a wheel as a part of the documentation build process in CI; see https://github.com/scikit-image/scikit-image/pull/7644 for an example which configures the Pyodide kernel to load an extra wheel and add it to a local index that is available for Pyodide to install.

The emscripten-forge distribution does not have this limitation. Still, packages there need to be continually updated, supported, and patched in the same way they need to be for inclusion in Pyodide. This is planning to change with the upcoming [Pyodide version 0.28](https://github.com/pyodide/pyodide/issues/4918), allowing the distribution of Pyodide’s packages outside of Pyodide's releases.

### The maintenance of interactive documentation utilities

After interactive documentation deployments are rolled out, common maintenance patterns include:

- hosting them on an experimental and best-effort basis, built for quick prototyping and pedagogical use cases for beginners and intermediate users, and
- handling issues concerning these rollouts only for the "stable" and "development" versions of the documentation.

The maintenance of these deployments has a couple of aspects, which we cover below:

##### Disabling interactive buttons where interactivity isn't useful or not desired, or where the code is not compatible with WebAssembly

If there are areas in the public API documentation for a project for which interactive examples are not useful for inclusion (or are supposed to be hidden to end users as far as interactivity is concerned), they may be hidden at runtime using [a `try_examples.json` configuration file](https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html#try-examples-json-configuration-file), which will exclude them from being rendered interactive using a regular expression pattern.

##### Updating package and kernel versions for Pyodide-powered or emscripten-forge-powered websites

- Attempts are made for packages to update to the latest versions at the time of an Emscripten version bump and when a new release for Pyodide is about to be released. Breakages in builds and/or tests for packages are rare but inevitable, and some packages need to be disabled, where recipe maintainers, with their understanding of the packages' internals, will have the ability to help debug issues in collaboration with the Pyodide maintainers to resolve them. The same process follows with the emscripten-forge distribution.
- The best way to ensure that interactive documentation websites for projects remain up to date is to use pinned versions of `jupyterlite-core`, and `jupyterlite-pyodide-kernel` (which controls the Pyodide version used), update them periodically, and add corresponding updates to packages' recipes in Pyodide and emscripten-forge as applicable to keep them up to date. This is a manual process for Pyodide, and is automated for emscripten-forge.

#### Resolving common issues with web requests in the browser

While HTTP libraries such as `httpx`, `requests`, and so on have gained compatibility with Pyodide, it is still necessary to use [`pyodide-http`](https://github.com/koenvo/pyodide-http) to patch them for usage inside JupyterLite, or add code paths that use [Pyodide-specific networking capabilities](https://pyodide.org/en/stable/usage/api/python-api/http.html).

Data files, if present in the repository or in an external source that are later downloaded by `pooch` or similar tools as a means for usage in test suites or as a part of a "fetcher"-like public API attribute, may not work by default due to [CORS restrictions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) enforced by web browsers.

In particular, the following points apply:

- CORS headers are present if data files are hosted on raw GitHub URLs.
- If they are hosted on GitHub Releases, CORS headers are absent.
- If they are hosted on GitLab, [CORS headers are absent](https://gitlab.com/gitlab-org/gitlab/-/issues/16732).

In this case, we recommend wrapping URLs to files within data registries with a CDN that acts as a CORS proxy server and adds CORS headers over such URLs. [Statically](https://statically.io/) and [GitHack](https://raw.githack.com/) are both reasonable free options with no limits on traffic, and they add CORS headers to the files they serve.

For example, a URL like `https://raw.githubusercontent.com/scikit-image/scikit-image/main/skimage/data/chelsea.png` may be wrapped with Statically as `https://cdn.statically.io/gh/scikit-image/scikit-image/main/skimage/data/chelsea.png`.

## Background and additional context

Emscripten, unlike glibc, does not provide a backwards-compatible ABI. There has been a recent effort to standardise support for it through a `manylinux`-like standard as a means towards uploading to PyPI through [PEP 776 – Emscripten Support](https://peps.python.org/pep-0776/) (see also, previous discussion at https://github.com/pypi/warehouse/issues/10416). Emscripten has been a Tier III target platform for CPython (it was restored with the upcoming Python version 3.14). However, the lack of standardisation of a Pyodide ABI means that every package has to be rebuilt with newer versions of Emscripten with each corresponding update in Pyodide or emscripten-forge. This goal is in progress at https://github.com/pyodide/pyodide/issues/5580 and [PEP 783 – Emscripten Packaging](https://peps.python.org/pep-0783/).

Usually, it is recommended to reach out to the Pyodide maintainers to see if it is necessary to include a package in Pyodide and attempt to add "explicit" support for it, especially with pure Python packages, as most of them work out of the box unless they support niche use cases or interact with components of the Python runtime or standard library that are not supported well (see ["How to assess compatibility with WebAssembly"](#11-how-to-assess-compatibility-with-webassembly) for more). As Scientific Python projects are numerical in nature, they have usually worked well with or without patches by collaborators in the Pyodide/WASM ecosystem and with support from the recipe maintainers.

## Suggestions on other documentation tooling

While this SPEC provides recommendations on integration with Sphinx, we also offer brief suggestions for other documentation development tooling as well:

1. [MkDocs](https://www.mkdocs.org/) does not have a JupyterLite plugin that provides functionality equivalent to `jupyterlite-sphinx` at the time of writing. However, there are some ways through which interactive documentation deployments can be somewhat achieved:
   - Projects like https://github.com/samuelcolvin/mkdocs-run-code, https://github.com/JeffersGlass/mkdocs-pyscript, and https://gitlab.com/frederic-zinelli/pyodide-mkdocs-theme provide integrations to embed interactive components.
   - As a JupyterLite site contains static assets and HTML files, it can be bundled and served alongside an MkDocs-based documentation website, with both separate from each other.
2. [The MyST-JS project](https://js.mystmd.org/) also provides configuration to integrate with Pyodide and JupyterLite: https://mystmd.org/guide/integrating-jupyter#id-case-using-pyodide-jupyterlite
3. [The Quarto technical publishing system](https://quarto.org/) provides [Quarto Live](https://r-wasm.github.io/quarto-live/), which enables interactive code blocks for Quarto documents via the webR and Pyodide runtimes to run R and Python code in the browser.

## Acknowledgements

Work on investigating best practices for interactive documentation for Scientific Python projects, improving tooling for interactive documentation, and developing and documenting workflows was supported by the [CZI grant 2022-316713](https://blog.scientific-python.org/scientific-python/2022-czi-grant/).

## Notes

### An end-to-end example

For an end-to-end example on how to set up interactive documentation with JupyterLite, see [the `jupyterlite/sphinx-demo` repository](https://github.com/jupyterlite/sphinx-demo).

### Interactive documentation efforts

For further reference, here are some efforts towards enabling interactive documentation deployments for Scientific Python projects:

- https://github.com/scipy/scipy/pull/20303
- https://github.com/scipy/scipy/issues/19729 and https://github.com/scipy/scipy/pull/20019
- https://github.com/numpy/numpy/pull/26745
- https://github.com/sympy/sympy/pull/27419
- https://github.com/scikit-image/scikit-image/pull/7644

### Utilities

These are commonly used utilities and projects that are provided by the JupyterLite ecosystem:

- https://jupyterlite-sphinx.readthedocs.io/en/stable/
- https://jupyterlite-pyodide-kernel.readthedocs.io/en/stable/
- https://jupyterlite-xeus.readthedocs.io/en/stable/
- https://jupyterlite.readthedocs.io/en/stable/

### Interactive documentation runtime drivers

These include Pyodide and emscripten-forge, which are the two main drivers for interactive documentation deployments:

- https://pyodide.org/en/stable/usage/packages-in-pyodide.html
- https://emscripten-forge.org/

The Xeus project is a Jupyter kernel for C++ and other languages. JupyterLite can use it to run code for various languages in the browser. It is also used by JupyterLab and other Jupyter projects. The Xeus project is part of the Jupyter ecosystem and provides a C++ implementation of the Jupyter kernel protocol.

- https://github.com/jupyterlite/xeus
- https://github.com/jupyterlite/xeus-lite-demo

### Sphinx extensions

- https://jupyterlite-sphinx.readthedocs.io/en/stable/directives/try_examples.html
- https://sphinx-gallery.github.io/stable/configuration.html#jupyterlite

### Ancillary documentation and resources on how to maintain interactive documentation deployments

The SciPy documentation has dedicated sections on how to maintain interactive documentation deployments, which is worth checking out:

- https://github.com/scipy/scipy/pull/22385
- https://scipy.github.io/devdocs/dev/core-dev/index.html#interactive-examples-in-docstrings
- https://scipy.github.io/devdocs/dev/contributor/adding_notebooks.html

### Miscellaneous additional context

There have been discussions regarding Pyodide as an officially supported platform for `scikit-learn`:

- https://github.com/scikit-learn/scikit-learn/issues/23727

[`pypa/cibuildwheel`](https://cibuildwheel.pypa.io), since version 2.19 has supported building Pyodide wheels:

- https://iscinumpy.dev/post/cibuildwheel-2-19-0/
