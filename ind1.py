#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
С использованием многопоточности для заданного значения найти
сумму ряда с точностью члена ряда по абсолютному значению 1e-07
и произвести сравнение полученной суммы с контрольным значением
функции для двух бесконечных рядов.
"""

from threading import Thread
from math import exp, pow, log, factorial

accuracy = 0.0000001


def func_y1(x):
    yx = (exp(x) - exp(-x)) / 2
    return yx


def func_y2(x):
    yx = 3 ** x
    return yx


def sum1(x):
    s, n, cur = 0, 1, 0
    while True:
        pre = (x ** (n + 2)) / factorial(n + 2)
        n += 2
        if abs(cur - pre) < accuracy:
            break
        cur = (x ** (n + 2)) / factorial(n + 2)
        s += cur
    return s


def sum2(x):
    s, n, cur = 0, 0, 0
    while True:
        pre = (pow(x, n) * pow(log(3), n)) / factorial(n)
        n += 1
        if abs(cur - pre) < accuracy:
            break
        cur = (pow(x, n) * pow(log(3), n)) / factorial(n)
        s += cur
    return s


def compare(first, second, x):
    res = first(x) - second(x)
    print(f"Результат: {res}")


if __name__ == '__main__':
    th1 = Thread(target=compare(sum1, func_y1, 2))
    th2 = Thread(target=compare(sum2, func_y2, 1))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
