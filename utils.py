import json
from classes import OutputTransactions


def filtered_executed_transactions(filename):
    """фильтрует исполненные (executed) банковские операции из файла operations.json"""

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        filtered_executed = [item for item in data if item.get("state", None) == "EXECUTED"]
        return filtered_executed


def sorted_data_executed_transactions(filtered_executed):
    """сортирует последние пять исполненных (executed) банковских операций
    после функции filtered_executed_operation"""
    sorted_data = sorted(filtered_executed, key=lambda d: d["date"])[-5:][::-1]
    return sorted_data


def add_last_five_transactions(sorted_data):
    """получает данные после функции sorted_data_executed_transactions для обработки классом OutputTransactions"""
    last_five_transactions = [OutputTransactions(i['date'], i['operationAmount']['amount'],
                                                 i['operationAmount']['currency']['name'],
                                                 i['description'], i.setdefault('from', 'NoValue'), i['to'] )
                              for i in sorted_data]
    return last_five_transactions


def output_last_five_transactions(last_five_transactions):
    """выводит обработанные данные последних пяти банковских операций"""

    for i in last_five_transactions:
        print(f'\n{i.date_time()}  {i.description}\n'
              f'{i.encryption_from()}{i.encryption_to()}\n'
              f'{i.amount} {i.name}'
              )
