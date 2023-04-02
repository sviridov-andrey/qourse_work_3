from utils import (filtered_executed_transactions, sorted_data_executed_transactions,
                  add_last_five_transactions, open_json_file)

if __name__ == '__main__':
    data = open_json_file("operations.json")
    filtered_executed = filtered_executed_transactions(data)
    sorted_data = sorted_data_executed_transactions(filtered_executed)
    last_five_transactions = add_last_five_transactions(sorted_data)

    for i in last_five_transactions:
        print(f'\n{i.date_time()} {i.description}\n'
              f'{i.encryption_from()}{i.encryption_to()}\n'
              f'{i.amount} {i.name}'
              )
