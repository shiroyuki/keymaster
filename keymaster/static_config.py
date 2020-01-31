import os

CONFIG_ROOT_DIR = os.path.join(os.environ['HOME'], '.spymaster')
LOCAL_STORAGE_FILEPATH = os.path.join(CONFIG_ROOT_DIR, 'local.smpkg')
LOCAL_BASIC_CRYPTOGRAPHIC_KEY_PATH = os.path.join(CONFIG_ROOT_DIR, 'local.basic.smkey')