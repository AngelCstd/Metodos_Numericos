from helpers import obtener_matriz, multiplicar_lista
from sympy import symbols
x = symbols('x')
y = symbols('y')
z = symbols('z')
lista_variables = [x, y, z]
def gauss_jordan():

    #Obtener matriz y mostrarla
    matriz = obtener_matriz()
    matriz[0] = [*matriz[0], 1, 0, 0]
    matriz[1] = [*matriz[1], 0, 1, 0]
    matriz[2] = [*matriz[2], 0, 0, 1]
    print("Tu matriz inicial es:")
    for fila in matriz:
        print(fila)

    #Convertir la matriz en uno y despues restarla a la otra matriz y mostrarla en ambas ocaciones
    for i in range(len(matriz)):
        matriz = obtener_uno(matriz, i)
        print("-------------------------------------")
        print(f"Convirtiendo en uno la variable {i}")
        for fila in matriz:
            print(fila)
        matriz = convirtiendo_en_ceros(matriz, i)
        print(f"Convirtiendo en ceros")
        for fila in matriz:
            print(fila)

#_----------------------------------------------------------
def obtener_uno(matriz, indice):
    coeficiente = matriz[indice][indice].coeff(lista_variables[indice])
    nuevo_vector = multiplicar_lista(matriz[indice], (1/coeficiente))
    matriz[indice] = nuevo_vector
    return matriz
#_----------------------------------------------------------
def convirtiendo_en_ceros(matriz, indice_matriz_con_uno):
    matriz_con_ceros = matriz 
    for i in range(len(matriz_con_ceros)):
        if i != indice_matriz_con_uno:
            coeficiente = matriz_con_ceros[i][indice_matriz_con_uno].coeff(lista_variables[indice_matriz_con_uno])
            vector_nuevo = suma_matrices(matriz_con_ceros[i], coeficiente, [*matriz_con_ceros[indice_matriz_con_uno]])
            matriz_con_ceros[i] = vector_nuevo
    return matriz_con_ceros
#-------------------------------------------------------------
def suma_matrices(matriz_cambios, coeficiente, matriz_que_suma):
    matriz_multiplicada = multiplicar_lista(matriz_que_suma,-coeficiente)
    for i in range(len(matriz_multiplicada)):
        matriz_cambios[i] = matriz_cambios[i]+matriz_multiplicada[i]
    return matriz_cambios