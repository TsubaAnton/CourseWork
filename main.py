import json
from datetime import datetime


def read_operations(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data


def format_operation(operation):
    formatted_date = datetime.strptime(operation['date'], "%d.%m.%y").strftime("%d.%m.%y")
    masked_card_number = f"{operation['from'][:6]} xx** **** {operation['from'][-4:]}" if 'from' in operation else ''
    masked_account_number = f"**{operation['to'][-4:]}" if 'to' in operation else ''

    formatted_operation = (
        f"{formatted_date} {operation['description']}\n"
        f"{masked_card_number} -> счет {masked_account_number}\n"
        f"{operation['operationamount']['amount']} {operation['operationamount']['currency']}"
    )

    return formatted_operation





# пример использования
filename = 'operations.json'  # укажите путь к файлу с операциями
operations_data = read_operations(filename)
#display_last_operations(operations_data)
