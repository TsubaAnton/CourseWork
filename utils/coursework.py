import json
from datetime import datetime


def read_operations(filename):
    """Читает данные операций из json-файла"""
    with open(filename, 'r', encoding='utf-8') as file:
        operations_data = json.load(file)
    return operations_data


def format_operation(operation):
    """Форматирует операцию в необходимую для вывода строку"""
    formatted_date = datetime.strptime(operation['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%y")
    if 'from' in operation:
        card_info = operation['from'].split(' ')
        card_name = card_info[0]
        masked_card_number = f"{card_name} {card_info[1][:4]} {card_info[1][4:8]} {card_info[1][8:12]} {card_info[1][12:]}".replace('*', 'x')
    else:
        masked_card_number = ''
    masked_account_number = f"**{operation['to'][-4:]}" if 'to' in operation else ''
    formatted_operation = (
        f"{formatted_date} {operation['description']}\n"
        f"{masked_card_number} -> Счет {masked_account_number}\n"
        f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}"
    )
    return formatted_operation + '\n'


def display_last_operations(operations_data):
    """Выводит информацию о 5 последних операциях"""
    executed_operations = sorted(
        filter(lambda op: op.get('state') == 'EXECUTED', operations_data),
        key=lambda op: datetime.strptime(op['date'], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=True
    )[:5]


"""Получаем библиотеку json"""
filename = '../operations.json'
operations_data = read_operations(filename)
print(display_last_operations(operations_data))
