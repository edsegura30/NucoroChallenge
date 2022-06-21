# Python imports
from typing import Tuple


CurrencyChoice = Tuple[str, str]


class CurrencyCodes:
    CHF = 'CHF'
    EUR = 'EUR'
    GBP = 'GBP'
    USD = 'USD'

    @classmethod
    def get_choices(cls):
        return [
            (cls.CHF, 'Swiss Franc'),
            (cls.EUR, 'Euro'),
            (cls.GBP, 'Pound Sterling'),
            (cls.USD, 'United States Dollar'),
        ]
