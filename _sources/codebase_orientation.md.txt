# General Codebase Orientation

The [spyder-ide/spyder](https://github.com/spyder-ide/spyder) repository contains
code for many plugins that are versioned and published into a single package.

See the [Contributing Guidelines]() for detailed developer installation instructions.

## Directories

The repository contains a number of top-level directories, the contents of which
are described here.

### Binder setup: ``binder/``

This contains an environment specification for ``repo2docker`` which allows
the repository to be tested on [mybinder.org](https://mybinder.org>)

This specification is developer focused.

### external-deps

### img_src

### requirements

### rope_profiling

### scripts

### Python package: ``spyder/``

This, along with the ``setup.py``, comprises the Python code for the project.
This includes the notebook server extension, JupyterLab's command line interface,
entrypoints, and Python tests.

It also contains the final built JavaScript assets which are distributed with
the Python package.
