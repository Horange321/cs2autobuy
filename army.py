from PIL import Image
from log import *


def rgb2hsv(c):
    r = c[0] / 255.0
    g = c[1] / 255.0
    b = c[2] / 255.0
    c = [r, g, b]
    v = max(c)

    if v == 0:
        s = 0
    else:
        s = min(c) / v

    if v == c[0]:
        h = 60 * (c[1] - c[2]) / (v - min(c))
    elif v == c[1]:
        h = 120 + 60 * (c[2] - c[0]) / (v - min(c))
    else:
        h = 240 + 60 * (c[0] - c[1]) / (v - min(c))
    if h < 0:
        h += 360
    return h


def get_army():
    img = Image.open('img.png')
    c = sorted(img.getcolors(255 ** 3), reverse=True)
    c = c[0][1]
    log(LogLevel.DEBUG, 'c', c)
    h = rgb2hsv(c)
    log(LogLevel.DEBUG, 'h', h)
    return 'T' if h < 150 else 'CT'
