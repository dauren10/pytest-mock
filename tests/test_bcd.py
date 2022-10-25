from unittest.mock import patch
from mockaroo import parse

@patch('mockaroo.fetch_net')
def test_parse_fom_fetch_net(mock_get):
    mock_get.return_value = 'def'
    assert parse() == 'def123'
