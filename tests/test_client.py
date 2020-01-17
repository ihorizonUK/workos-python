import pytest

from workos import client
from workos.exceptions import ConfigurationException

class TestClient(object):
    @pytest.fixture(autouse=True)
    def setup(self):
        client._sso = None

    def test_initialize_sso(self, set_api_key_and_project_id):
        assert bool(client.sso)

    def test_initialize_sso_missing_api_key(self, set_project_id):
        with pytest.raises(ConfigurationException) as ex:
            client.sso

        message = str(ex)

        assert 'api_key' in message
        assert 'project_id' not in message

    def test_initialize_sso_missing_project_id(self, set_api_key):
        with pytest.raises(ConfigurationException) as ex:
            client.sso
        
        message = str(ex)

        assert 'project_id' in message
        assert 'api_key' not in message
    
    def test_initialize_sso_missing_api_key_and_project_id(self):
        with pytest.raises(ConfigurationException) as ex:
            client.sso

        message = str(ex)

        assert all(setting in message for setting in ('api_key', 'project_id',))