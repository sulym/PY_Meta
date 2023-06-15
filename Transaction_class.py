class Transaction:
    def __init__(self, amount: int,
                date: str,
                currency: str = "USD",
                usd_conversion_rate: float = 1.0,
                description: str = None
                ) -> None:
        self._amount = amount
        self._date = date
        self._currency = currency
        self._usd_conversion_rate = usd_conversion_rate
        self._description = description

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def date(self) -> str:
        return self._date

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def usd_conversion_rate(self) -> float:
        return self._usd_conversion_rate

    @property
    def description(self) -> str:
        if self._description is None:
            return "No description provided"
        else:
            return self._description
            
    @property
    def usd(self) -> float:
        return self._amount * self._usd_conversion_rate