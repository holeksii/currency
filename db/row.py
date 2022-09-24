from datetime import datetime


class Row:
    def __init__(self, _date: datetime, _from: str, _to: str, _buy: float, _sell: float) -> None:
        if type(_date) == str:
            # format  11-11-1111
            self.date = datetime(int(_date[6:]), int(_date[3:5]), int(_date[:2]))
        elif type(_date) == datetime:
            self.date = _date
        else:
            raise ValueError('date must be str or date!')
        
        self.from_= str(_from)
        self.to = str(_to)
        self.buy = float(_buy)
        self.sell = float(_sell)

    def text(self) -> str:
        date = self.date.strftime('%d-%m-%Y')
        return f'{date},{self.from_},{self.to},{self.buy},{self.sell}'

