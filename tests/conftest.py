import pytest, json
from framework.storage_client import StorageClient

@pytest.fixture(scope="session")
def storage_config():
    with open("config/storage_config.json") as file:
        return json.load(file)

@pytest.fixture(scope="session")
def storage_client(storage_config):
    client = StorageClient(storage_config["server"]["host"],storage_config["server"]["username"],storage_config["server"]["password"])
    yield client
    client.close()
