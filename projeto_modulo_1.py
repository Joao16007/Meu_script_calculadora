# -*- coding: utf-8 -*-
"""Projeto - Módulo 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18Bws5IhqsE4BXdVTusY0dcuoSROeWrHr
"""

operacao = 1
while operacao:
  print('0. Sair')
  print('1. Adição')
  print('2. Subtração')
  print('3. Multiplicação')
  print('4. Divisão')

  operacao = int(input('Escolha a operação desejada:\n'))

  if operacao == 0:
    break

  num1 = float(input('Digite o primeiro número: '))
  num2 = float(input('Digite o segundo número: '))

  if operacao == 1:
    print('O resultado é:', num1 + num2)
  elif operacao == 2:
    print('O resultado é:', num1 - num2)
  elif operacao == 3:
    print('O reslutado é:', num1 * num2)
  elif operacao == 4:
    print('O resultado é:', num1 / num2)
  else:
    print('Selecione uma opcao válida! ')