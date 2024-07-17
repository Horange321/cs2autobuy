#!/bin/env python3
import time

import easyocr
import torch
import pynput
import yaml
import pyautogui

from money import get_money
from army import get_army
from log import *
from buy import *

log(LogLevel.INFO, "Cuda support", torch.cuda.is_available())
reader = easyocr.Reader(['en'])
with open('autobuy.yml', 'r') as f:
    conf = yaml.safe_load(f)


def once(de: bool = False):
    log(LogLevel.INFO, '', ('def hotkey' if de else 'hotkey') + 'pressed')
    time.sleep(conf['keycodes']['delay'])
    money = get_money(reader, conf)
    if money is None:
        return
    log(LogLevel.INFO, 'money', money)
    army = get_army()
    if army is None:
        return
    log(LogLevel.INFO, '', army)

    pyautogui.press(conf['keycodes']['buy'])
    if army == 'T':
        autobuy('def_t', money) if de else autobuy('t', money)
    else:
        autobuy('def_ct', money) if de else autobuy('ct', money)


with pynput.keyboard.GlobalHotKeys({
    conf['keycodes']['hotkey']: once,
    conf['keycodes']['def_hotkey']: lambda: once(True)
}) as listener:
    print("Ready")
    listener.join()
