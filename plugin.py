# This is used for the `get_help` function around line 27 - YAML - Yet Another Markup Language - it's like JSON, but it allows for comments and can have less cruft
import yaml
# This is where most of the plugin structure will be coming from.  The Class definition around like 13 is saying "Create a new type of Plugin like the 'Base'".
import plugins
# This is the Operating System library.  It has a function called 'getLogin() we're using around line 37 - https://docs.python.org/3/library/os.html#os.getlogin
import os
# Not sure if this is needed, but this should be where the error handling comes from.  If you had an error, your would call something like `error_print('my error message')`
from src.console.utils import error_print
# Not sure if you need this - but if you want to read the Settings, but there might be user info here for the 'whoami' side of things
from src.console import Settings

#If the filename you are working on is `EchoPlugin.py` then name this file `WhoamiPlugin.py`
class WhoamiPlugin(plugins.Base):
    PLUGIN_NAME = 'whoami'
    # This initializes the Plugin - e.g. it tells it what commands it has in it.
    def __init__(self):
        self.command_list = []
        self.command_list.append(('whoami', self.whoami))

    # This isn't really needed here probably - there isn't anything that's being 'warmed up' prior to starting.
    # For Example: You would use something like this to maybe lookup the last ticket number entered into a DB if the plugin was creating a new ticket.  We shouldn't need anything to start up.
    async def start(self):
        print("starting up")

    # This allows for documentation - there is probably something like a '--help' command defined in the plugin.Base that returns the output of this function - so `whoami --help` would print this.
    @staticmethod
    async def get_help():
        help_page = """
        commands:
         - whoami: Prints the OS provided Username
        """
        content = yaml.safe_load(help_page)
        return content

    # This is the actual function that will be outputing the user information.  Depending on what the requirements are this is where things will end up going.
    async def whoami(self):
        print('You are user: ' + os.getLogin())

    # #This is an example of what another command might look like:
    #
    # #Add this to the `def __init__(self)` list of commands
    # self.command_list.append(('whatismy', self.whatismy))
    #
    # #Add this to the `get_help` help_page block (line 28)
    # - whatismy:
    #   - id: Prints your user ID
    #   - email: Prints your email address
    #
    # #This is the actual 'working' part of that new command
    # async dev whatismy(self, args: list):
    #     if args[0] == 'id':
    #         print('You are User ID: ' + userIDLookedUpFromSomewhereElse)
    #     elif args[0] == 'email':
    #         print('Your Email is: ' + emailAddressLookedUpFromSomewhereElse)
    #     else:
    #         await error_print('No a valid user data element to look up')