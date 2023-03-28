import json


def filtered_executed_operation(filename):
    """фильтрует исполненные (executed) банковские операции из файла operations.json"""

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        filtered_executed = [item for item in data if item.get("state", None) == "EXECUTED"]
        return filtered_executed


def sorted_data_executed_operation(filtered_executed):
    """сортирует последние пять исполненных (executed) банковских операций после функции filtered_executed_operation"""
    sorted_data = sorted(filtered_executed, key=lambda d: d["date"])[-5:-1][::-1]
    return sorted_data



filtered_executed = filtered_executed_operation("operations.json")
sorted_data_executed_operation(filtered_executed)
