import os
import subprocess
from argparse import ArgumentParser, Namespace

from gallium import ICommand
from imagination import container

from keymaster.enigma import Enigma
from keymaster.static_config import CONFIG_ROOT_DIR


class LocalInitializer(ICommand):
    "Initialize the local environment"
    def identifier(self):
        return 'local:init'

    def define(self, parser: ArgumentParser):
        pass

    def execute(self, args: Namespace):
        e: Enigma = container.get(Enigma)
        e.setup()
        print('Done')