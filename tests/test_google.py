from unittest import mock
import google_api
import facebook_api


def test_google(mocker):
    mocker.patch('google_api.get_data', return_value='data_1')
    mocker.patch('facebook_api.get_data', return_value='data_1')
    assert google_api.get_data() == 'data_1'
    assert facebook_api.get_data() == 'data_1'
