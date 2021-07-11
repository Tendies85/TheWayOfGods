from dataclasses import dataclass

import typing as t


@dataclass
class Avatar:
    name: str
    _health: float
    _money: float
    _food: float
    _follower: int

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, x):
        if x > 100:
            self._health = 100
        elif x < 0:
            self._health = 0
        else:
            self._health = x

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, x):
        if x > 25:
            self._food = 25
        elif x < 0:
            self._health = 0
        else:
            self._health = x

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, x):
        self._money = x

    @property
    def follower(self):
        return self._follower

    @follower.setter
    def follower(self, x):
        self._follower = x



@dataclass
class Health:
    value: int

    def __str__(self):
        return f"{self.value}\u2665"


@dataclass
class Choice:
    text: str
    values: dict

    def __str__(self):
        value = ""
        if 'health' in self.values:
            value += f"{self.values['health']}♥ "
        if 'follower' in self.values:
            value += f"{self.values['follower']}🙏 "
        if 'food' in self.values:
            value += f"{self.values['food']}🍎 "
        if 'money' in self.values:
            value += f"{self.values['money']}💰 "

        return f"{self.text} \n\t{value}"

@dataclass
class Question:
    text: str
    choices: t.List[Choice]
    result: Choice = None
