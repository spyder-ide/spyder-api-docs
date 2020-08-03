# Common extension points

## Completion Providers

```python
from spyder.api.translation import get_translation
from spyder.plugins.projects.api import BaseProjectType


class NewProjectType(BaseProjectType):
    ID = None

    def __init__(self, root_path, parent_plugin=None):
        super().__init__(root_path, parent_plugin)

    # --- Configuration
    # -------------------------------------------------------------------------
    def get_option(self, option, section=WORKSPACE, default=None):
        """Get project configuration option."""
        return self.config.get(section=section, option=option, default=default)

    def set_option(self, option, value, section=WORKSPACE):
        """Set project configuration option."""
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
        return True, ""

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
        return False, "A ProjectType must define a `create_project` method!"

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
        return False, "A ProjectType must define an `open_project` method!"

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
        return False, "A ProjectType must define a `close_project` method!"
```

And then register the new project type with the projects plugin.

```python

class Plugin(SpyderPluginV2):

    def register(self):
        projects = self.get_plugin("project_explorer")
        self.register_project_type(self, NewProjectType)
```
