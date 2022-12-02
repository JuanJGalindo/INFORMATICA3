## module gaussElimin
"""
x = gaussElimin(a,b).
Solves [a]{b} = {x} by Gauss elimination.
"""
import numpy as np
import pandas as pd

def ingresoDatos(n):
    data1=[]
    data2=[]
    a=[]
    b=[]
    for i in range(n**2):
        temp=float(input('Ingrese el coeficiente de la posición determinada para la matriz de coeficientes: '))
        data1.append(temp)
    a=np.array(data1).reshape(n,n)

    for i in range(n):
        temp=float(input('Ingrese el coeficiente de la posición determinada para el vector de términos independientes:'))
        data2.append(temp)
    b=np.array(data2).reshape(n,1)

    return a, b

def resolverSistema(a, b, n):

#Fase de Eliminación
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]

#Fase de Sustitución
    for k in range(n-1,-1,-1):
        if a[k,k]!=0.0:
            b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
        else:
            return False
    return b
