import sys
from abc import ABC, abstractmethod
from argparse import ArgumentParser, Namespace
from functools import lru_cache


class InlineParser(ArgumentParser):
    def exit(self, status=0, message=None):
        if message:
            sys.stderr.write(f'ERROR: {message}\n')
        raise InlineError(message)

    def error(self, message):
        self.print_usage(sys.stderr)
        self.exit(2, f'{self.prog} {message}')


class InlineError(RuntimeError):
    pass


class InlineRuntimeError(RuntimeError):
    pass


class List(object):
    pass


class SubCommand(ABC):
    @abstractmethod
    def get_aliases(self) -> List:
        ...

    @abstractmethod
    def get_parser(self) -> InlineParser:
        ...

    @abstractmethod
    def run(self, args: Namespace):
        ...

    @lru_cache(maxsize=1)
    def _make_parser(self) -> InlineParser:
        return InlineParser(self.get_aliases()[0], description=self.__doc__.strip())
