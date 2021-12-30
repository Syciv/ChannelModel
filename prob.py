from random import randint, random


def prob(p):
    """Возвращает True с заданной вероятностью"""
    r = random()
    return r <= p