from datetime import datetime
from .row import Row

class Table:
    def __init__(self, _rows: list, name : str, currency : str) -> None:
        self.rows = _rows
        self.name = name
        self.currency = currency


    def text(self) -> str:
        str = 'date,from_,to,buy,sell\n'
        for row in self.rows:
            str += row.text() + '\n'
        return str
    

    def merge_date_duplicates(self):
        rows = []
        for row in self.rows:
            
            to_merge = []
            for row_ in self.rows:
                if row.date == row_.date:
                    to_merge.append(row_)

            avg_buy = 0
            avg_sell = 0
            for row_ in to_merge:
                avg_buy += row_.buy
                avg_sell += row_.sell
            avg_buy /= len(to_merge)
            avg_sell /= len(to_merge)
            rows.append(Row(row.date, row.from_, row.to, avg_buy, avg_sell))
                                
        self.rows = rows


    def save(self, path: str):
        with open(path, 'w') as file:
            file.write(self.text())

    def get_date(self) -> list:
        days = []
        for row in self.rows:
            days.append(row.date)
        return days

    def get_days(self) -> list:
        days = []
        for row in self.rows:
            d = row.date
            days.append(d.timestamp())
        return days

    def get_prices(self) -> list:
        prices = []
        for row in self.rows:
            prices.append(row.buy)
        return prices

    def get_currency(self) -> str:
        return self.rows[0].to

    