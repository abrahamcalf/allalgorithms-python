# -*- coding: UTF-8 -*-
#
# Gnome Sort Algorithm
# The All ▲lgorithms library for python
#
# Contributed by: Cayo Viegas
# Github: @CayoViegas
#

def gnome(lista):
  pivot = 0
  lista_length = len(lista) 
  while pivot < lista_length - 1:
    if lista[pivot] > lista[pivot + 1]:
      lista[pivot + 1], lista[pivot] = lista[pivot], lista[pivot + 1]
      if pivot > 0:
        pivot -= 2
    pivot += 1
    
