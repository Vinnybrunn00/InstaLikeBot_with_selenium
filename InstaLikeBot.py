from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from rich import print
import time
import sys
import os

limpar = 'cls' if os.name == 'nt' else 'clear'
os.system(limpar)

class InstaLikeBot:
    def __init__(self):
        self.firefox = Firefox()

    def Abrir_Navegador(self):
        url = 'https://instagram.com'
        navegador = self.firefox
        navegador.get(url)
        qq = '...'
        print(f"{url}", end='')
        for l in list(qq):
            print(l, end='')
            sys.stdout.flush()
            time.sleep(1)
        time.sleep(2)
        os.system(limpar)

    def Usuario(self):
        user = '' #seu usuario
        usuario = self.firefox.find_element_by_name('username')
        usuario.click()
        usuario.send_keys(user)
        print(
            'DADOS DO INSTAGRAM'
            '\n\n=========================='
            f"\nUSUARIO: {user}")

    def Senha(self):
        passwd = '' #sua senha
        senha = self.firefox.find_element_by_name('password')
        senha.click()
        senha.send_keys(passwd)
        senha.send_keys(Keys.RETURN)
        print(
            f"SENHA: {passwd}"
            '\n==========================\n')
        vl = '...'
        print("Entrando", end='')
        for v in list(vl):
            print(v, end='')
            sys.stdout.flush()
            time.sleep(1)
        os.system(limpar)
        print("\nTUDO PRONTO!!!\n")
        time.sleep(3)
        #os.system(limpar)

    def Perfil_Desejado(self):
        tt = input("Digite nome do usuario: ")
        hastag = f"https://instagram.com/{tt}"
        perfil = self.firefox
        perfil.get(hastag)
        print(f"Acessando: [green]{hastag}[/]")
        time.sleep(3)
        os.system(limpar)

    def Clickar_na_foto(self):
        click = self.firefox.find_element_by_class_name('_9AhH0').click()
        time.sleep(3)

        while True:
            print('[yellow]+================> INSTALIKEBOT <================+[/]\n')
            curtir_fotos = self.firefox.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            curtir_fotos.click()
            print("[green][+] Foto curtida![/]")
            time.sleep(3)

            try:
                proxima_foto = self.firefox.find_element_by_class_name('l8mY4.feth3')
                pontos = '...'
                print("[reed][+]Próxima foto[/]", end='')
                for i in list(pontos):
                    print(i, end='')
                    sys.stdout.flush()
                    time.sleep(00.5)
                proxima_foto.click()
                time.sleep(2)
                os.system(limpar)

            except:
                os.system(limpar)
                print("\n\n[yellow][+] TODAS AS FOTOS CURTIDAS COM SUCESSO[/]")
                break

vini = InstaLikeBot()
vini.Abrir_Navegador()
vini.Usuario()
vini.Senha()
vini.Perfil_Desejado()
vini.Clickar_na_foto()
