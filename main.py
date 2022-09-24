from currency.oshchad_driver_starter import OshchadDriverStarter
from currency.private_driver_starter import PrivatDriverStarter
from plot.privat_plot import show_prices_plot
from plot.linear_regression import *

wds = PrivatDriverStarter()
table = wds.get_table('EUR')
table.merge_date_duplicates()
table.save('./resources/privat_eur.csv')
wds.close_driver()

#show_prices_plot(table)
days = np.array(table.get_days())
prices = np.array(table.get_prices())
k = estimate_coef(days, prices)

plot_regression_line(days, prices, k)


# wds1 = OshchadDriverStarter()
# table1 = wds1.get_table('EUR')
