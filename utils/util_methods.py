import os

import yaml


def read_config():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_path = os.path.join(base_dir, 'config.yaml')

    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config