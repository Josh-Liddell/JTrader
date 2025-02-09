import argparse as ap
import json


class JTrader():
    def __init__(self):
        self.parser = ap.ArgumentParser(description='A tool to run trade strategies on historical data')
        with open('config.json', 'r') as file:
            self.args_config = json.load(file)
        self.setup_parser()

    def setup_parser(self):
        for arg in self.args_config:
            # This is automatically unpacking the values in a way that makes them behave as comma-separated arguments!
            self.parser.add_argument(*arg['flags'], **arg['kwargs'])
            # The * unpacks the list into separate positional arguments
            # The ** unpacks the dictionary into keyword arguments

    def run(self):
        args = self.parser.parse_args()

        # Execute the program operations below (doing different things depending on what was entered of course)
        files = args.filename
        self.printNames(files)

    def printNames(self, files):
        for name in files:
            print(f'Filename: {name}')


if __name__ == '__main__':
    JTrader().run()
