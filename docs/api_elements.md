# API elements

Spyder works like a set of loosely coupled components. Here you will find a description of the main elements that compose Spyder's API.

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

There two types of plugins in Spyder's API:

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

### Spyder's Plugins

The default plugins in the Spyder application include:

* **Core**: Creates application menus and status bar widgets.
* **Appearance**: Sets the theme of the interface and editors.
* **Completions**: Provides code completion to editor widgets using the
  [Language Server Protocol](https://microsoft.github.io/language-server-protocol/).
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

## Configuration

Default configuration settings

## Global API

General elements in Spyder's API. (Creation of classes)

## Global Widgets:
Auxiliar graphical elements used throughout several plugins.

## Global utilities:

## Global APP:

Related to Qt Application and Main Window.

## Grafical elements

Images + Fonts



### CLASS NAMES

``SpyderAction``


``SpyderApplicationToolBar``

``SpyderToolBar``

### Status bar:

``SpyderStatusWidget``

### Menus:

``SpyderApplicationMenu``

``SpyderMenu``

