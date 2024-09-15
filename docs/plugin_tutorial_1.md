# Our first Spyder plugin

## What we will learn

1. Setting the development environment.
2. Create the basic structure of a plugin.
3. Create a new action to open a link in youtube.
4. Set a shortcut for our new action.
5. Add the newly created action to an application menu.

## Set the development environment

### Conda (the recommended way)

```{margin} **More information**
(TODO: Link to conda environments.)
(TODO: Link to python environments.)
```

```bash
conda create --name spyder-plugin "python=3.8" "spyder=5" --channel conda-forge --yes --quiet
conda activate spyder-plugin
```

```{warning} Mixing conda and pip packages
Here is [markdown link syntax](https://jupyter.org)
```

Conda/Pip

## Create the plugin basic structure

Let's create a new folder where the code for our plugin will live.

```bash
my-spyder-plugin
│
├── my_spyder_plugin
│   │
│   ├── __init__.py
│   │
│   └── plugin.py
│
└── setup.py
```

### `__init__.py`

Spyder plugins are Python installable packages, so we need to define some
information. For now we just need to add a version string for our package.

```{margin} **More information**
(TODO: Link to semantic versioning.
```

We recommend using semantic versioning. This basically means a version is
divided in `"Major.Minor.Patch"` components where:

* **Major**: TODO:
* **Minor**: TODO:
* **Patch**: TODO:

```{code-block} python
---
caption: |
  `my-spyder-plugin/my_spyder_plugin/__init__.py`
---

__version__ = "0.1.0"

```

### `plugin.py`

```{margin} **More information**
(On plugins and on icons)
```

```{code-block} python
---
caption: |
  `my-spyder-plugin/my_spyder_plugin/plugin.py`
---

# Third party imports
from spyder.api.plugins import SpyderPluginV2


class MySpyderPlugin(SpyderPluginV2):
   ID = "my_spyder_plugin"

   # --- SpyderPluginV2 API
   # -------------------------------------------------------------------------
   def get_name(self):
      return "My Awesome Spyder Plugin"

   def get_description(self):
      return "A really Awesome Spyder Plugin"

   def get_icon(self):
      return self.create_icon("settings")

   def register(self):
      self.print_hello()

   # --- Public API
   # -------------------------------------------------------------------------
   def print_hello(self):
      print("Hello world!")

```

### `setup.py`

```{margin} **More information**
(TODO: Link to semantic python packaging for more info if interested)
```

```{code-block} python
---
caption: |
  `my-spyder-plugin/setup.py`
emphasize-lines: 13-15
---

# Third party imports
from setuptools import find_packages, setup

# Local imports
from my_spyder_plugin import __version__


setup(
   name="my-spyder-plugin",
   version=__version__,
   description="My first Spyder plugin"
   packages=find_packages(),
   entry_points={
      "spyder.plugin": "my_spyder_plugin.plugin::MySpyderPlugin"
   }
)
```

## Creating a Plugin action

TODO:

```{code-block} python
---
caption: |
  `my-spyder-plugin/my_spyder_plugin/plugin.py`
emphasize-lines: 2-7
---

   def register(self):
      self.create_action(
         "print_message_name",
         text="Print a message!",
         icon=self.create_icon("print"),
         triggered=self.print_hello,
      )
      self.print_hello()


```

## Assigning a shortcut

TODO:

## Adding it to an application menu

TODO:

## Final result

```{code-block} python
---
caption: |
  `my-spyder-plugin/my_spyder_plugin/plugin.py`
---

# Third party imports
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.plugins.core.api import ApplicationMenus, HelpMenuSections


class MySpyderPlugin(SpyderPluginV2):
   ID = "my_spyder_plugin"
   REQUIRES = [Plugins.Core]

   # --- SpyderPluginV2 API
   # -------------------------------------------------------------------------
   def get_name(self):
      return "My Awesome Spyder Plugin"

   def get_description(self):
      return "A really Awesome Spyder Plugin"

   def get_icon(self):
      return self.create_icon("settings")

   def register(self, core):
      # Create a plugin action
      print_action = self.create_action(
         "print_message_name",
         text="Print a message!",
         icon=self.create_icon("print"),
         triggered=self.print_hello,
         register_shortcut=True,
      )

      # Add the action to an existing menu
      help_menu = self.get_plugin(ApplicationMenus.Help)
      core.add_item_to_application_menu(
         print_action,
         menu=help_menu,
         section=HelpMenuSections.Documentation,
      )

      self.print_hello()

   # --- Public API
   # -------------------------------------------------------------------------
   def print_hello(self):
      print("Hello world!")
```

TODO: Add screenshot or wireframe image

## What we covered

TODO:

## Next steps

TODO:
