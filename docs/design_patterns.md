# Design patterns

Here we will explain some useful guidelines that you should take into account to write your code.


## Python style

Unless otherwise specified, follow
[PEP 8](https://peps.python.org/pep-0008/) specifications and
recommendations for coding style and
[PEP 257](https://peps.python.org/pep-0257/) for docstrings.

Use flake8 to check for problems in this area. Remember that PEP 8 is only a
guide, so respect the style of the surrounding code as a primary goal.

Additional conventions:

* Always use four (4) spaces for **indentation**, including continuation lines
  and hanging indents, except for:
* Use 8 spaces for hanging indent continuations of the ``def``, ``if``,
  ``for``, ``while`` and ``with`` statements, to avoid confusion with their
  indented block.
* **Test-suite functions** need not have a separate summary line in the
  docstring, particularly if it is only a few lines long, though this is
  suggested for longer docstrings.
* Put the ``"""`` on their own lines for multi-line **docstrings**; keep them
  all in the same line for single-line docstrings, except for module-level
  docstrings.


## PyQt / PySide Style

Spyder aims to be compatible with PySide and PyQt, so make sure code runs with
both bindings.

Qt by default has its own conventions for the definitions of methods and
classes, and sometimes this clashes with was is suggested by
[PEP 8](https://peps.python.org/pep-0008/).

These are some suggestions to take into account when using the Qt bindings in
Python:


### Method naming conventions

Qt defines methods in camelCase, and when Spyder overloads these methods, we
cannot avoid camelCase. However, When new methods are defined in Spyder, these
methods should follow the PEP8 convention:

```python
class SpyderWidget(QWidget):
    """Example widget."""

    def __init__(self, parent):
        super()__init__(parent)

    def mousePressEvent(self, event):
        """Overload Qt method."""
        # Do something with the event...

    def run_new_method(self):
        """Run some new method."""
        # Do something interesting
```


### Widget Structure

Most Spyder widgets follow this convention (use it when creating new widgets)

```python
# Variables

# Widgets

# Widget setup

# Layout

# Signals
```

Example:

```python

class SomeWidget(QWidget):

    def __init__(self):
        super().__init__()

        # Variables
        self._some_private_variable = None
        self.some_variable = None

        # Widgets
        self.awesome_widget = SomeAwesoemWidget()

        # Widget setup
        self.awesome_widget.setSomething(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.awesome_widget)
        self.setLayout(layout)

        # Signals
        self.awesome_widget.sig_some_signal_requested.connect(
            self.some_method)
```


### Docstrings

Docstrings are sentences in the infinitive form and ended with a dot `.`.
The `__init__` share (at least) the same docstring as the class.

Example:

```python

class SomeWidget():
    """Create some widget."""

    SOME_CLASS_ATTRIBUTE = True
    """
    This explanation on this attribute.
    """

    sig_something_requested = Signal(str, dict)
    """
    This signal is emitted to request something.

    Parameters
    ----------
    some_indicative_name: str
        Some explanation.
    some_indicative_name_2: dict
        Some other explanation.
    """

    def __init__(self):
        """Create some widget."""

    def run_something(self, param_1, param_2, param_3=True):
        """
        Create some widget.

        Parameters
        ----------
        param_1: str
            Some explanation.
        param_2: int
            Some explanation.
        param_3: bool, optional
            Some explanation. Default is True.

        Returns
        -------
        int:
            Some explanation.

        Notes
        -----
        Additional information.
        """
        # Something runs!

        return 10
```


### Imports

TODO:


### Internationalization / Localization

TODO:

```python
from spyder.api.translations import get_translation

_ = get_translation("spyder")
```


### Signals


#### Naming Do's

For naming new custom signals, use the `sig_` prefix and lowercase:

```python

# Third party imports
from qtpy.QtCore import Signal
from qtpy.QtWidget import Signal


class SomeWidget(QWidget):

    # Signals
    sig_something_happened = Signal(str)
```

Signals should provide a hint on what they do or what they need to request
and they should always start with the `sig_` prefix and end with a verb in
past (or past participle?).

If a widget (Subclass of QWidget) or object (Subclass of QObject) can
perform a given action, then that action must be indicated by the verb
ending the signal name.

If a widget has some common text functionalities and emits signals when
these are triggered, they should look something like:

```python
class SomeWidget(QWidget):

    sig_text_copied = Signal(str)
    sig_text_pasted = Signal(str)
```

If a widget (Subclass of QWidget) or object (Subclass of QObject) cannot
perform a given action, but needs to inform any connected widget that
something needs to happen, then the signal must end in `_requested`.

If a widget may offer the possibility of opening some file, but the widget
itself is not an editor, then the signal can be emitted to make this request:

```python
class SomeWidget(QWidget):

    sig_open_file_requested = Signal(str)
```


#### Naming Do not's

Signals should not be named like a methods/functions. The following are examples
of names not following the recommended convention.

```python
class SomeWidget(QWidget):

    sig_open_file = Signal(str)  # No verb indicating the action
    widget_ready = Signal(str)   # No sig prefix and no verb indicating the action
    doSomething = Signal(str)    # Uses Qt style names, not python ones

```
