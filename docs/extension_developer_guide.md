# Codebase orientation

## Developer Guide

Spyder can be extended via:

1. **Application plugins** (top level): Application plugins extend the
   functionality of Spyder itself. An example of this would be a new Plugin
   that created a new Pane to provide some functionality.
2. **Plugins API extension** (plugin level):  A plugin provides an API to extend
   its functionality. An example of this would be a completion provide, that
   would extend the available completion providers. Another example would be
   a new Prpoject Type, that would allow users to create specific types of
   projects with custom creation, starting, and closing logic. There are two
   types of plugin in spyder:

Spyder is internally constructed using plugins and this is also the way a new
plugin/extension cna be created. The Spyder Plugins can be of two types:

1. **Spyder Dockable Plugins** (``SpyderDockablePlugin``), which create a new
   Pane (Based on a ``QDockWidget``) and (optionally) any other elements such
   as toolbars, menus, status bar widgets, curstom dialogs and a custom
   preferences page.
2. **Spyder Plugins** (``SpyderPluginV2``), which do not create a new Pane
   but provide other elements such as toolbars, menus, status bar widgets,
   curstom dialogs and a custom preferences page.

Plugins can provide the following widgets:

* **Pane** (``PluginMainWidget``): A plugin can create a new Pane.
* **Containers** (``PluginMainContainers``): Plugins that do not create new
  panes but provide other graphical elements can use a container to parent
  widgets and connect them to the plugin.
* **Actions** (``SpyderAction``): A plugin can create many new actions, which
  can be added to menus, toolbars, and can also be exposed so they can be
  used to create shortcuts that trigger these actions.
* **Preferences Page** (``PluginConfigPage``): A page for plugin preferences.
  A plugin can only have 1 page.
* **Application menus** (``SpyderApplicationMenu``): A plugin can extend or
  create new application menus
* **Application toolbars** (``SpyderApplicationToolBar``): A plugin can extend
  or create new application toolbars
* **StatusBar widgets** (``SpyderStatusWidget``): A plugin can extend or
  create new application status bar widgets.

Plugins are distributed as python packages, so you can write plugins and
publish them in PyPI or Conda forge.

## Tutorials

We provide a set of guides to get started writing third-party plugins for Spyder:

* Tutorial 1
* Tutorial 2
* Tutorial 3

## Cookiecutters

We provide a simple cookiecutter to create Spyder plugin:

* Cookiecutter.

## API Documentation

If you are looking for lower level details on the spyder and Qt API:

* Spyder API Documentation
* Qt API Documentation

## Plugins

A plugin adds a core functionality to the application.

* A plugin can require other plugins for operation.
* A plugin is activated when it is needed by other plugins, or when explicitly
  activated.
* Plugins require and provide Token objects, which are used to provide a typed
  value to the plugin’s activate() method.
* The module providing plugin(s) must meet the JupyterLab.IPluginModule
  interface, by exporting a plugin object or array of plugin objects as the
  default export.

The default plugins in the Spyder application include:

* **Core**: Creates application menus and status bar widgets.
* **Appearance**: Sets the theme of the interface and editors.
* **Completions**: Provides code completion to editor widgets using the
  [Language server protocol](TODO:).
* **Shortcuts**: Provides the handling of shortcuts.
* **Editor**: Provides a splitable multilingual Editor with introspection
  capabilities.
* **Outline Explorer**:
* **Projects**:
* **IPython Console**:
* **Variable Explorer**:
* **Help**:
* **Plots**:
* **History**:
* **Find**:
* **Profiler**:
* **Code analysis**:

Here is a dependency graph for the Spyder (internal) plugins:

![dependency_graph.png](images/dependency_graph.png)

## Configuration and preferences

## Global API

## Global Widgets

## Global utilities
