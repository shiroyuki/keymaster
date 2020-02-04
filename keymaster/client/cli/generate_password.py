from gallium.interface import ICommand, alias
from imagination import container

from keymaster.common.service.randomizer import Randomizer


@alias('rand')
class GeneratePassword(ICommand):
    """Generate a password"""

    def __init__(self):
        self.__randomizer: Randomizer = container.get(Randomizer)

    def identifier(self):
        return 'generate:password'

    def define(self, parser):
        parser.add_argument('--method', '-m',
                            help=f'randomization method {self.__randomizer.known_methods} -- default to the first one',
                            default=self.__randomizer.known_methods[0],
                            required=False)
        parser.add_argument('--length', '-l',
                            type=int,
                            help='password length',
                            default=12,
                            required=False)

    def execute(self, args):
        print(self.__randomizer.randomize(args.method, args.length))
