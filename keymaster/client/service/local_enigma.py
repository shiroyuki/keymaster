from keymaster.common.service.enigma import Enigma

from imagination.decorator.service import registered


@registered()
class LocalEnigma(Enigma):
    pass
