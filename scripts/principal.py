from gerenciamento import menus
import pyfiglet
import time
import os
from colorama import Fore, Back, Style, init
from tqdm import tqdm


os.system('cls' if os.name == 'nt' else 'clear')
print ('=============================================================================================\n\n')
eleicoes = pyfiglet.figlet_format('ELEICOES', font='ansi_shadow').splitlines()
puc = pyfiglet.figlet_format('  PUC', font='ansi_shadow').splitlines()

for e, p in zip(eleicoes, puc):
    print(Style.BRIGHT + Fore.WHITE + e + Fore.BLUE + p)

print(Style.RESET_ALL)
enter = input('                           Pressione Enter para continuar...')

os.system('cls' if os.name == 'nt' else 'clear')
print ('\n\n\n\n\n')
for i in tqdm(range(100), desc= 'CARREGANDO: ' , bar_format="{l_bar}%s{bar}%s{r_bar}" % (Style.BRIGHT + Fore.BLUE, Fore.RESET)):
    time.sleep(0.02)
os.system('cls' if os.name == 'nt' else 'clear')
menus.menu_principal()
