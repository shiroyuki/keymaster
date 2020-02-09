from imagination.decorator.config import EnvironmentVariable
from imagination.decorator.service import registered

from keymaster.common.service.enigma import Enigma


@registered(params=[
    EnvironmentVariable('KEYMASTER_SERVER_ENIGMA_KEY')
])
class ServerEnigma(Enigma):
    pass
