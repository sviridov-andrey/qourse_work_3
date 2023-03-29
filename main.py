from utils import (filtered_executed_transactions, sorted_data_executed_transactions,
                  add_last_five_transactions, output_last_five_transactions)

if __name__ == '__main__':

    filtered_executed = filtered_executed_transactions("operations.json")
    sorted_data = sorted_data_executed_transactions(filtered_executed)
    last_five_transactions = add_last_five_transactions(sorted_data)до
    output_last_five_transactions = output_last_five_transactions(last_five_transactions)
