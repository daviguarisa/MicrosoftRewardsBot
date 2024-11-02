# ATENÇÃO - Abrir pasta e não somente o arquivo!

import pyautogui as pg
import pandas as pd
import time, random

pg.PAUSE = 1 # -> tempo entre todos os comandos

pg.press('Win')
pg.write('edge')
pg.press('enter')
pg.hotkey("alt", "space")
pg.press("x")
time.sleep(1) 
pg.click(x=298, y=52) # -> barra de pesquisa
pg.write('https://rewards.bing.com/')
pg.press('enter')
pg.hotkey('ctrl', 't')

tabela = pd.read_csv('times_brasileiros.csv')

for i in range(0, 40): # -> número de pesquisas
    indice = random.randint(1, 100)
    team = tabela.loc[indice, 'Time']
    pg.write(str(team))
    pg.press('enter')
    time.sleep(1) # -> tempo entre pesquisas
    pg.hotkey('ctrl', 'w')
    pg.click(x=400, y=13) # -> nova aba
    pg.click(x=298, y=52) # -> barra de pesquisa

# Trava de segurança -> arrastar o mouse pro canto superior esquerdo