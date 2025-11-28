# Import pytest because this file contains fixtures
import pytest

# Import yaml to load configuration files
import yaml


# Fixture to load configuration file (config.yaml)
@pytest.fixture()
def config():
    # Open config.yaml from config folder
    with open("config/config.yaml", "r") as f:

        # Load YAML file content into Python dictionary and return it
        return yaml.safe_load(f)
