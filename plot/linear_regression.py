from datetime import datetime, timedelta
import numpy as np 
import matplotlib.pyplot as plt 

  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 

    # mean of x and y vector 
    m_x = np.mean(x) 
    m_y = np.mean(y) 

    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 

    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 

    return (b_0, b_1) 

  

def plot_regression_line(days, y, b, currency, name): 
    X = []
    Y = []
    for i in range(len(days)):
        X.append(datetime.fromtimestamp(days[i]))
        Y.append(y[i])

    for i in range(len(days)):
        X.append(X[-1]+ timedelta(days=1))
        Y.append(b[0] + b[1]*X[-1].timestamp())

    plt.scatter(X, Y, color = "b", marker = "o", s = 15) 

    days2 = []
    for i in range(len(X)):
        days2.append(X[i].timestamp())
    
    days = np.array(days2)


    y_pred = b[0] + b[1]*days

    plt.plot(X, y_pred, color = "r")

    plt.gcf().autofmt_xdate()
    plt.title('Linear Regression Prediction for ' + name + ' ' + currency)
    plt.ylabel('price')
    plt.xlabel('date')
    fig = plt.gcf()
    fig.set_size_inches(7, 7)
    plt.show() 
 


def show_prices_plot_linear(table):
    days = np.array(table.get_days())
    prices = np.array(table.get_prices())
    k = estimate_coef(days, prices)
    currency = table.currency
    name = table.name

    plot_regression_line(days, prices, k, currency, name)
