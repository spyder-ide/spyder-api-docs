# Future work

## On mixins

Mixins are classes that contains methods for use by other classes without
having to be the parent class of those other classes. How those other classes
gain access to the mixin's methods depends on the language. Mixins are sometimes
described as being "included" rather than "inherited".

For this reason a common pattern with mixing is that they should not have a
constructor as this implies that an any class using a mixin now needs to make
sure that it follows some constructor which goes against the idea of just
injecting some functionality.

Some current examples on the Spyder code base that present this problem include:

* Mixing module!


The idea of this issue is to star listing all the things we need to have in place to provide a simple api to do general things (create menus, create toolbars) and a simple api for more specific things. Please update this comment to include your suggestions

# General

- [ ] Create a new entry for a menu
        - Define where in the menu it can go? assign an space always at the end?
- [ ] Create a new toolbar
       - Create a new action
       - Create icons
- [ ] Create new shortcut for a menu or toolbar action; cf. #3254 and #7894
- [ ] Register file type for creating, opening and saving files, e.g. notebook files; see PR #8798 (WIP)
- [ ] Configuration
       - Define, read and set new config variables
       - Define, read and set project-specific config variables
       - Define tab in config dialog for setting these variables
       - Read config variables that do not belong to the plugin; get notified when they changed
       - Localization, e.g. `get_translation()`
- [ ] Utilities. Are `spyder.py3config` and `spyder.utils` part of the API? Separate out in Spyder-specific layer that can be called from the plugin level and a generic layer that can be called from widgets?

# Specific
- [ ] Allow for users to extend the pattern search on the editor. Will require moving the logic for it to be a mode so it can be more easily extended
- [ ] Create a new data type or the variable explorer to handle
      - This probably requires updating the `_io` plugins to a more  "normal api"
- [ ] Go to file/line in editor, opening the file if necessary
- [ ] Get active project
- [ ] Signals
      - Main: `sig_pythonpath_changed`
      - Projects: `sig_project_created`, `sig_project_loaded`, `sig_project_closed`
      - Workingdirectory: `set_explorer_cwd`
- [ ] A utility class for displaying log files and other text; currently `variableexplorer.texteditor` is used for this


# Future
Things to keep in mind but probably not needed for Spyder 4.
- [ ] Expose a kernel which can be coupled to Console, Variable Explorer, Debugger; e.g. for notebook kernels or post-mortem debugging in unit tests
- [ ] Colour lines in editor, e.g. for profiling information or for coverage
