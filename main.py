from utils import filtered_executed_transactions, sorted_data_executed_transactions

if __name__ == '__main__':

    filtered_executed = filtered_executed_transactions("operations.json")
    sorted_data_executed_transactions(filtered_executed)
