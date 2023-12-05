from utils.coursework import format_operation, display_last_operations


def test_format_operation():
    """Тест функции format_operation"""
    operation_1 = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    operation_2 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Visa 7158300734726758",
        "to": "Счет 35383033474447895560"
    }

    expected_result_1 = ("26.08.19 Перевод организации\n"
                         "Maestro 1596 8378 6870 5199 -> Счет **9589\n"        
                         "31957.58 руб.\n")
    expected_result_2: str = ("03.07.19 Перевод организации\n"
                         "Visa 7158 3007 3472 6758 -> Счет **5560\n"     
                         "8221.37 USD\n")

    assert format_operation(operation_1) == expected_result_1
    assert format_operation(operation_2) == expected_result_2


def test_display_last_operations(capsys):
    """Тест функции display_last_operations"""
    operations_data = [
        {"id": 1, "date": "2022-01-01T12:00:00.000000", "state": "EXECUTED",
         "operationAmount": {"amount": "100", "currency": {"name": "USD"}}},
    ]

    display_last_operations([])
    captured = capsys.readouterr()
    assert captured.out == ""
