import os, sys
sys.path.insert(0, os.path.join(os.getcwd(), '..', 'Imagination'))
sys.path.insert(0, os.path.join(os.getcwd(), '..', 'xmode'))
from keymaster.starter import activate

activate()