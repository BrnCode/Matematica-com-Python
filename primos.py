# -*- coding: utf-8 -*-
"""Primos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fdAyQ6cDjNnGvKuwqsISqTSW-0RoVsdc
"""

def eh_primo(num):

    for d in range(2, num):
        if num % d == 0:
            return False
        return True

eh_primo(123456789)

def eh_primo(num):

    for d in range(2, num//2 +1): # // da um numero inteiro na div
        if num % d == 0:
            return False
        return True

eh_primo(123456789)

import math

def eh_primo(num):
    # raiz = int(num ** (0.5))
    raiz = int(math.sqrt(num))
    for d in range(2, raiz +1): # // da um numero inteiro na div
        if num % d == 0:
            return False
        return True

eh_primo(123456789)

numero = int(input('Digite um numero: '))
if eh_primo(numero):
    print('O numero {} é primo.'.format(numero))
else:
    print('O numero {} não é primo.'.format(numero))

