# Third party imports
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.plugins.core.api import ApplicationMenus, HelpMenuSections


class MySpyderPlugin(SpyderPluginV2):
   ID = "my_spyder_plugin"
   REQUIRES = [Plugins.Core]

   # --- SpyderPluginV2 API
   # -------------------------------------------------------------------------
   def get_name(self):
      return "My Awesome Spyder Plugin"

   def get_description(self):
      return "A really Awesome Spyder Plugin"

   def get_icon(self):
      return self.create_icon("settings")

   def register(self, core):
      print_action = self.create_action(
         "print_message_name",
         text="Print a message!",
         icon=self.create_icon("print"),
         triggered=self.print_hello,
         register_shortcut=True,
      )

      help_menu = self.get_plugin(ApplicationMenus.Help)
      core.add_item_to_application_menu(
         print_action,
         menu=help_menu,
         section=HelpMenuSections.Documentation,
      )

      self.print_hello()

   # --- Public API
   # -------------------------------------------------------------------------
   def print_hello(self):
      print("Hello world!")
