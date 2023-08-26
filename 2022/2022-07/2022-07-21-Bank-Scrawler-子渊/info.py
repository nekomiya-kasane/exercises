from sqlite3 import Date
from numpy import integer, number
from datetime import date

class company_info:
    name: str = ""
    shareholder: str = ""
    shareholder_ratio: float = -1
    ex_shareholder: str = ""
    shareholder_renew_time: date = date(1970, 1, 1)
    capital_now: list[float] = []
    branches_now: list[float] = []


class shareholder_info:
    name: str = ""
    capital: float = 0
    ratio: float = 0
    time: date = date(1970, 1, 1)

class history_info_item:
    index: integer = -1
    time: date = date(1970, 1, 1)
    before: str = ""
    after: str = ""

class history_info:
    infos: list[history_info_item] = []

    def append(self, item: history_info_item):
        self.infos.insert(item.index - 1, item)

    def get_branches_info(self, years: integer = 1):
        pass

    def get_capital_info(self, years: integer = 1):
        pass
