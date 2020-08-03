# Tutorial: Our first Spyder plugin

## What we will learn

TODO:

## Set the development environment

```{margin} **More information**
(TODO: Link to conda environments.)
(TODO: Link to python environments.)
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
:caption: my-spyder-plugin/my_spyder_plugin/__init__.py

__version__ = "0.1.0"
```

### `plugin.py`

```{margin} **More information**
(On plugins and on icons)
```

```{code-block} python
:caption: my-spyder-plugin/my_spyder_plugin/plugin.py

# Third party imports
from spyder.api.plugins import SpyderPluginV2


class MySpyderPlugin(SpyderPluginV2):
   ID = "my_spyder_plugin"

   def get_name(self):
      return "My Awesome Spyder Plugin"

   def get_description(self):
      return "A really Awesome Spyder Plugin"

   def get_icon(self):
      return self.create_icon("settings")

   def register(self):
      print("Hello!")
```

### `setup.py`

```{margin} **More information**
(TODO: Link to semantic python packaging for more info if interested)
```

```{code-block} python
:caption: my-spyder-plugin/setup.py
:emphasize-lines: 13-15

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
:caption: my-spyder-plugin/my_spyder_plugin/plugin.py
:emphasize-lines: 18-22

# Third party imports
from spyder.api.plugins import SpyderPluginV2


class MySpyderPlugin(SpyderPluginV2):
   ID = "my_spyder_plugin"

   def get_name(self):
      return "My Awesome Spyder Plugin"

   def get_description(self):
      return "A really Awesome Spyder Plugin"

   def get_icon(self):
      return self.create_icon("settings")

   def register(self):
      self.create_action(
         "print_message_name",
         text="Print a message!",
         icon=self.create_icon("print"),
      )
```

## Assigning a shortcut

TODO:

## Adding it to an application menu

TODO:

## Creating a container widget to store more widgets

TODO:

## Moving the action from the plugin into the container

TODO:

## Creating a toolbar

TODO:

## Adding an action to the toolbar

TODO:

## Creating a status widget

TODO:

## Adding the status widget to the status bar

TODO:

## What we covered

TODO:

## Next steps

TODO:
