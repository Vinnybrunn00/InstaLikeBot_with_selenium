from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from rich.console import Console
from pyfiglet import figlet_format
from rich import print
import time
import sys
import os
import requests

#value = 0

banner = figlet_format('InstaLikeBot')
style = f'[italic][bold]{banner}[/]'
style2 = f'[italic]{banner}[/]'
style3 = f'[bold]{banner}[/]'

clean = 'cls' if os.name == 'nt' else 'clear'
os.system(clean)

class InstaLikeBot:
    def __init__(self):
        self.firefox = Firefox()
        self.console = Console()
        self.url = 'https://instagram.com'
        self.user = 'vinnybrunn00' # user
        self.passwd = '22v12g25j' # password
        self.profile = 'tntsportsbr' # desired profile

        if self.user == "":
            print('[?] - The USER field is empty!')
            sys.exit()

        elif self.passwd == "":
            print('[?] - The PASSWORD field is empty!')
            sys.exit()

        elif self.profile == "":
            print('[?] - PROFILE field is empty')
            sys.exit()
        time.sleep(2)

    def Open_Browser(self):
        print(style)
        navigator = self.firefox
        with self.console.status(f'{self.url}...') as void:
            navigator.get(self.url)
            time.sleep(2)
        os.system(clean)

    def User(self):
        print(style2)
        try:    
            user = self.firefox.find_element_by_name('username')
            user.click()
            user.send_keys(self.user)
            password = self.firefox.find_element_by_name('password')
            password.click()
            password.send_keys(self.passwd)
            password.send_keys(Keys.RETURN)
        except:
            print('[!] - Element not found, or unexpected error!')
            sys.exit()
        time.sleep(2)
        os.system(clean)

    def Desired_Profile(self):
        print(style3)
        ff = len(self.passwd)
        hide = '*'*ff
        print(f'''
            ============= Personal Data =============
            Usuário: [yellow]{self.user}[/]
            Senha: [green]{hide}[/]
            ==========================================
            ''')

        with self.console.status('logging in...'):
            time.sleep(3)
        #os.system(clean)

        try:
            hastag = f"https://instagram.com/{self.profile}"
            code = requests.get(hastag)
            print(f'Status Code > [green]{code.status_code}[/]')
            profile = self.firefox
            profile.get(hastag)
            with self.console.status(f"Accessing: [green]{hastag}...[/]"):
                time.sleep(10)
            os.system(clean)
        except:
            print('Senha incorreta, tente novamente')
            sys.exit()

    def Click_On_Photo(self):
        print(style)
        try:
            click = self.firefox.find_element_by_class_name('_aagw')
            click.click()
            time.sleep(3)

        except:
            print('[!] - Element not found, or unexpected error')
            quit()

        while True:
            value =+ 1 
            like_photos = self.firefox.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            like_photos.click()
            print("[green][+] Liked photo! :heavy_check_mark:[/]")
            time.sleep(3)

            try:
                next_picture = self.firefox.find_element_by_class_name('_aaqg._aaqh')
                with self.console.status('Next photo...'):
                    next_picture.click()
                    time.sleep(2)
                os.system(clean)

            except:
                os.system(clean)
                print("\n\n[yellow][!] All photos successfully liked! :heavy_check_mark:[/]")
                print(f'[+] Total de fotos curtidas: {value}')
                self.firefox.quit()
                break

vini = InstaLikeBot()
vini.Open_Browser()
vini.User()
vini.Desired_Profile()
vini.Click_On_Photo()
