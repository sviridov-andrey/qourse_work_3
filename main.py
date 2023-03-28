from utils import filtered_executed_operation, sorted_data_executed_operation

if __name__ == '__main__':

    filtered_executed = filtered_executed_operation("operations.json")
    sorted_data_executed_operation(filtered_executed)
