import json


def filtered_executed_operation(filename):
    """фильтрует исполненные (executed) банковские операции из файла operations.json"""

    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        filtered_executed = [item for item in data if item.get("state", None) == "EXECUTED"]
        return filtered_executed



filtered_executed_operation("operations.json")
