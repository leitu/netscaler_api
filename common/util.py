import re
import yaml
import logging
import logging.config

# def netapp_size(value):
#   match = re.search('^(\d+)([kmgtpezyKMGTPEZY]?)$', str(value))
#   if match:
#     return match.group(0)
#   else:
#     raise ValueError('Not a valid size descriptor')

def initialize_logging(config_file):
  config = yaml.load(open(config_file, 'r'))
  logging.config.dictConfig(config)
