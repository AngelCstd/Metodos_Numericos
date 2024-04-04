from sympy import symbols, Add
x = symbols('x')
y = symbols('y')
z = symbols('z')

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
def obtener_matriz():
    matriz = list()
    for i in range(3):
        xi = int(input(f"Ingresa cuanto vale X de tu ecuación {i+1}: "))
        yi = int(input(f"Ingresa cuanto vale Y de tu ecuación {i+1}: "))
        zi = int(input(f"Ingresa cuanto vale Z de tu ecuación {i+1}: "))
        ri = int(input(f"Ingresa a cuanto es igual tu ecuación {i+1}: "))
        matriz.append([xi*x, yi*y, zi*z, ri])
    return matriz

#-------------------------------------------------------------------------------
def verificar_elementos_nulos(matriz):
    for fila in matriz:
        if fila.count(0) != 0: return True
    return False

#-------------------------------------------------------------------------------
def obtener_fila_de_mayor_coeficiente(simbolo, matriz, indice_variable):

    #Iniciamos los valores para saber cual valor es mayor y el indice de la fila que es mayor
    mayor = -1
    fila_indice = -1

    #Iniciamos un ciclo para ver cual valor es mayor
    for fila, indice in zip(matriz, range(3)):

        #Obtenemos el coeficiente del simbolo e indice que pedimos de cada una de las filas
        current_coeficiente = abs(fila[indice_variable].coeff(simbolo))

        #si el coeficiente es mayor al numero mayor actual entonces lo cambiamos y ponemos la fila que tiene ese indice
        if current_coeficiente > mayor:
            mayor = current_coeficiente
            fila_indice = indice

    return fila_indice

#-------------------------------------------------------------------------------
def convertir_dominante(matriz):
    mayor_x = obtener_fila_de_mayor_coeficiente(x, matriz, 0)
    mayor_y = obtener_fila_de_mayor_coeficiente(y, matriz, 1)
    mayor_z = obtener_fila_de_mayor_coeficiente(z, matriz, 2)
    
    if not ((mayor_x != mayor_y ) & (mayor_x != mayor_z) & (mayor_y != mayor_z)): return False
    return [matriz[mayor_x], matriz[mayor_y], matriz[mayor_z]]

#-----------------------------------------------------------------
def multiplicar_lista(lista, multiplicador):

    #Recorremos a lista multiplicandola 
    for i in range(len(lista)):
        lista[i] = lista[i]*multiplicador
    return lista

#----------------------------------------------------
def despeje_ecuaciones_lineales(ecuacion, simbolo, indice_variable):
    
    #Saco el valor que voy a despejar y el resultado
    variable_despejada = ecuacion[indice_variable]
    resultado = ecuacion[-1]
    del ecuacion[indice_variable]
    del ecuacion[-1]
    coeficiente = variable_despejada.coeff(simbolo)

    #Multiplico la matriz restante por -1
    ecuacion_list_despejada = multiplicar_lista(ecuacion, -1)
    ecuacion_add_despejada = Add(resultado, *ecuacion_list_despejada)
    ecuacion_despejada = ecuacion_add_despejada/coeficiente

    return ecuacion_despejada

#----------------------------------------------------
def obtener_valores_variables(ecuacion, variables):

    #Creamos la variable donde vamos a guardar la nueva ecuacion que se ira guardando cuando vamos sustituyendo de variable en variable
    resultado = ecuacion

    #Mandamos los valores de la ecuacion
    for variable, valor in variables:
        resultado = resultado.subs(variable, valor)

    #retornamos una tupla con los valores
    return float(resultado) 