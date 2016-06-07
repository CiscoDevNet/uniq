from unittest.mock import MagicMock
import os

import pytest

from uniq.apis.nb.client_manager import NbClientManager
from uniq.apis.exceptions import UniqException


class TestNbClientManager(object):
    """ Tests of nb api client. """

    @pytest.fixture
    def setup_nb_client(self):
        """ Returns faked NbClientManager nb. """

        nb = NbClientManager('1.2.3.4', 'username', 'password', connect=False)
        return nb

    @pytest.fixture
    def setup_nb_client_and_mock(self, setup_nb_client):
        """ Returns faked NbClientManager nb and mocked method 'call_api' """

        nb = setup_nb_client
        mocked_call_api = MagicMock()
        nb.callAPI = mocked_call_api
        return (nb, mocked_call_api)

    def test_v1_only_endpoint_without_api_version(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v1 only endpoints without specifying api version. """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.application.getApplication(id="1")
        mocked_call_api.assert_called_with(
            '/application/1', 'GET', {}, None,
            {'Content-Type': 'application/json', 'Accept': 'application/json'}, files={})

    def test_v1_only_endpoint_with_api_version(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v1 only endpoints with specifying api version. """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.application.getApplication(id="1", api_version='v1')
        mocked_call_api.assert_called_with(
            '/application/1', 'GET', {}, None,
            {'Content-Type': 'application/json', 'Accept': 'application/json'}, files={})

    def test_v1_only_endpoint_raise_exception_when_assigning_v2(self, setup_nb_client_and_mock):
        """ Verifies nb_api raise proper exception when calling v1 only endpoints with specifying
        wrong api version.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock
        with pytest.raises(UniqException) as excinfo:
            nb_api.application.getApplication(id="1", api_version='v2')
        assert (excinfo.value.error_message ==
            "endpoint 'getApplication' doesn't support version 'v2'")

    def test_v2_only_endpoint_without_api_version(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v2 only endpoints without specifying api version. """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.contract.getCount()
        mocked_call_api.assert_called_with(
            '/v2/contract/count', 'GET', {}, None,
            {'Content-Type': 'application/json', 'Accept': 'application/json'}, files={})

    def test_v2_only_endpoint_with_api_version(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v2 only endpoints with specifying api version. """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.contract.getCount(api_version='v2')
        mocked_call_api.assert_called_with(
            '/v2/contract/count', 'GET', {}, None,
            {'Content-Type': 'application/json', 'Accept': 'application/json'}, files={})

    def test_v2_only_endpoint_raise_exception_when_assigning_v1(self, setup_nb_client_and_mock):
        """ Verifies nb_api raise proper exception when calling v2 only endpoints with specifying
        wrong api version.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock
        with pytest.raises(UniqException) as excinfo:
            nb_api.contract.getCount(api_version='v1')
        assert (excinfo.value.error_message ==
            "endpoint 'getCount' doesn't support version 'v1'")

    def test_call_v1_endpoint_when_v1_v2_using_same_name(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v1 endpoints which have both v1 and v2 version and
        their nickname are same.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.add(api_version='v1', scheduleAt='1', scheduleDesc='2',
                          scheduleOrigin='3', policyList={'policy'})
        mocked_call_api.assert_called_with(
            '/policy', 'POST', {'scheduleDesc': '2', 'scheduleOrigin': '3', 'scheduleAt': '1'},
            {'policy'}, {'Accept': 'application/json', 'Content-Type': 'application/json'},
            files={})

    def test_call_v2_endpoint_when_v1_v2_using_same_name(self, setup_nb_client_and_mock):
        """ Verifies nb_api works when calling v2 endpoints which have both v1 and v2 version and
        their nickname are same.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.add(policyDTOs={'new_policy'}, api_version='v2')
        mocked_call_api.assert_called_with(
            '/v2/policy', 'POST', {}, {'new_policy'},
            {'Accept': 'application/json', 'Content-Type': 'application/json'}, files={})

    def test_v1_endpoint_is_default_when_v1_v2_using_same_name(self, setup_nb_client_and_mock):
        """ Verifies v1 endpoints will be called when calling endpoints which have both v1 and v2
        version and their nickname are same.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.add(scheduleAt='1', scheduleDesc='2',
                          scheduleOrigin='3', policyList={'policy'})
        mocked_call_api.assert_called_with(
            '/policy', 'POST', {'scheduleDesc': '2', 'scheduleOrigin': '3', 'scheduleAt': '1'},
            {'policy'}, {'Accept': 'application/json', 'Content-Type': 'application/json'},
            files={})

    def test_call_v1_endpoint_when_v1_v2_using_name_map(self, setup_nb_client_and_mock):
        """ Verifies v1 endpoints can be called properly with v1 original nickname when endpoints
        of v1 and v2 have same url but different nickname.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.get(id='1', api_version='v1')
        mocked_call_api.assert_called_with(
            '/policy/1', 'GET', {}, None,
            {'Accept': 'application/json', 'Content-Type': 'application/json'}, files={})

    def test_call_v2_endpoint_when_v1_v2_using_name_map(self, setup_nb_client_and_mock):
        """ Verifies v1 endpoints can be called properly with v2 original nickname when endpoints
        of v1 and v2 have same url but different nickname.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.getById(id='1', api_version='v2')
        mocked_call_api.assert_called_with(
            '/v2/policy/1', 'GET', {}, None,
            {'Accept': 'application/json', 'Content-Type': 'application/json'}, files={})

    def test_call_v2_endpoint_with_v1_name_when_v1_v2_using_name_map(self,
                                                                     setup_nb_client_and_mock):
        """ Verifies v2 endpoints can be called properly with v1 nickname when endpoints
        of v1 and v2 have same url but different nickname.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.get(id='1', api_version='v2')
        mocked_call_api.assert_called_with(
            '/v2/policy/1', 'GET', {}, None,
            {'Accept': 'application/json', 'Content-Type': 'application/json'}, files={})

    def test_v1_endpoint_is_default_when_v1_v2_using_name_map(self, setup_nb_client_and_mock):
        """ Verifies v1 endpoints can be called properly without specifying api_version when
        endpoints of v1 and v2 have same url but different nickname.
        """

        nb_api, mocked_call_api = setup_nb_client_and_mock

        nb_api.policy.get(id='1')
        mocked_call_api.assert_called_with(
            '/policy/1', 'GET', {}, None,
            {'Accept': 'application/json', 'Content-Type': 'application/json'}, files={})


    @pytest.fixture
    def setup_nb_and_add_faked_models(self, setup_nb_client):
        """ Setup faked NbClientManager and load faked_models for test. """

        nb = setup_nb_client
        nb.add_new_apis(os.path.join(os.path.dirname(os.path.dirname(__file__)), "faked_models"))
        return nb

    def test_two_same_model(self, setup_nb_and_add_faked_models):
        """ Verifies deserialize works if there are two identical models in two clients. """

        nb = setup_nb_and_add_faked_models

        model_obj = nb.deserialize({"name": "name", "id": "id"}, "Same")
        assert model_obj.name == "name" and model_obj.id == "id"

    def test_one_model_contain_another(self, setup_nb_and_add_faked_models):
        """ Verifies deserialize works if there are two models and one is another's subset
        in two clients.
        """

        nb = setup_nb_and_add_faked_models

        model_obj = nb.deserialize({"name": "name", "id": "id"}, "Contain")
        assert model_obj.name == "name" and model_obj.id == "id" and model_obj.contain is None

        model_obj = nb.deserialize({"name": "name", "id": "id", "contain": "contain"}, "Contain")
        assert model_obj.name == "name" and model_obj.id == "id" and model_obj.contain == "contain"

    def test_models_has_diff_attr(self, setup_nb_and_add_faked_models):
        """ Verifies nb client raises proper exception if there are two models have different
        attributes.
        """

        nb = setup_nb_and_add_faked_models
        with pytest.raises(UniqException) as excinfo:
            model_obj = nb.deserialize({"name": "name", "id": "id"}, "DifferentAttr")

        assert excinfo
        assert ("faked_client.models.DifferentAttr.DifferentAttr" in excinfo.value.error_message and
                "other_faked_client.models.DifferentAttr.DifferentAttr"
                in excinfo.value.error_message)

    def test_models_has_diff_type(self, setup_nb_and_add_faked_models):
        """ Verifies nb client raises proper exception if any type of attributes are different
        between two models .
        """

        nb = setup_nb_and_add_faked_models
        with pytest.raises(UniqException) as excinfo:
            model_obj = nb.deserialize({"name": "name", "id": "id"}, "DifferentType")

        assert excinfo
        assert ("faked_client.models.DifferentType.DifferentType" in excinfo.value.error_message and
                "other_faked_client.models.DifferentType.DifferentType"
                in excinfo.value.error_message)