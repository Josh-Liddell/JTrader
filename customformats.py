import argparse as ap
import textwrap


# In this file I am overriding methods to allow me to customize the help and version outputs

# Changing the usage prefix, adding logo before and a newline after the help output
class CustomFormatter(ap.HelpFormatter):
    # Using this class to format my help page
    # helpformatter is the default class used by argparse to format and display help messages
    def __init__(self, prog):
        super().__init__(prog, width=200, max_help_position=50)

    # Customizing prefix
    def _format_usage(self, usage, actions, groups, prefix):
        prefix = 'How to use: '
        return super()._format_usage(usage, actions, groups, prefix)

    def format_help(self):
        logo = r'''
               ________               __
              / /_  __/________ _____/ /__  _____
         __  / / / / / ___/ __ `/ __  / _ \/ ___/
        / /_/ / / / / /  / /_/ / /_/ /  __/ /
        \____/ /_/ /_/   \__,_/\__,_/\___/_/
        '''

        # This puts my logo before the rest of the default help page
        return textwrap.dedent(logo) + '\n' + super().format_help() + '\n'


# Here I customzed the Argument parser to change the order of the help outputs, and if -h is called to use the custom formatting
class CustomArgParser(ap.ArgumentParser):
    # Overriding the format help func to change order of help page entries
    def format_help(self):

        formatter = self._get_formatter()

        # description
        formatter.add_text(self.description)

        # usage
        formatter.add_usage(self.usage, self._actions,
                            self._mutually_exclusive_groups)

        # positionals, optionals and user-defined groups
        for action_group in self._action_groups:
            formatter.start_section(action_group.title)
            formatter.add_text(action_group.description)
            formatter.add_arguments(action_group._group_actions)
            formatter.end_section()

        # epilog
        formatter.add_text(self.epilog)

        # determine help from format above
        return formatter.format_help()

    # By overriding this, customformatter is only used when -h is called not the other ones like -v or when an error happens
    def print_help(self, file=None):
        self.formatter_class = CustomFormatter
        super().print_help(file)
