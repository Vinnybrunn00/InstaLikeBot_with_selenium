from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from rich.console import Console
from pyfiglet import figlet_format
from rich import print
import time
import sys
import os

#value = 0

banner = figlet_format('InstaLikeBot')
style = f'[italic][bold]{banner}[/]'
style2 = f'[italic]{banner}[/]'
style3 = f'[bold]{banner}[/]'

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

class InstaLikeBot:
    def __init__(self):
        self.firefox = Firefox()
        self.console = Console()
        self.url = 'https://instagram.com'
        self.user = 'result358' # usuario
        self.passwd = '22v12g25j' # senha
        self.profile = 'vinnybrunn00' # perfil desejado

        if self.user == "":
            print('[?] - A o campo USUÁRIO está vazio!')
            sys.exit()

        elif self.passwd == "":
            print('[?] - o campo SENHA está vazio!')
            sys.exit()

        elif self.profile == "":
            print('[?] - O campo PROFILE está vazio')
            sys.exit()
        time.sleep(2)

    def Abrir_Navegador(self):
        print(style)
        navegador = self.firefox
        with self.console.status(f'{self.url}...') as void:
            navegador.get(self.url)
            time.sleep(2)
        os.system(limpar)

    def Usuario(self):
        print(style2)
        try:    
            usuario = self.firefox.find_element_by_name('username')
            usuario.click()
            usuario.send_keys(self.user)
            senha = self.firefox.find_element_by_name('password')
            senha.click()
            senha.send_keys(self.passwd)
            senha.send_keys(Keys.RETURN)
        except:
            print('[!] - Elemento não encontrado, ou erro inesperado!')
            sys.exit()
        time.sleep(2)
        os.system(limpar)

    def Perfil_Desejado(self):
        print(style3)
        ff = len(self.passwd)
        ocultar = '*'*ff
        print(f'''
            ============= Dados Pessoais =============
            Usuário: [yellow]{self.user}[/]
            Senha: [green]{ocultar}[/]
            ==========================================
            ''')

        with self.console.status('Logando...') as void:
            time.sleep(3)
        #os.system(limpar)
        try:
            hastag = f"https://instagram.com/{self.profile}"
            perfil = self.firefox
            perfil.get(hastag)
            with self.console.status(f"Acessando: [green]{hastag}...[/]") as void:
                time.sleep(3)
            os.system(limpar)
        except:
            print('Senha incorreta, tente novamente')
            sys.exit()

    def Clickar_na_foto(self):
        print(style)
        try:
            click = self.firefox.find_element_by_class_name('_aagu')
            click.click()
            time.sleep(3)

        except:
            print('[!] - Elemento não encontrado, ou erro inesperado')
            quit()
            sys.exit()

        while True:
            #value =+ 1 
            curtir_fotos = self.firefox.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            curtir_fotos.click()
            print("[green][+] Foto curtida! :heavy_check_mark:[/]")
            time.sleep(3)

            try:
                proxima_foto = self.firefox.find_element_by_class_name('_aaqg')
                with self.console.status('Proxima foto...') as void:
                    proxima_foto.click()
                    time.sleep(2)
                os.system(limpar)

            except:
                os.system(limpar)
                print("\n\n[yellow][!] Todas as fotos curtidas com sucesso! :heavy_check_mark:[/]")
                #print(f'[+] Total de fotos curtidas: {value}')
                self.firefox.quit()
                break

vini = InstaLikeBot()
vini.Abrir_Navegador()
vini.Usuario()
vini.Perfil_Desejado()
vini.Clickar_na_foto()
