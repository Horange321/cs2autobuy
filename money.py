import pyautogui
from log import *


def get_money(reader, conf):
    img = pyautogui.screenshot('img.png')
    x = conf['resolution']['x']
    y = conf['resolution']['y']
    img = img.crop((0, int(0.9375 * y), int(0.0625 * x), int(0.9861 * y)))
    img.save('img.png')
    img.close()
    res = reader.readtext('img.png')[0][1]
    try:
        res = int(res[1:])  # 取消第一个 '$'
        print(res)
        return res
    except ValueError:
        log(LogLevel.ERROR, '', "Error: Failed to get money")
        return None
