# Extending Spyder

Spyder offers different way of extending the global application and extending
the functionality of plugins tehmeselves.

## Application extension points

### Creating actions and shortcuts

### Main application menus

There are three main ways to extend Spyder's application menu.

1. You can add new application menu to the application menu bar.
2. You can add new actions to the existing application menus.
3. You can override or extend one of the existing application menu actions.

#### Creating a new application menu

To add a new menu to the menu bar, you need to create one with the `core` plugin.

You can then add actions to the menu.

```python
from spyder.api.plugins import Plugins, SpyderPluginV2


class SomePlugin(SpyderPluginV2):

    def register(self):
        core = self.get_plugin(Plugins.Core)
        extras_menu = core.create_application_menu(
            "extras_menu",
            title="Extras",
        )
```

#### Adding a new action to an existing menu

```python
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.plugins.core.api import HelpMenuSections


class SomePlugin(SpyderPluginV2):

    def register(self):
        core = self.get_plugin(Plugins.Core)
        help_menu = core.get_menu("help_menu")

        # Create a new action
        run_action = self.create_action(
            "hello_world_action"
            text="Print Hello World!",
            triggered=lambda: print("Hello World!"),
        )

        # Add action to menu
        self.add_item_to_menu(
            run_action,
            menu=help_menu,
            section=HelpMenuSections.Documentation,
        )
```

#### Extending an existing action

```python
# TODO:
```

### Application toolbars

### Status bar

Status bar widgets!

TODO:

## Plugin extension points

### Appearance

Themes etc..

### Layouts

Custom layouts

### Projects

#### A new project type

```python
# ./a_plugin/project_types.py

# Third party imports
from spyder.api.translation import get_translation
from spyder.plugins.projects.api import BaseProjectType


# Localization
_ = get_translation("a_plugin")


class NewProjectType(BaseProjectType):
    ID = None

    def __init__(self, root_path, parent_plugin=None):
        super().__init__(root_path, parent_plugin)

    # --- Configuration
    # -------------------------------------------------------------------------
    def get_option(self, option, section=WORKSPACE, default=None):
        """
        Get project configuration option.
        """
        return self.config.get(section=section, option=option, default=default)

    def set_option(self, option, value, section=WORKSPACE):
        """
        Set project configuration option.
        """
        self.config.set(section=section, option=option, value=value)

    # --- API
    # ------------------------------------------------------------------------
    @staticmethod
    def get_name():
        """
        Provide a human readable version of NAME.
        """
        raise NotImplementedError("Must implement a `get_name` method!")

    @staticmethod
    def validate_name(path, name):
        """
        Validate the project's name.

        Returns
        -------
        tuple
            The first item (bool) indicates if the name was validated
            successfully, and the second item (str) indicates the error
            message, if any.
        """
        return True,  _("Some usefull error message in case of problems.")

    def create_project(self):
        """
        Create a project and do any additional setup for this project type.

        Returns
        -------
        tuple
            The first item (bool) indicates if the project was created
            successfully, and the second item (str) indicates the error
            message, if any.
        """
        return False, _("Some usefull error message in case of problems.")

    def open_project(self):
        """
        Open a project and do any additional setup for this project type.

        Returns
        -------
        tuple
            The first item (bool) indicates if the project was opened
            successfully, and the second item (str) indicates the error
            message, if any.
        """
        return False,  _("Some usefull error message in case of problems.")

    def close_project(self):
        """
        Close a project and do any additional setup for this project type.

        Returns
        -------
        tuple
            The first item (bool) indicates if the project was closed
            successfully, and the second item (str) indicates the error
            message, if any.
        """
        return False,  _("Some usefull error message in case of problems.")
```

And then register the new project type with the projects plugin.

```python
# ./a_plugin/plugin.py

# Third party imports
from spyder.api.plugins import Plugins, SpyderPluginV2

# Local imports
from a_plugin.project_types import NewProjectType


class SomeAwesomePlugin(SpyderPluginV2):
    # ...
    def register(self):
        projects = self.get_plugin(Plugins.Projects)
        self.register_project_type(self, NewProjectType)
    # ...
```

#### A new project type from a cookiecutter

TODO:

#### Several project types

TODO:

### Completion providers

TODO:
