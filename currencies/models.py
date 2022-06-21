# Pip imports
from django.db import models

# Internal imports
from currencies.constants import CurrencyCodes


class Currency(models.Model):
    """Contains information about a currency."""
    code = models.CharField(
        choices=CurrencyCodes.get_choices(),
        max_length=3,
        unique=True,
    )
    name = models.CharField(db_index=True, max_length=20)
    symbol = models.CharField(max_length=10)


    def __str__(self):
        return f'{self.code} ({self.symbol})'


class CurrencyExchangeRate(models.Model):
    """
    Tracks data required to perform conversions between different currencies.
    """
    exchanged_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
    )
    rate_value = models.DecimalField(
        db_index=True,
        decimal_places=6,
        max_digits=18,
    )
    source_currency = models.ForeignKey(
        Currency,
        related_name='exchanges',
        on_delete=models.CASCADE,
    )
    valuation_date = models.DateField(db_index=True)

    def __str__(self):
        return (
            f'{self.valuation_date.strftime("%d/%m/%Y")}: '
            f'{self.source_currency.code} -> {self.exchanged_currency.code}'
        )
