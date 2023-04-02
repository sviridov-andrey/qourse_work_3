import json
from classes import OutputTransactions


def open_json_file(filename):
    """открывает файл operations.json"""

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def filtered_executed_transactions(data):
    """фильтрует исполненные (executed) банковские операции после результата функции open_json_file"""

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
