from dnd import attack_damage
from unittest import mock


@mock.patch("dnd.randint", return_value=5, autospec=True)
def test_attack_damage(mock_randint):
    assert attack_damage(1) == 6
    mock_randint.assert_called_once_with(1,8)#был ли вызов функции assert_called
    
