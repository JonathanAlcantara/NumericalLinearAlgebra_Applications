# -*- coding: utf-8 -*-

import numpy as np
import csv
a = []
b = []

with open('LUINPUT.csv','r') as csvfile:
    # o nome 'spamreader' abaixo é só exemplo, poderia ser qq. coisa
    spamreader = csv.reader(csvfile, delimiter=',') # separe por vírgula

    # o módulo csv detectará novas linhas automaticamente
    for linha in spamreader:
        if len(linha) == 0:
            break
        a.append(linha)

    for linha in spamreader:
      b.append(linha)





u = []
l = []
linesQty = len(a)
columnsQty = len(a[0])

matrix = np.array(a, float)
u = matrix

b = np.array(b,float)
b = np.transpose(b)

if np.linalg.det(matrix) == 0:
  print("Matriz singular. Não pode fazer LU")
  exit
elif linesQty != columnsQty:
  print("Matriz nao e quadrada")
else:
  for j in range(0,columnsQty - 1):
    pivot = u[j,j]
    if pivot == 0:
      break
    print("Pivo da coluna ",j+1," é ", pivot)
    mTemp = np.identity(linesQty,float)
    lTemp = np.identity(linesQty,float)
    for k in range(j+1, linesQty):
      if u[k,j] != 0:
        mTemp[k,j] = (-1 * u[k,j])/pivot
        lTemp[k,j] = u[k,j]/pivot

    print("M",j+1,":\n")
    print(mTemp)
    print("L",j+1,":\n")
    print(lTemp)

    u = np.dot(mTemp, u)
    print("U",":\n")
    print(u)

    if len(l) == 0:
      l = lTemp
    else:
      l = np.dot(l,lTemp)

    print("L",":\n")
    print(l)

  print("\n\nA = LU\n")
  print("A = \n")
  print(matrix)
  print("\n\nL",":\n")
  print(l)
  print("\n\nU",":\n")
  print(u)
  print ("\n\nLU:")
  print(np.dot(l,u))
 
  # Calculating Y
  
  y = np.zeros([linesQty,1])
  
  for i in range(0,linesQty):
    if(i == 0):
        y[i,0] = b[i,0]/l[i,i]
    else:
        sum = 0
        for k in range(0,i):
            sum += y[k,0]*l[i,k]
        y[i,0] = (b[i,0] - sum)/l[i,i]
  
  print("\n\nY:\n")
  print(y)
  
  # Calculating X
  x = np.zeros([linesQty,1])
  
  for i in range(linesQty - 1, -1, -1):
    if(i == linesQty - 1):
        x[i,0] = y[i,0]/u[i,i]
    else:
        sum = 0
        for k in range(i+1, linesQty):
            sum += x[k,0]*u[i,k]
        x[i,0] = (y[i,0] - sum)/u[i,i]
  
  print("\n\nX:\n")
  print(x)
        








