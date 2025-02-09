#!/home/joshua/.venv/bin/python3
import argparse as ap
import json


class CustomFormatter(ap.HelpFormatter):
    # Using this class to format my help page
    # helpformatter is the default class used by argparse to format and display help messages
    def __init__(self, prog):
        super().__init__(prog, width=200, max_help_position=50)


class JTrader():
    def __init__(self):
        self.parser = ap.ArgumentParser(
            # Here I am settin up the help menu
            description='A tool to run trade strategies on historical price data',
            usage='jtrade [STRATEGY] [PRICE DATA]',
            epilog='Have fun trading!',
            add_help=False,

            # formatter_class needs a callable (a function or class) that will create the formatter instance
            formatter_class=CustomFormatter
        )

        with open('config.json', 'r') as file:
            self.args_config = json.load(file)
        self.setup_parser()

    # Here I am adding the arguments based on the config and assigning them groups (so they show up nice the -h)
    def setup_parser(self):
        general_group = self.parser.add_argument_group("General Options")
        strat_group = self.parser.add_argument_group("Strategy Options")
        price_group = self.parser.add_argument_group("Price Data Options")
        for arg in self.args_config[0:2]:
            # This is automatically unpacking the values in a way that makes them behave as comma-separated arguments!
            general_group.add_argument(*arg['flags'], **arg['kwargs'])
            # The * unpacks the list into separate positional arguments
            # The ** unpacks the dictionary into keyword arguments
        for arg in self.args_config[2:3]:
            strat_group.add_argument(*arg['flags'], **arg['kwargs'])
        for arg in self.args_config[3:]:
            price_group.add_argument(*arg['flags'], **arg['kwargs'])

    def run(self):
        # NOTE: This function below grabs the aguments passed in at the command line and assigns them to args
        args = self.parser.parse_args()

        # Execute the program operations below (doing different things depending on the options selected)
        mv = 0
        if args.mr is True:
            mv += 1
            if args.ticker or args.filename or args.directory:
                self.meanReversionStrategy(tickers=args.ticker, filenames=args.filename, directory=args.directory)
                print("Mean reversion strategy complete")
            else:
                print("Mean reversion strategy description")
                print("Include price data argument to run this strategy on it!")

        # TODO: if next strategy is true, etc etc mv = 1

        # This runs if price data was entered with no strategy
        if mv == 0:
            if args.ticker or args.filename or args.directory:
                if args.ticker:
                    print(f"The ticker(s) you chose is {args.ticker}")
                if args.filename:
                    print(f"The filenames(s) you chose is {args.filename}")
                if args.directory:
                    print(f"The directory you chose is {args.directory}")
            else:
                print("Welcome to JTrader! A project developed by Josh Liddell.\nSee jtrader -h to begin")

            # files = args.filename
            # self.printNames(files)

    def printNames(self, files):
        for name in files:
            print(f'Filename: {name}')

    def meanReversionStrategy(self, tickers=None, filenames=None, directory=None):
        if tickers:
            print("Running the mean reversion strategy on the ticker(s)")
        if filenames:
            print("Running the mean reversion strategy on the file(s)")
        if directory:
            print("Running the mean reversion strategy on the directory")


if __name__ == '__main__':
    # Initialize and run the tool
    JTrader().run()


# If the user runs the script with -a, args.option_a will be True (if action=store_true)
