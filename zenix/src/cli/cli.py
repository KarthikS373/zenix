import argparse


class Cli:

    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description='Zenix command line interface',
        )

        self._parser.add_argument('-y',
                                  '--yes',
                                  action='store_true',
                                  help='Execute code without user confirmation')

        self._parser.add_argument('-f',
                                  '--fast',
                                  action='store_true',
                                  help='Execute faster')

        self._parser.add_argument('-v',
                                  '--verbose',
                                  action='store_true',
                                  help='Verbose output')

        self.args = self._parser.parse_args()

    def get_args(self):
        return self.args
