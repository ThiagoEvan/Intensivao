import pyautogui as pg
import pyperclip
from time import sleep

#abrir chrome
pg.hotkey('win', 'r')
sleep(0.5)
pg.write('chrome')
pg.press('enter')
sleep(10)

# entrar no sistema
#error

pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pg.hotkey('ctrl', 'v')
pg.press('enter')