from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from db.row import Row
from db.table import Table

class PrivatDriverStarter:

    name = 'PrivatBank'



    def get_driver(self) -> webdriver.Chrome:
        return self.driver


    def close_driver(self):
        self.driver.quit()


    def click_all_buttons(self, currency: str, time_to_sleep: float):
        self.cookies_button.click()
        sleep(time_to_sleep)
        self.archive_buttton.click()
        sleep(time_to_sleep)
        self.table_button.click()
        sleep(time_to_sleep)

        self.driver.find_element(By.XPATH, '/html/body').send_keys('\ue00f')
        sleep(time_to_sleep)
        self.currency_list_button.click()
        sleep(time_to_sleep)
        if currency == 'USD':
            self.usd_button.click()
        elif currency == 'EUR':
            self.eur_button.click()
        else:
            raise ValueError('Currency must be USD or EUR')
        
      
        self.driver.find_element(By.XPATH, '/html/body').click()

        sleep(time_to_sleep)
        self.six_months.click()
        while True:
            try:
                sleep(time_to_sleep)
                self.load_more_button.click()
            except:
                break


    def get_table(self, currency: str) -> Table:

        self.driver = webdriver.Chrome()

        self.driver.set_window_size(1280, 720)
        self.driver.get('https://privatbank.ua/rates-archive')

        sleep(3)


        self.cookies_button = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/a[1]')
        self.archive_buttton = self.driver.find_element(by=By.XPATH, value='//*[@id="archive-block"]/span')
        self.table_button = self.driver.find_element(by=By.XPATH, value='//*[@id="table-currency"]')

        self.currency_list_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mainWrapArchive"]/div[3]/article/div/div[1]/div[3]/div/button')
        self.usd_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mainWrapArchive"]/div[3]/article/div/div[1]/div[3]/div/div/ul/li[2]/a')
        self.eur_button = self.driver.find_element(by=By.XPATH, value='//*[@id="mainWrapArchive"]/div[3]/article/div/div[1]/div[3]/div/div/ul/li[3]/a')

        self.six_months = self.driver.find_element(by=By.XPATH, value='//*[@id="six_months_by_table"]')
        self.load_more_button = self.driver.find_element(by=By.XPATH, value='//*[@id="table-period"]/div[1]/div[3]')
    
        self.click_all_buttons(currency, 0.2)
        sleep(1)
        table = self.driver.find_element(by=By.CLASS_NAME, value='insert_table')
        table_text = table.text
        table_text = table_text.replace(',', '.')
        table_text = table_text.replace('/', ' ')
        rows = table_text.split('\n')
        rows = [row.split(' ') for row in rows]

        table = []
        for row in rows:
            table.append(Row(row[0], row[2], row[3],  row[4], row[5]))

        return Table(table, self.name, currency)
