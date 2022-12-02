import numpy as np
import pandas as pd
import logica as log
import interfaz as interf

interf.explicarLogica(), print()


while True: 
    n=int(input('Ingrese el número de ecuaciones del sistema a resolver: '))
    datos=log.ingresoDatos(n), print()

    a=datos[0][0]
    b=datos[0][1]

    print('La matriz de coeficientes es: ')
    interf.imprimirMatriz(a, n)
    print('El vector de términos independientes es: ')
    interf.imprimirVector(b, n), print()

    validez=''
    validez=input('Si la matriz y el vector anterior son correctos, oprima el caracter "w". Si no, digite el caracter "l" y reescriba todo nuevamente: ')
    if validez[0]=='l': continue
    elif validez[0]=='w': break


resultado=log.resolverSistema(a, b, n)

if np.any(resultado)==False:
    mensajeError='El sistema de ecuaciones es irresoluble.'
    print(), print(mensajeError)
else:
    print(),print('Los valores resultantes para las variables involucradas en el sistema de ecuaciones lineales son:')
    interf.imprimirResultado(resultado, n)

