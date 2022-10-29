#####################################################################
""" Ejemplo: Crear los siguientes vectores, matrices y tensores. (Para ello utilice arreglos de numpy)

                     => vector1 = 1,2,3,4,5
                     => vector2 = 10,20,30,40,50

                     => matriz1 = [1 1 1
                                1 1 1
                                1 1 1]
                     => matriz2 = [1 2 3
                                4 5 6
                                7 8 9]

                     => tensor1=[[0 0 0
                                0 0 0
                                0 0 0]
                                [2 2 2
                                2 2 2
                                2 2 2]] 

                     => tensor2= [[1  2  3
                                4  5  6
                                7  8  9]
                                [10 11 12
                                13 14 15
                                16 17 18]] 
"""

import numpy as np

# Vectores con numpy
vector1 = np.array([1,2,3,4,5])
vector2 = np.array([10,20,30,40,50])

# Matrices con numpy
matriz1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

matriz2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Tensores con numpy
tensor1= np.array([ [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]],
                 
                    [[2, 2, 2],
                     [2, 2, 2],
                     [2, 2, 2]]
                 ])
tensor2= np.array([ [[1,  2,  3],
                     [4,  5,  6],
                     [7,  8,  9]],
                  
                    [[10, 11, 12],
                     [13, 14, 15],
                     [16, 17, 18]]
                 ])


#####################################################################
"""
Ejemplo: ¿Cómo crear los anteriores arreglos (vectores, matrices, tensores) de manera automática?
"""
vector1 = np.arange(1,6,1) #inicio,fin,salto
vector2 = np.arange(10, 51, 10)

matriz1 = np.ones((3,3))   #tamaño (filas,columnas)
matriz2 = np.arange(1, 10).reshape((3,3))  #reshape (filas, columnas)

tensor1 = "pendiente!!!"
tensor2 = np.arange(1,19).reshape((2,3,3))



"""
ejemplos: a) ¿Cómo apilar vector1 y vector2 ? (formar nuevo vector mas largo)
          b) ¿Cómo apilar vector1 y vector2 ? (formar nueva matriz)
          c) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz mas ancha)
          d) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz más larga)
          e) ¿Cómo apilar un vector y una matriz? (formar nueva matriz más larga o más ancha)
"""

""" a) ¿Cómo apilar vector1 y vector2 ? (formar nuevo vector mas largo)
        
        vector1 = 1 2 3 4 5       vector2 = 10 20 30 40 50
        
        vectorResultante = 1 2 3 4 5 10 20 30 40 50 
"""
vectorResultante = np.hstack((vector1, vector2))
print(vectorResultante)


""" b) ¿Cómo apilar vector1 y vector2 ? (formar nueva matriz)
        
        vector1 = 1 2 3 4 5     vector2 = 10 20 30 40 50

        matrizResultante =   1  2  3  4  5
                            10 20 30 40 50
"""

matrizResultante = np.vstack((vector1, vector2))
print(matrizResultante)


""" c) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz mas ancha)
        
        matriz1 =  1 1 1     matriz2 = 1 2 3
                   1 1 1               4 5 6
                   1 1 1               7 8 9
        
        => Apilarlas horizontalmente
        matrizAncha  =  1 1 1 1 2 3
                        1 1 1 4 5 6
                        1 1 1 7 8 9
"""

matrizAncha = np.hstack((matriz1, matriz2))
print(matrizAncha)


""" d) ¿Cómo apilar matriz1 y matriz2 ? (formar nueva matriz más larga)

        matriz1 =  1 1 1     matriz2 =  1 2 3
                   1 1 1                4 5 6
                   1 1 1                7 8 9
    
        => Apilarlas verticalmente
        matrizLarga =  1 1 1 
                       1 1 1 
                       1 1 1 
                       1 2 3
                       4 5 6
                       7 8 9
"""

matrizLarga = np.vstack((matriz1, matriz2))
print(matrizLarga)


"""
        e) ¿Cómo apilar una matriz y un vector? (formar una matriz más larga o más ancha)

        matriz =  1 2 3      vector = 10 20 30
                  4 5 6                            
                  7 8 9                            

        matrizResultante1 =  1  2  3
                             4  5  6
                             7  8  9
                             10 20 30

        matrizResultante2 =  1  2  3 10
                             4  5  6 20
                             7  8  9 30
           
"""
vector = np.array([10,20,30])
matriz = np.arange(1,10).reshape((3,3))

matrizResultante1 = np.vstack((matriz, vector))
print("=>", matrizResultante1)

matrizResultante2 = np.hstack((matriz, vector.reshape((3,1))))
print("=>", matrizResultante2)