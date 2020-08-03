# Codebase orientation

## Extension Developer Guide

Spyder can be extended via:

1. Application plugins (top level): Application plugins extend the
   functionality of Spyder itself. An example of this would be a new Plugin
   that created a new Pane to provide some functionality.
2. Plugins API extension (plugin level):  A plugin provides an API to extend
   its functionality. An example of this would be a completion provide, that
   would extend the available completion providers. Another example would be
   a new Prpoject Type, that would allow users to create specific types of
   projects with custom creation, starting, and closing logic.

The Spyder application is comprised of:

* The spyder main window application object
* Plugins
* Some global widgets
* Some global utilities

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

* Core:
* Appearance:
* Completions:
* Shortcuts:
* Editor:
* Outline Explorer:
* Projects:
* IPython Console:
* Variable Explorer:
* Help:
* Plots:
* History:
* Find:
* Profiler:
* Code analysis:

Here is a dependency graph for the Spyder (internal) plugins:

## Configuration and preferences

## Global API

## Global Widgets

## Global utilities
