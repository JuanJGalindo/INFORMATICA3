"""
Aqui contenemos la parte visual del
triqui. Este modulo contiene 2 funciones:
* explicarJuego: retornar mensaje explicativo
* imprimirTablero: retornar string con el tablero
"""
import numpy as np
import pandas as pd

def explicarLogica():
    explicacion = """
  ================================================================
    El siguiente programa está diseñado para llevar a cabo la
    resolución de sistemas de ecuaciones lineales de la forma:

                    A\u2081\u2081X\u2081+A\u2081\u2082X\u2082+...+A\u2081\u2099X\u2099=B\u2081
                    A\u2082\u2081X\u2081+A\u2082\u2082X\u2082+...+A\u2082\u2099X\u2099=B\u2082
                               .
                               .
                               .
                    A\u2099\u2081X\u2081+A\u2099\u2082X\u2082+...+A\u2099\u2099X\u2099=B\u2099  

    Donde los valores de A\u2096\u2096, corresponden a los coeficientes que 
    acompañan a cada variable en el sistema de ecuaciones y B\u2096, son 
    los valores de los términos independientes de cada ecuación.

    De tal manera que se cree la matriz A y el vector B:

                   |A\u2081\u2081 A\u2081\u2082 ... A\u2081\u2099|        |B\u2081|
                   |A\u2082\u2081 A\u2082\u2082 ... A\u2082\u2099|        |B\u2082|
                   |      ...      |        |..|
                   |A\u2099\u2081 A\u2099\u2082 ... A\u2099\u2099|        |B\u2099|
    
    Para la matriz A, el programa le pedirá ingresar los valores 
    correspondientes mediante llenado de filas con sus correspondientes
    valores en cada columna(A\u2081\u2081, A\u2081\u2082, ..., A\u2081\u2099; luego, A\u2082\u2081 A\u2082\u2082 ... A\u2082\u2099.
    Así sucesivamente, hasta A\u2099\u2081 A\u2099\u2082 ... A\u2099\u2099) 
    y el vector B, según los valores de sus filas (B\u2081, B\u2082, ..., B\u2099).
  =======================================================================
    """
    print(explicacion)


def imprimirMatriz(a, n):
  matrizVisual=a
  for valor in enumerate(matrizVisual):
    for i in range(n):
      print("{}".format(valor[1][i]), end=' ')
    print()
  print()

def imprimirVector(b, n):
  vectorVisual=b
  for valor in enumerate(vectorVisual):
    print("{}".format(valor[1][0]), end=' '),print()
  print()

def imprimirResultado(resultado, n):
  data=[]
  index=[]  
  for i in range(n):
    data.append(resultado[i][0])
    index.append('X'+str(i+1))
  resultado=pd.Series(data, index=index)
  print(resultado)
    
imprimirResultado(np.array([[1],[2]]), 2)