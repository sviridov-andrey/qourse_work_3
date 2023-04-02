import time


class OutputTransactions:
    def __init__(self, date=None, amount=None, name=None, description=None, from_=None, to=None):
        self.date = date
        self.amount = amount
        self.name = name
        self.description = description
        self.from_ = from_
        self.to = to

    def date_time(self):
        """формат даты операции"""
        dt = time.strptime(self.date[:10], '%Y-%m-%d')
        return str(time.strftime('%d-%m-%Y', dt))

    def encryption_bank_account(self, number=None):
        """алгоритм шифрования номера счета"""
        return f"{number[:5]}**{number[-6:]}"

    def encryption_bank_card(self, number=None):
        """алгоритм шифрования номера карты"""
        return f"{number[:-12]} {number[-12:-10]}** **** {number[-4:]}"

    def encryption_from(self):
        """выбор алгоритма шифрования отправителя"""
        if "Счет" in self.from_:
            return f'{self.encryption_bank_account(self.from_)} -> '
        elif 'NoValue' in self.from_:
            return f''
        else:
            return f'{self.encryption_bank_card(self.from_)} -> '

    def encryption_to(self):
        """выбор алгоритма шифрования получателя"""
        if "Счет" in self.to:
            return self.encryption_bank_account(self.to)
        else:
            return self.encryption_bank_card(self.to)

    def __repr__(self):
        return (f'OutputTransactions, {self.date}, {self.description}, {self.from_}, '
                f'{self.to}, {self.amount}, {self.name}')
