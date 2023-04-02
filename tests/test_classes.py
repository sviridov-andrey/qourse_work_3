from classes import OutputTransactions


def test_date_time():
    output_transactions = OutputTransactions(date="2018-12-28T23:10:35.459698")
    assert output_transactions.date_time() == "28-12-2018"


def test_encryption_bank_account():
    output_transactions = OutputTransactions()
    assert output_transactions.encryption_bank_account(number="Счет 96231448929365202391") == "Счет **202391"


def test_encryption_bank_card():
    output_transactions = OutputTransactions()
    assert output_transactions.encryption_bank_card(number="Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_encryption_from():
    output_transactions = OutputTransactions(from_="Счет 64686473678894779589")
    assert output_transactions.encryption_from() == "Счет **779589 -> "
    output_transactions = OutputTransactions(from_="NoValue")
    assert output_transactions.encryption_from() == ""
    output_transactions = OutputTransactions(from_="MasterCard 7158300734726758")
    assert output_transactions.encryption_from() == "MasterCard 7158 30** **** 6758 -> "


def test_encryption_to():
    output_transactions = OutputTransactions(to="Счет 64686473678894779589")
    assert output_transactions.encryption_to() == "Счет **779589"
    output_transactions = OutputTransactions(to="MasterCard 7158300734726758")
    assert output_transactions.encryption_to() == "MasterCard 7158 30** **** 6758"
