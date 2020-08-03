# Third party imports
from setuptools import find_packages, setup

# Local imports
from my_spyder_plugin import __version__


setup(
   name="my-spyder-plugin",
   version=__version__,
   description="My first Spyder plugin",
   packages=find_packages(),
   entry_points={
      "spyder.plugin": "my_spyder_plugin.plugin::MySpyderPlugin"
   }
)
