import math
import random


def x():
    return random.random() * 2 - 1


def y(x):
    if x > 0:
        y = 1
    elif x < 0:
        y = -1
    prob = random.random()
    if prob <= 0.2:
        y = -y

    return y
