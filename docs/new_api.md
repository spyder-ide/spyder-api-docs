# The new API

This document will try to give an explanation of why Spyder 5 incurred in a
major refactoring of the codebase and redefinition of its plugin API.

## The guiding principles

1. Spyder should be provide a set of loosely coupled components with a clear
   hierarchy and dependency instead from a tightly coupled monolith.
   This means that some plugins have REQUIRED dependencies that must be
   present for the plugin to be able to be loaded, and there are OPTIONAL
   dependencies, that will not prevent the plugin from starting and working
   with other plugins

2. Spyder should be written in the same way any external developer would, when
   extending or creating a Spyder Plugin.

3. Spyder should provide 1 way and 1 way only for handling plugins, that means
   that even if plugins are providing very different functionality, the basic
   principles for creating, regustering, setting up, loading, closing and
   accessing the configuration system should be the same for all.

## Work

### Remove circular dependencies among plugins

TODO:

### Only access configuration for REQUIRED and OPTIONAL dependencies

TODO:

### Fix mixins that require custom `__init__` calls

TODO:

### Fix signal names

TODO:

### The Spyder main application

TODO:

### The plugin interface

TODO:

#### Plugin

TODO:

### Main Containers

TODO:

#### Main Widgets

TODO:
