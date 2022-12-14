# Копилка
from typing import Union

class PiggyBank:
    def __init__(self, number_of_coins: int, amount_of_money: Union[int, float], capacity_volume: int):
        """
        Создание и подготовка к работе объекта "Копилка"
        :param number_of_coins: Количество монет
        :param amount_of_money: Накопленная сумма денег
        :param capacity_volume: Объем копилки (в монетах)
        Примеры:
        >>> piggybank = PiggyBank(500, 700, 1000)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_coins, int):
            raise TypeError("Количество монет должно быть типа int")
        if number_of_coins <= 0:
            raise ValueError("Количество монет должно быть положительным числом")
        self.number_of_coins = number_of_coins
        
        if not isinstance(amount_of_money, (int, float)):
            raise TypeError("Накопленная сумма должна быть float или int")
        if amount_of_money <= 0:
            raise ValueError("Накопленная сумма должна быть положительным числом")
        self.amount_of_money = amount_of_money

        if not isinstance(capacity_volume, int):
            raise TypeError("Объем копилки должен быть int")
        if ocapacity_volume < 0:
            raise ValueError("Объем копилки не может быть отрицательным числом")
        self.capacity_volume = capacity_volume
        
        def add_coins_to_piggybank(self, added_coins: int, added_amount: Union[int, float]) -> None:
        """
        Добавление монет в копилку.
        :param added_coins: Количество добавляемых монет
        :param added_amount:Сумма добавляемых монет
        :raise ValueError: Если количество добавляемых монет превышает свободное место в копилке, то вызываем ошибку
        Примеры:
        >>> piggybank = PiggyBank(500, 700, 1000)
        >>> piggybank.add_coins_to_piggybank(10, 200)
        """
        if not isinstance(added_coins, int):
            raise TypeError("Количество добавляемых монет должно быть типа int")
        if added_coins < 0:
            raise ValueError("Количество добавляемых монет должно быть положительным числом")
            
        if not isinstance(added_amount, (int, float)):
            raise TypeError("Сумма добавляемых монет должна быть типа int или float")
        if added_amount < 0:
            raise ValueError("Сумма добавляемых монет должна быть положительным числом")
        ...
        
        def break_piggybank(self) -> None:
        """
        Разбить копилку. Выводит накопленную сумму и количество монет.
        Примеры:
        >>> piggybank = PiggyBank(500, 700, 1000)
        >>> piggybank.break_piggybank()
        """
        ...
        
        def occupied_piggybank(self) -> None:
        """
        Процент заполнения копилки.
        Примеры:
        >>> piggybank = PiggyBank(500, 700, 1000)
        >>> piggybank.occupied_piggybank()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации


# Депозит

from typing import Union


class Deposit:
    def __init__(self, deposit_amount: Union[int, float], rate: Union[int, float], period: int):
        """
        Создание и подготовка к работе объекта "Депозит"
        :param deposit_amount: Сумма депозита
        :param rate: Процентная ставка годовых
        :param period: Срок депозита (в днях)
        Примеры:
        >>> deposit = Deposit(500000, 7.5, 30)  # инициализация экземпляра класса
        """
        if not isinstance(deposit_amount, (int, float)):
            raise TypeError("Сумма депозита должна быть типа float или int")
        if deposit_amount <= 0:
            raise ValueError("Сумма депозита должна быть положительным числом")
        self.deposit_amount = deposit_amount
        
        if not isinstance(rate, (int, float)):
            raise TypeError("Ставка должна быть float или int")
        if 100 < rate <= 0:
            raise ValueError("Ставка должна быть больше 0, но меньше 100")
        self.rate = rate

        if not isinstance(period, int):
            raise TypeError("Срок должен быть int")
        if period < 0:
            raise ValueError("Срок не может быть отрицательным числом") # Надо продумать какой максимальный
        self.period = period
        
        def replenish_deposit(self, added_sum: Union[int, float]) -> None:
        """
        Пополнение депозита.
        :param added_sum: Сумма пополнения
        Примеры:
        >>> deposit = Deposit(500000, 7.5, 30)
        >>> deposit.replenish_deposit(20000)
        """
        if not isinstance(added_sum, (int, float)):
            raise TypeError("Сумма пополнения должна быть типа int или float")
        if added_sum < 0:
            raise ValueError("Сумма пополнения должна быть положительным числом")
            
        ...
        
        def partial_withdrawal(self, withdrawal_sum: Union[int, float]) -> None:
        """
        Частичное востребование депозита.
        :param withdrawal_sum: Сумма истребования
        :raise ValueError: Если сумма истребования превышает минимальный остаток, то вызываем ошибку
        Примеры:
        >>> deposit = Deposit(500000, 7.5, 30)
        >>> deposit.replenish_deposit(100000)
        """
        if not isinstance(withdrawal_sum, (int, float)):
            raise TypeError("Сумма истребования должна быть типа int или float")
        if withdrawal_sum < 0:
            raise ValueError("Сумма истребования должна быть положительным числом")
            
        ...
        
        def prematured_deposit(self, actual_period: int) -> None:
        """
        Досрочное закрытие депозита.
        :param actual_period: Фактический срок депозита
        :param rate = 0.01: Ставка при досрочном закрытии депозита
        :raise ValueError: Если фактический срок превышает срок по договору, то вызываем ошибку
        Примеры:
        >>> deposit = Deposit(500000, 7.5, 30)
        >>> deposit.prematured_deposit(15)
        """
        if not isinstance(actual_period, int):
            raise TypeError("Фактический срок депозита должен быть типа int")
        if actual_period < 0:
            raise ValueError("Фактический срок должен быть положительным числом")
            
        ...
        
        def closing_deposit(self) -> None:
        """
        Закрытие депозита по сроку.
        :param interest_of_savings: Сумма начисленных процентов
        Примеры:
        >>> deposit = Deposit(500000, 7.5, 30)
        >>> deposit.closing_deposit()
        """
            
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
                       #сумма, срок, ставка %годовых
                       #пополнение, частичное истребование, сумма ожидаемых процентов



# Пекарня

class Bakery:
    def __init__(self, snowman: int, christmas_tree: int, ):
        """
        Создание и подготовка к работе объекта "Пекарня"
        :param snowman: Количество пряников в виде снеговика
        :param christmas_tree: Количество пряников в виде елочек
        Примеры:
        >>> order = Bakery(10, 20)  # инициализация экземпляра класса
        """
        if not isinstance(snowman, int):
            raise TypeError("Количество снеговиков должно быть типа int")
        if snowman <= 0:
            raise ValueError("Количество снеговиков должно быть положительным числом")
        self.snowman = snowman

        if not isinstance(christmas_tree, int):
            raise TypeError("Количество елочек должно быть типа int")
        if christmas_tree < 0:
            raise ValueError("Количество елочек должно быть положительным числом")
        self.christmas_tree = christmas_tree
        
        def change_order(self, added_snowmans: int, added_christmas_tree: int) -> None:
        """
        Изменение количества пряников соответствующего типа в заказе.
        :param added_snowmans: Количество добавляемых (убираемых) снеговиков
        :param added_christmas_tree:Количество добавляемых (убираемых) елочек
        :raise ValueError: Если количество убираемых позиций превышает количетсво пряников в заказе, то вызываем ошибку
        Примеры:
        >>> order_bakery = Bakary(10, 15)
        >>> order_bakery.change_order(-1, 2)
        """
        if not isinstance(added_snowmans, int):
            raise TypeError("Количество добавляемых снеговиков должно быть типа int")
            
        if not isinstance(added_christmas_tree, (int, float)):
            raise TypeError("Сумма добавляемых елочек должна быть типа int")

        ...
        
        def order_cost(self) -> None:
        """
        Посчитать стоимость заказа.
        :param snowman_cost: Стоимость пряника в виде снеговика
        :param christmas_tree_cost: Стоимость пряника в виде елочки
        Примеры:
        >>> order_bakery = Bakary(10, 15)
        >>> order_bakery.order_cost()
        """
        ...

if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации

