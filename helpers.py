from sympy import symbols
x = symbols('x')

#-------------------------------------------------------------------------------
def error_division(valores):

    #Desempaquetamos y regresamos el error de los valores
    previous, current = valores
    return abs((current-previous)/current)

#-------------------------------------------------------------------------------
def error_resta(valores):

    #Desempaquetamos y regresamos el error de los valores
    previous, current = valores
    return abs((current-previous))

#-------------------------------------------------------------------------------
def pedir_ecuacion():

    #Inicio valores que se usaran en el ciclo
    valores_ecuacion = list()
    limite_exponentes = int(input("Hasta que exponente llega tu ecuación: "))

    #Ciclo para agregar los valores a una lista
    for indice in range(limite_exponentes+1):
        valor = int(input(f"Ingresa tu valor x^{indice}: "))
        valores_ecuacion.append(valor*x**indice)

    #Invertimos los valores para una mejor lectura
    valores_ecuacion.reverse()

    #Agregamos los valores a una ecuacion unificada y la retornamos
    return valores_ecuacion

#-------------------------------------------------------------------------------
def obtener_valores(ecuacion, valores):

    #Definimos la tupla donde se guardaran los valores
    resultados = tuple()

    #Recorremos los valores que nos mandaron para btener sus resultados
    for valor in valores:
        resultado_x = float(ecuacion.subs(x, valor))
        resultados = (*resultados, resultado_x)

    #retornamos una tupla con los valores
    return resultados
#-------------------------------------------------------------------------------