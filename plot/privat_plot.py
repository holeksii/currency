import matplotlib.pyplot as plt
from db.table import Table

def show_prices_plot(table: Table):
    days = table.get_date()
    prices = table.get_prices()
    currency = table.currency
    name = table.name
    plt.plot(days, prices)
    plt.title(name +" "+ currency + ' prices')
    plt.ylabel('price')
    plt.xlabel('day')
    plt.legend()
    plt.show()
