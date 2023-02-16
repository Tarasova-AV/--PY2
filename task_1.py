class Devices:
    """"Класс устройств"""

    exchange_rate = 72.7923  # Курс доллара ЦБ РФ

    base_price = {'Iphone': 799, 'Ipad': 449,
                  'MacBook': 999}  # Минимальная цена базовой модели Iphone 14/Ipad 10/MacBook Air

    DATA_BASE = (  # "Наценка" к базовой стоимости в зависимости от параметров
        {6.1: 0, 6.7: 100, '128GB': 0, '256GB': 100, '512GB': 200},  # Iphone 14/ Iphone 14 Plus
        {'Wi-Fi only': 0, 'cellular': 150, '64GB': 0, '256GB': 150},  # Ipad 10th generation
        {'M1': 0, 'M2': 100, '256GB SSD': 0, '512GB SSD': 300}  # MacBook Air
    )

    def __init__(self, name: str, capacity: int, finish: str):
        self.name = name
        self.capacity = capacity
        self.finish = finish

    def get_price_usd(self) -> int:
        """ Метод для расчета стимости устройства в долларах"""
        ...

    def get_price_rub(self) -> float:
        """ Метод для расчета стимости устройства в рублях"""
        price_rub = self.get_price_usd() * self.exchange_rate
        return round(price_rub)

    def __str__(self):
        return f"Apple {self.name} {self.capacity}GB {self.finish}"

    def __repr__(self):
        return f'("name" = {self.name!r}, "capacity" = {self.capacity!r}, "finish" = {self.finish!r})'

    # Для унификации проверок зададим переменные через свойства
    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        if not isinstance(capacity, int):
            raise TypeError
        if capacity not in [64, 128, 256, 512]:
            raise ValueError
        self._capacity = capacity

    @property
    def finish(self) -> str:
        return self._finish

    @finish.setter
    def finish(self, finish: str) -> None:
        if not isinstance(finish, str):
            raise TypeError
        if finish not in ['blue', 'purple', 'red', 'silver', 'midnight', 'starlight', 'gray', 'gold', 'pink', 'yellow']:
            raise ValueError
        self._finish = finish


class Iphone(Devices):
    """Производный класс. Смартфоны."""

    def __init__(self, name, capacity, finish, display: float):
        super().__init__(name, capacity, finish)
        if display not in [6.1, 6.7]:
            raise ValueError
        self.display = display  # Диагональ смартфона

    def __repr__(self):
        return f'(name = {self.name!r}, capacity = {self.capacity}, finish = {self.finish!r}, display = {self.display})'

    def get_price_usd(self):
        device = 'Iphone' if 'Iphone' in self.name else 'Ipad' if 'Ipad' in self.name else 'MacBook'  # определяем тип
        index = 0 if 'Iphone' in self.name else 1 if 'Ipad' in self.name else 2
        capacity_gb = str(self.capacity) + 'GB'
        price_usd = self.base_price[device] + self.DATA_BASE[index][capacity_gb] + self.DATA_BASE[index][
            self.display]  # к базовой стоимости прибавляем "надбавки"
        return price_usd


class Ipad(Devices):
    """Производный класс. Планшеты."""

    def __init__(self, name, capacity, finish, cellular=None):
        super().__init__(name, capacity, finish)
        if cellular != 'cellular':
            if cellular == None:
                cellular = 'Wi-Fi only'
            else:
                raise ValueError
        self.cellular = cellular  # Наличие симкарты

    def __repr__(self):
        return f'(name= {self.name!r}, capacity= {self.capacity}, finish= {self.finish!r}, cellular= {self.cellular!r})'

    def get_price_usd(self):
        device = 'Iphone' if 'Iphone' in self.name else 'Ipad' if 'Ipad' in self.name else 'MacBook'
        index = 0 if 'Iphone' in self.name else 1 if 'Ipad' in self.name else 2
        capacity_gb = str(self.capacity) + 'GB'
        price_usd = self.base_price[device] + self.DATA_BASE[index][capacity_gb] + self.DATA_BASE[index][self.cellular]
        return price_usd


class MacBook(Devices):
    """Производный класс. Ноутбуки."""

    def __init__(self, name, capacity, finish, chip: str):
        super().__init__(name, capacity, finish)
        if chip not in ['M1', 'M2']:
            raise ValueError
        self.chip = chip  # Линейка процессора

    def __repr__(self):
        return f'(name= {self.name!r}, capacity= {self.capacity}, finish= {self.finish!r}, chip= {self.chip!r})'

    def get_price_usd(self):
        device = 'Iphone' if 'Iphone' in self.name else 'Ipad' if 'Ipad' in self.name else 'MacBook'
        index = 0 if 'Iphone' in self.name else 1 if 'Ipad' in self.name else 2
        capacity_gb = str(self.capacity) + 'GB SSD'
        price_usd = self.base_price[device] + self.DATA_BASE[index][capacity_gb] + self.DATA_BASE[index][self.chip]
        return price_usd


if __name__ == "__main__":
    Iphone1 = Iphone('Iphone 14', 128, 'blue', 6.1)
    Ipad1 = Ipad('Ipad', 64, 'pink', 'cellular')
    Mac1 = MacBook('MacBook Air', 256, 'silver', 'M2')

    print(f'({Iphone1.name}: {Iphone1.get_price_usd()} usd, {Iphone1.get_price_rub()} rub)')
    print(f'({Ipad1.name}: {Ipad1.get_price_usd()} usd, {Ipad1.get_price_rub()} rub)')
    print(f'({Mac1.name}: {Mac1.get_price_usd()} usd, {Mac1.get_price_rub()} rub)')
