from classes import OutputTransactions
from utils import open_json_file, filtered_executed_transactions, sorted_data_executed_transactions, \
    add_last_five_transactions


def test_open_json_file():
    data = open_json_file("test_operations.json")
    assert len(data) == 101
    assert isinstance(data, list)


def test_filtered_executed_transactions(test_data):
    data = filtered_executed_transactions(test_data)
    assert [i["state"] for i in data[:2] if i.get("state", None)] == ['EXECUTED', 'EXECUTED']
    assert len(filtered_executed_transactions(test_data)) == 6


def test_sorted_data_executed_transactions(test_data_2):
    data = sorted_data_executed_transactions(test_data_2)
    assert [i["date"] for i in data[:3]] == ['2019-07-03T18:35:29.512364', '2019-04-04T23:20:05.206878',
                                             '2019-03-23T01:09:46.296404']


def test_add_last_five_transactions(test_data_2):
    data = add_last_five_transactions(test_data_2)
    assert str(data[:3]) == (f'[OutputTransactions, 2018-12-28T23:10:35.459698, Открытие вклада, NoValue, '
    f'Счет 96231448929365202391, 49192.52, USD, OutputTransactions, '
    f'2019-07-03T18:35:29.512364, Перевод организации, MasterCard '
    f'7158300734726758, Счет 35383033474447895560, 8221.37, USD, '
    f'OutputTransactions, 2018-06-30T02:08:58.425572, Перевод организации, Счет '
    f'75106830613657916952, Счет 11776614605963066702, 9824.07, USD]')
