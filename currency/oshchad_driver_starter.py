from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from db.row import Row
from db.table import Table

class OshchadDriverStarter:
    PATH = '.\chromedriver.exe'


    def __init__(self):
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get('https://www.oschadbank.ua/rates-archive')

        sleep(5)

        # buttons
        self.table_button = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[2]/div[1]/div[1]/div/div[3]/div[2]')

        self.currency_list_button = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[1]/div[1]/div[1]/div/div[1]')
        self.usd_button = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/li[1]')
        self.eur_button = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/li[2]')

        self.six_months = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[1]/div[2]/div/ul/li[4]')
        self.load_more_button = self.driver.find_element(by=By.XPATH, value='//*[@id="__layout"]/div/div[2]/main/section[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/button/span')
    

    def get_driver(self) -> webdriver.Chrome:
        return self.driver


    def close_driver(self):
        self.driver.quit()


    def click_all_buttons(self, currency: str, time_to_sleep: float):
        self.currency_list_button.click()
        sleep(time_to_sleep)
        if currency == 'USD':
            self.usd_button.click()
        elif currency == 'EUR':
            self.eur_button.click()
        else:
            raise ValueError('Currency must be USD or EUR')
        sleep(time_to_sleep)


        self.driver.find_element(By.XPATH, '/html/body').send_keys('\ue00f')
        sleep(time_to_sleep)
        self.table_button.click()
        sleep(time_to_sleep)
        # press PAGE DOWN to scroll down
        
        
        self.six_months.click()
        while True:
            try:
                sleep(time_to_sleep)
                self.load_more_button.click()
            except:
                break


    def get_table(self, currency: str) -> Table:
        self.click_all_buttons(currency, 1)
        sleep(1)
        table = self.driver.find_element(by=By.CLASS_NAME, value='rate-table__table-body')
        table_text = table.text
        return table_text
        # table_text = table_text.replace(',', '.')
        # table_text = table_text.replace('/', ' ')
        # rows = table_text.split('\n')
        # rows = [row.split(' ') for row in rows]

        # table = []
        # for row in rows:
        #     table.append(Row(row[0], row[2], row[3],  row[4], row[5]))

        # return Table(table, "PrivatBank", currency)
