"""
Modulo para la lógica del triqui

Este modulo contiene 3 funciones:

* generarTableroLogico => No recibe nada, 
                          retorna una lista de Nones
* insertarCaracterEnTablero => recibe lista, posicion, caracter
                         retorna un lista actualizada
* determinarGanador => recibe una lista (tablero)
                       retorna ganador ("x", "o", None)
"""

def generarTableroLogico():
    tableroLogico = [None,None,None,None,None,None,None,None,None]
    return tableroLogico

def insertarCaracterEnTablero(tableroLogico:list, posicion:int, caracter:str):
    tableroLogico[posicion] = caracter
    return tableroLogico

def determinarGanador(tableroLogico:list):
    posicionesAComparar = [(0,1,2),
                           (3,4,5),
                           (6,7,8),
                           (0,3,6),
                           (1,4,7),
                           (2,5,8),
                           (0,4,8),
                           (2,4,6)]
    ganador = None
    for pos1, pos2, pos3 in posicionesAComparar:
        if tableroLogico[pos1] == tableroLogico[pos2] == tableroLogico[pos3]:
            ganador = tableroLogico[pos1]
            break
    return ganador




