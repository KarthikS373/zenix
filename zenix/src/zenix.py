from zenix.src.utils import *
from zenix.src.cli import cli

class Zenix:

    def __init__(self):
        self.model = "llama"
        self.messages = []
        self.temperature = 0.001

        self.debug = False
