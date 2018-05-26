import numpy as np
import csv
import math
tol = 0.001
a = []

with open('jacobiinput.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',') 

    for linha in spamreader:
        a.append(linha)

linesQty = len(a)
columnsQty = len(a[0])

a = np.array(a)
print("A Inicial\n")
print(a)
x = np.identity(linesQty, float)

if linesQty != columnsQty:
    print ("Matriz não é quadrada")
elif np.allclose(a, a.T, atol=1e-8) == False:
   print("Matriz não é simétrica")
else:
    tmp = a
    np.fill_diagonal(tmp, 0)
    np.absolute(tmp)
    i,j = np.unravel_index(np.absolute(tmp).argmax(), a.shape)
    print(i,j)
    while(math.fabs(a[i,j]) > tol):
        ang = math.pi/4
        if a[i,i] != a[j,j]:
            ang = 0.5 * np.arctan((2 * a[i,j])/(a[i,i] - a[j,j]))
        p = np.identity(linesQty, float)
        p[i,i] = np.cos(ang)
        p[j,j] = np.cos(ang)
        p[i,j] = -1 * np.sin(ang)
        p[j,i] = np.sin(ang)
        print("P:\n")
        print(p)
        
        pTranspose = p
        pTranspose = np.transpose(pTranspose)
        print("PTranspose:\n")
        print(pTranspose)
        
        pTransVsA = np.dot(pTranspose, a)
        
        
        a = np.dot(p.T, np.dot(a,p))
        print("\n\nA:\n")
        print(a)
        
        x = np.dot(x,p)
        print("\n\nX:\n")
        print(x)
        
        tmp = a
        np.fill_diagonal(tmp, 0)
        np.absolute(tmp)
        i,j = np.unravel_index(np.absolute(tmp).argmax(), a.shape)
        print(i,j)


            
    