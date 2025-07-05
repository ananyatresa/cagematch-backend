import os

import yaml


def read_config():
    # Get the directory where the current script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)

    file_path = os.path.join(parent_dir, "config.yaml")

    with open(file_path,'r') as file:
        config = yaml.safe_load(file)
    return config