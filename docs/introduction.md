# Contributing to Spyder

This section will help you to set up an environment for contributing to Spyder as well as creating third party Spyder Plugins.

## First contribution

If this is your first time contributing to Spyder or in general to open source we invite you to watch the video below which will guide you with the main steps with doing your first contribution.

<figure class="video_container">
  <iframe src="https://www.youtube.com/embed/GizipMT1LvQ" frameborder="0" allowfullscreen="true"> </iframe>
</figure>

For a detailed explanation, follow the instructions below.

### Clone and Fork the repository

The first thing you need to do fork Spyder's repository. To do this, log into your account on GitHub and click the “Fork” button at the top left of the project's page. This will create a copy of the repository in your own account.

![fork.png](images/fork.png) 

Then, click the ``Clone or Download`` button on your repository and copy the link.

![fork.png](images/fork.png) 

After that, run the following on the command line (or Git Bash, if you’ve installed Git for Windows) to clone the repo:

```bash
$ git clone <LINK-TO-YOUR-REPO>
```

Set the upstream remote to the official Spyder repo with:

```bash
$ git remote add upstream https://github.com/spyder-ide/spyder.git
```

This will allow you to keep your local repo up to date with the latest changes in Spyder.

For a beginner guide on using Git, check the link below:

https://rogerdudler.github.io/git-guide


### Create a conda environment or virtualenv

If you use Anaconda you can create a conda environment with the following commands:

```bash
$ conda create -n spyder-dev python=3
$ conda activate spyder-dev
```

You can also use `virtualenv` on Linux, but `conda` is **strongly** recommended:

```bash
$ mkvirtualenv spyder-dev
$ workon spyder-dev
```

### Installing dependencies

After you have created your development environment, you need to install Spyder's necessary dependencies. The easiest way to do so (with Anaconda) is

```bash
$ conda install -c spyder-ide/label/dev --file requirements/conda.txt
```

This installs all Spyder's dependencies into the environment.
If you are running on macOS, you will also need to install `python.app`.

```bash
$ conda install python.app
```

If using `pip` and `virtualenv` (not recommended), you need to `cd` to the directory where your git clone is stored and run:

```bash
$ pip install -e .
```


### Running Spyder

To start Spyder directly from your clone, i.e. without installing it into your environment, you need to run (from the directory you cloned it to e.g. `spyder`):

```bash
$ python bootstrap.py
```
Note that if you are running on macOS, you will need to call `pythonw` instead of `python`.

To start Spyder in debug mode, useful for tracking down an issue, you can run:

```bash
$ python bootstrap.py --debug
```
### Commit your changes

Once you make your changes to the repository, 
you have to create a branch for your work. 

**NOTE**
If your change is small, like a bug fix or minor UI improvement, you should make it to the branch for the current version of Spyder, in this case “5.x”, instead of master. You need to base your new branch on the correct Spyder branch in order to avoid conflicts.

Here, we will explain how to do it with 5.x.

Run:

```bash
$ git checkout 5.x
```

Make sure to reset the spyder configuration file when switching between master and 5.x by running:

```bash
python bootstrap.py -- --reset
```

Next, create your branch from this one. Remember to give your branch a name that is related to your fix. For this, run the following command:

```bash
git checkout -b [BRANCH-NAME]
```

Add and commit your changes with a descriptive message.

```bash
git commit -a -m “[MESSAGE]”
```

Finally, push your new branch with your changes to your fork on GitHub:
 
```bash 
git push -u origin pythonpath-tooltip
```

Enter your GitHub username and password if requested.

### Opening a PR

Now, you can submit your changes to Spyder’s repo. 

Go to the Spyder repository on Github, and you will see the option to open a Pull Request. Before submitting it, make sure that you read the template. 

![fork.png](images/PR.png) 

Make sure that you select the correct branch to merge your changes.
 
## Issue tracker 

Labels issue tracker ?


## Other ways to contribute

1. Issue testing and triaging: 
-check if older bugs are still present
-find duplicate issues and link related ones
-add good self-contained reproducers to issues
-label issues correctly (this requires triage rights – just ask)
2. Reviewing PRs
3. Translations: Crowdin 
4. Improving documentation:  
-Reading tutorials and reporting confusing parts, 
-finding type-os and minor errors in docs
-writing your own guides and tutorials
-improving docstrings within the code, and -improving documentation style and design.
5. Participating in the community
-help
-sharing 
6. Developing educational materials
7. Community outreach


