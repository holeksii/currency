from .oshchad_driver_starter import OshchadDriverStarter
from .private_driver_starter import PrivatDriverStarter

import json


from info import CURRENCIES
from db.table import Table


def update_all():
    drivers = [OshchadDriverStarter(), PrivatDriverStarter()]

    updated = []
    for currency in CURRENCIES:
        for driver in drivers:
            try:
                table = driver.get_table(currency)
                table.save(f'./resources/{driver.name}_{currency}.csv')
                driver.close_driver()
                updated.append((driver.name, currency))
            except:
                try:
                    driver.close_driver()
                except:
                    pass
                print(f"Помилка при оновленні даних {driver.name} {currency}")
                

    # save updated
    with open('./resources/avaliable.json', 'w') as f:
        json.dump(updated, f)

    return updated
    