from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from rich.console import Console
from rich import print
from time import sleep
import sys, os

console = Console()
clear = 'cls' if os.name == 'nt' else 'clear'

class Bot:
    def __init__(self):
        self.navegador = Firefox()
        self.url = 'https://instagram.com'
    
    def getInstagram(self):
        browser = self.navegador
        browser.get(self.url)
        sleep(5)
        print(f'{self.url} :heavy_check_mark:')
        
    def login(self, username, password):
        user = self.navegador.find_element(By.XPATH, '//input[@name="username"]')
        user.click()
        user.send_keys(username)
        passwd = self.navegador.find_element(By.XPATH, '//input[@name="password"]')
        passwd.click()
        passwd.send_keys(password, Keys.RETURN)
        sleep(5)
        print('Login Sucess :heavy_check_mark:')
        
    def Search(self, hashtag: str):
        search = self.navegador
        search.get(f'{self.url}/{hashtag}')
        sleep(5)
        print(self.url + f'/{hashtag} :heavy_check_mark:')
    
    def getPhoto(self):
        self.navegador.find_element(By.XPATH, '//div[@class="_aabd _aa8k  _al3l"]').click()
        print('Click Photo :heavy_check_mark:')
        
        count = 0
        while True:
            count+=1
            self.navegador.find_element(By.XPATH, '//span[@class="_aamw"]').click()
            #self.navegador.find_element(By.XPATH, '//span[@class="_aamw"]//div[@role="button"]').click()
            sleep(2)
            try:
                self.navegador.find_element(By.CLASS_NAME, '_abm0')
                sleep(2)
            except:
                os.system(clear)
                print(f'Todas as {count} fotos curtidas com sucesso')
                sys.exit()
                
bot = Bot()
bot.getInstagram()
bot.login('username', 'password')
bot.Search('profile')
bot.getPhoto()
