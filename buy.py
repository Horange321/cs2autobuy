import yaml
import pyautogui
from log import *

with open('autobuy.yml', 'r') as f:
    conf = yaml.safe_load(f)


def buy(num):
    log(LogLevel.INFO, 'bought', num)
    num = str(num)
    pyautogui.write(num)
    if num[0] == '5':
        pyautogui.press('esc')


def autobuy(army: str, money: int):
    order = conf['buy'][army]
    sorder = sorted(order, reverse=True)
    for i in sorder:
        if money >= i:
            for j in order[i]:
                buy(j)
            return


def t(money: int):
    pass


def def_t(money: int):
    pass


def ct(money: int):
    pass


def def_ct(money: int):
    pass
