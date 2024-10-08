# Frequently asked questions

This is the FAQ section: (Should be the same as in the docs)

Please post any new questions under the Spyder tag in [[Stack Overflow|http://stackoverflow.com/questions/tagged/spyder]].

This FAQ is for development-related questions. For questions about Spyder itself, see the [[Troubleshooting Guide and FAQ]].


## Does the GPL exception hold for PyQt5?

Please take a look at [this thread](https://riverbankcomputing.com/pipermail/pyqt/2014-February/033843.html)


## How to debug Spyder

Another way you can help us to debug this is by opening a terminal and starting Spyder with this command:

```bash
spyder --debug-info verbose --debug-output file
```

After doing that, a file called `spyder-debug.log` will be generated in the same directory where you ran that command. You can then upload this file when you issue a file report.

Also, before closing Spyder, you can also go to the the menu `Tools > LSP logs` (which is only shown in debug mode):

and click on the two entries shown on it to open those files in the editor, and upload their contents also to the issue you are reporting.
