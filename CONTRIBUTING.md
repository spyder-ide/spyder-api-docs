# Contributing to Spyder-Infra

First off, thanks for your interest in helping out with Spyder-Infra!

**Important Note:** This is the repository for the Spyder-Infra project—not the Spyder IDE itself.
For more information about Spyder, please see the [website](https://www.spyder-ide.org/), and for the core Spyder codebase, visit the [main repo](https://github.com/spyder-ide/spyder).

Spyder-Infra is part of the Spyder IDE GitHub organization, and is developed with standard GitHub flow.
If you're not comfortable with at least the basics of ``git`` and GitHub, we recommend reading beginner tutorials such as [GitHub's Git Guide](https://github.com/git-guides/), its [introduction to basic Git commands](https://docs.github.com/en/get-started/using-git/about-git#basic-git) and its [guide to the fork workflow](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project).
However, this contributing guide should fill you in on most of the basics you need to know.

Let us know if you have any further questions, and we look forward to your contributions!


<!-- markdownlint-disable -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Reporting Issues](#reporting-issues)
- [Cloning the Repository](#cloning-the-repository)
- [Setting Up a Development Environment with Nox (Recommended)](#setting-up-a-development-environment-with-nox-recommended)
- [Setting Up a Development Environment Manually](#setting-up-a-development-environment-manually)
  - [Create and activate a fresh environment](#create-and-activate-a-fresh-environment)
  - [Install dependencies](#install-dependencies)
  - [Add the upstream remote](#add-the-upstream-remote)
- [Installing and Using the Pre-Commit Hooks](#installing-and-using-the-pre-commit-hooks)
- [Building the Project](#building-the-project)
  - [Build with Nox](#build-with-nox)
  - [Build manually](#build-manually)
- [Contributing Changes](#contributing-changes)
  - [Decide which branch to use](#decide-which-branch-to-use)
  - [Prepare your topic branch](#prepare-your-topic-branch)
  - [Commit your changes](#commit-your-changes)
  - [Push your branch](#push-your-branch)
  - [Submit a Pull Request](#submit-a-pull-request)
- [Standards and Conventions](#standards-and-conventions)
  - [Key standards](#key-standards)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- markdownlint-restore -->



## Reporting Issues

Find an issue with Spyder-Infra?
Please [open](https://github.com/spyder-ide/spyder-infra/issues/new/choose) an [issue](https://github.com/spyder-ide/spyder-infra/issues) documenting the bug, enhancement or new content following the guidance in our issue template.

If referring to a specific line or file, please be sure to provide a snippet of context and/or the file and line number to allow us to find and fix it, and if pointing out a problem, please be as specific as you can in suggesting a revised wording that would solve it.



## Cloning the Repository

First, navigate to the [project repository](https://github.com/spyder-ide/spyder-infra) in your web browser and press the ``Fork`` button to make a personal copy of the repository on your own GitHub account.
Then, click the ``Clone or Download`` button on your repository, copy the link and run the following on the command line to clone the repo:

```shell
git clone <LINK-TO-YOUR-REPO>
```

After cloning the repository, navigate to its new directory using the `cd` command:

```shell
cd spyder-infra
```



## Setting Up a Development Environment with Nox (Recommended)

Our [Nox](https://nox.thea.codes/) configuration makes it easy to get set up and building Spyder-Infra in just one or two steps!

If you already have Nox installed, you're already done!
Otherwise, you can easily install it as a standalone tool with [pipx](https://pipx.pypa.io/) (if you don't have that either, you'll need to install it first if you go that route):

```shell
pipx install nox
```

Alternatively, install it into your global (or preferred) Python environment with the usual:

```shell
conda install nox
```

or, if not using Conda,

```shell
python -m pip install nox
```

To check that Nox is installed and browse a list of commands (called "sessions") we provide through Nox and what they do, run

```shell
nox --list
```

Then, run the ``setup`` session, which performs the project's one-time setup steps; pass either ``--https`` or ``--ssh`` to specify how you'd like to push changes to GitHub.
If not sure, pass ``--https`` for now:

```shell
nox -s setup -- --https
```

You can always switch it later with ``nox -s setup-remotes -- --ssh``.



## Setting Up a Development Environment Manually

For advanced users, if you'd prefer to also have your own local environment with the project dependencies that doesn't go through Nox, you can also set one up yourself.

**Note**: You may need to substitute ``python3`` for ``python`` in the commands below on some Linux distros where ``python`` isn't mapped to ``python3`` (yet).


### Create and activate a fresh environment

We highly recommend you create and activate a virtual environment to avoid any conflicts with other packages on your system or causing any other issues.
Of course, you're free to use any environment management tool of your choice ([conda](https://docs.conda.io/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/), [pyenv](https://github.com/pyenv/pyenv), etc).
Regardless of the tool you use, make sure to remember to always activate your environment before using it.


#### Conda

To create an environment with Conda (recommended), simply execute the following:

```shell
conda create -c conda-forge -n spyder-infra-env python
```

Then, activate it with

```shell
conda activate spyder-infra-env
```


#### Pip/Venv

With pip/venv, you can create a virtual environment with

```shell
python -m venv spyder-infra-env
```

And activate it with the following on Linux and macOS,

```bash
source spyder-infra-env/bin/activate
```

or on Windows (``cmd.exe``),

```cmd
.\spyder-infra-env\Scripts\activate.bat
```


### Install dependencies

Then, since you're not using Nox, you need to install the appropriate dependencies in your active Python environment to develop and build the documentation.
You can install them into your current Conda environment with:

```shell
conda install -c conda-forge --file requirements.txt
```

Or if using ``pip``, you can grab them with:

```shell
python -m pip install -r requirements.txt
```


### Add the upstream remote

Make sure to set the upstream Git remote to the official Spyder-Infra repo with:

```shell
git remote add upstream https://github.com/spyder-ide/spyder-infra.git
```



## Installing and Using the Pre-Commit Hooks

This repository uses [Pre-Commit](https://pre-commit.com/) to install, configure and update a suite of pre-commit hooks that check for common problems and issues, and fix many of them automatically.
You'll need to install the pre-commit hooks before committing any changes, as they both auto-generate/update specific files and run a comprehensive series of checks to help you find likely errors and enforce the project's code quality guidelines and style guide.
They are also run on all pull requests, and will need to pass before your changes can be merged.

If you've [using Nox](#setting-up-a-development-environment-with-nox-recommended), it installs Pre-Commit and its hooks for you when running ``nox -s setup`` (as above).
You can also install them with

```shell
nox -s install-hooks
```

If you've followed the [manual install approach](#install-dependencies), Pre-Commit will be installed directly in your local environment.
To install the hooks, run the following from the root of this repo:

```shell
pre-commit install --hook-type pre-commit --hook-type commit-msg
```

The hooks will be automatically run against any new/changed files every time you commit.
It may take a few minutes to install the needed packages the first time you commit, but subsequent runs should only take a few seconds.
If you made one or more commits before installing the hooks, or would like to run them manually on everything in the repo, you can do so with:

```shell
nox -s lint
```

or

```shell
pre-commit run --all-files
```

**Note**: Many of the hooks fix the problems they detect automatically (the hook output will say ``Files were modified by this hook``, and no errors/warnings will be listed), but they will still abort the commit so you can double-check everything first.
Once you're satisfied, ``git add .`` and commit again.



## Building the Project

The project is built with _FIXME_BUILD_TOOL, which you can invoke either using [Nox](https://nox.thea.codes/) or manually.


### Build with Nox

To build the project using Nox, just run

```shell
nox -s build
```

and can then open the rendered output in your default web browser with

```shell
nox -s serve
```

Alternatively, to automatically rebuild the project when changes occur, you can invoke

```shell
nox -s autobuild
```

You can also pass your own custom [_FIXME_BUILD_TOOL build options](_FIXME_BUILD_OPTIONS_URL) after a ``--`` separator which are added to the default set.

_FIXME_BUILD_OPTIONS_EXAMPLE


### Build manually

For manual installations, you can invoke _FIXME_BUILD_TOOL yourself with the appropriate options:

```shell
_FIXME_BUILD_COMMAND
```

Then, navigate to the ``_FIXME_BUILD_DIRECTORY`` directory inside the ``spyder-infra`` repository and _FIXME_HOW_TO_RUN.


## Contributing Changes


### Decide which branch to use

When you start to work on a new pull request (PR), you need to be sure that your work is done on top of the correct branch, and that you base your PR on GitHub against it.

To guide you, issues on GitHub are usually marked with a label or milestone that indicates the correct branch to use.
If not, base your PR against the ``_FIXME_MAIN_BRANCH`` unless it addresses an issue specific to another branch.
You're always welcome to ask if you're unsure!


### Prepare your topic branch

To start working on a new PR, you need to execute these commands, filling in the branch names where appropriate (``<BASE-BRANCH>`` is the branch you're basing your work against, e.g. ``_FIXME_MAIN_BRANCH``, while ``<TOPIC-BRANCH>`` is the branch you'll be creating to store your changes, e.g. ``fix-doc-typo`` or ``add-new-plugin``:

```shell
git switch <BASE-BRANCH>
git pull upstream <BASE-BRANCH>
git switch -c <FEATURE-BRANCH>
```


### Commit your changes

Once you've made and tested your changes, add them to the staging area, and then commit them with a descriptive message.
Commit messages should be

* Descriptive: Clearly summarize your changes and their purpose
* Unique: Not "Fix typo" followed by "Fix typo"
* Concise: Keep your message to 74 characters or less
* Imperative: Write your messages in the imperative tense, e.g. "Fix this" or "Add that"
* Titles: Capitalized first letter and no period at the end

Try to make your commit message understandable on its own, giving the reader a high-level idea of what your changes accomplished without having to dig into the full diff output.
For example:

```shell
git add .
git commit -m "Add new guide on developing plugins for Spyder"
```

If your changes are complex (more than a few dozen lines) and can be broken into discrete steps/parts, its often a good idea to make multiple commits as you work.
On the other hand, if your changes are fairly small (less than a dozen lines) and part of the same atomic step, its usually better to make them as a single commit.
If you haven't yet pushed your latest commit to a pull request, but find you need to add something directly related to a previous commit, you can run ``git -a --amend`` (e.g. if you spot a bug or issue with what you've just committed).

These aren't hard and fast rules, so just use your best judgment, and if there does happen to be a significant issue we'll be happy to help.


### Push your branch

Now that your changes are ready to go, you'll need to push them to the appropriate remote repository.
All contributors, including core developers, should push to their personal fork and submit a PR from there, to avoid cluttering the upstream repo with feature branches.
To do so, run:

```shell
git push -u origin <TOPIC-BRANCH>
```

Where ``<TOPIC-BRANCH>`` is the name of your topic branch, e.g. ``fix-docs-typo``.


### Submit a Pull Request

Finally, create a pull request to the [``spyder-ide/spyder-infra`` repository](https://github.com/spyder-ide/spyder-infra/) on GitHub.
Make sure to set the target branch to the one you based your PR off of (e.g. ``_FIXME_MAIN_BRANCH`` or ``X.x``).

We'll then review your changes, and after they're ready to go, your work will become an official part of Spyder-Infra.

Thanks for taking the time to read and follow this guide, and we look forward to your contributions!



## Standards and Conventions


### Key standards

Make sure you follow these to ensure clarity, consistency and correctness throughout the our organization.

* **[reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)** (reST/rst) for documentation format
* **[PEP 8](https://www.python.org/dev/peps/pep-0008/)** style for any Python code
* **[UTF-8](https://en.wikipedia.org/wiki/UTF-8)** (no BOM) for character encoding
* **[LF](https://en.wikipedia.org/wiki/Newline)** for newlines
* **[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)** (YYYY-MM-DD HH:MM:SS) for dates/times
* **[SI/metric](https://en.wikipedia.org/wiki/International_System_of_Units)** for units
