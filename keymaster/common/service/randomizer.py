import subprocess
from functools import lru_cache
from typing import Callable, Dict, List

from imagination.decorator.service import registered


@registered()
class Randomizer:
    def __init__(self):
        self.__known_generator_map: Dict[str, Callable] = {
            'openssl:base64': self._use_openssl_base64,
            'openssl:hex': self._use_openssl_hex,
        }

    @property
    @lru_cache(maxsize=1)
    def known_methods(self) -> List[str]:
        return sorted(self.__known_generator_map.keys())

    def randomize(self, method: str, length: int):
        if method not in self.__known_generator_map:
            raise UnknownRandomizationMethodError(method)
        return self.__known_generator_map[method](length)

    @staticmethod
    def _use_openssl_base64(length: int) -> str:
        return subprocess.check_output(['openssl', 'rand', '-base64', str(length)]).decode()

    @staticmethod
    def _use_openssl_hex(length: int) -> str:
        return subprocess.check_output(['openssl', 'rand', '-hex', str(length)]).decode()


class UnknownRandomizationMethodError(RuntimeError):
    pass
