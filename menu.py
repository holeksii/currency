import json
from currency.update_all import update_all
from plot.table_plot import show_prices_plot
from plot.linear_regression import show_prices_plot_linear
from db.table import Table


menu_msg = '''оберіть дію:
1. оновити дані
2. вивести графік курсу
3. вивести графік курсу з прогнозом
q. вийти'''


def menu_loop():
    choice = None
    avaliable = []
    # open avaliable.json
    try:
        with open('./resources/avaliable.json', 'r') as f:
            avaliable = json.load(f)
    except:
        pass

    while choice != 'q':
        print(menu_msg)
        choice = input(">>").lower().strip()
        if choice == 'q':
            print("До побачення!")
        if choice == '1':
            print("Оновлення даних...")
            avaliable = update_all()
            print("Дані оновлені!")
        if choice == '2':
            print("Оберіть валюту:")
            for i, (driver, currency) in enumerate(avaliable):
                print(f'{i+1}. {driver} {currency}')
            if len(avaliable) == 0:
                print("Дані відсутні!")
                continue
            choice = int(input(">>")) - 1
            driver, currency = avaliable[choice]
            print(f'Ви обрали {driver} {currency}')
            table = Table.load(f'./resources/{driver}_{currency}.csv', driver, currency)
            show_prices_plot(table)
        if choice == '3':
            print("Оберіть валюту:")
            for i, (driver, currency) in enumerate(avaliable):
                print(f'{i+1}. {driver} {currency}')
            
            if len(avaliable) == 0:
                print("Дані відсутні!")
                continue

            choice = int(input(">>")) - 1
            driver, currency = avaliable[choice]
            print(f'Ви обрали {driver} {currency}')
            table = Table.load(f'./resources/{driver}_{currency}.csv', driver, currency)
            show_prices_plot_linear(table)
           
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    menu_loop()