#!/home/joshua/.venv/bin/python3
import json
from customformats import CustomArgParser


class JTrader():
    def __init__(self):
        self.parser = CustomArgParser(
            # Here I am settin up the help menu
            description='A tool to run trade strategies on historical price data',
            usage='jtrader [STRATEGY] [PRICE DATA] [OUTPUT OPTION]',
            epilog='Have fun trading!',
            add_help=False,
            allow_abbrev=False
        )

        with open('config.json', 'r') as file:
            self.args_config = json.load(file)
        self.setup_parser()

    # Here I am adding the arguments based on the config and assigning them groups (so they show up nice the -h)
    def setup_parser(self):
        groups = {
            "general": self.parser.add_argument_group("General Options"),
            "strategy": self.parser.add_argument_group("Strategy Options"),
            "price": self.parser.add_argument_group("Price Data Options"),
            "output": self.parser.add_argument_group("Output Options")
        }

        for key, group in groups.items():
            for arg in self.args_config[key]:
                group.add_argument(*arg['flags'], **arg['kwargs'])
                # This is automatically unpacking the values in a way that makes them behave as comma-separated arguments!
                # The * unpacks the list into separate positional arguments
                # The ** unpacks the dictionary into keyword arguments

    def run(self):
        # NOTE: This function below grabs the aguments passed in at the command line and assigns them to args
        args = self.parser.parse_args()
        strategies = [args.mr, args.sma]
        pricedata = [args.ticker, args.filename, args.directory]

        # Execute the program operations below (doing different things depending on the options selected)

        # NOTE: First check if there is price data, if so get the ticker data, validate files selected, then move on to checking what strategy(s) was selected and run it on the data
        if any(pricedata):
            validated, data = self.prepareData(args.ticker, args.filename, args.directory)
            if validated is True:
                if any(strategies):
                    if args.mr is True:
                        self.meanReversion(data)
                    if args.sma is True:
                        self.simpleMovingAverage(data)
                else:
                    if args.ticker:
                        print(f"The valid ticker(s) you chose is {args.ticker}")
                    if args.filename:
                        print(f"The valid filenames(s) you chose is {args.filename}")
                    if args.directory:
                        print(f"The directory you chose is {args.directory}")
                    print("Include a strategy option to run it on this data")

            else:
                print('There was an error validating/preparing your data')

        # NOTE: Then if no price data check if a strategy was entered, if so explain the strategy
        else:
            if any(strategies):
                if args.mr is True:
                    print("Mean reversion strategy description")
                    print("Include a price data argument to run this strategy on it!\n")
                if args.sma is True:
                    print("Simple moving average strategy description")
                    print("Include a price data argument to run this strategy on it!\n")

            # If there was no price data or strategies entered then:
            else:
                print("Welcome to JTrader! A project developed by Josh Liddell.\nSee jtrader -h to begin")

    # TODO: Make this func validate the data
    def prepareData(self, tickers, files, directory):
        data = []
        # If at any point something goes wrong change it to false (I think I wont let it run unless all the data is good)
        validated = True
        if tickers:
            # call the api get the data and add it to data.
            for t in tickers:
                data.append(t)
        if files:
            # Validate the file
            for f in files:
                data.append(f)
        if directory:
            # For each file in directory if its good append it
            data.append(directory)

        return validated, data

    def meanReversion(self, data):
        print(f"Running the mr strategy on {data}")

    def simpleMovingAverage(self, data):
        print(f"Running the sma strategy on {data}")


if __name__ == '__main__':
    # Initialize and run the tool
    JTrader().run()
