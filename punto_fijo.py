from helpers import pedir_ecuacion, obtener_valores, error_resta
from sympy import symbols, Add, sqrt

x = symbols('x')
#SI QUEREMOS MEJORAR ESTE METODO PODEMOS METER CONDICIONALES PARA SABER SUS TIPOS DE DESPEJES QUE TIENE Y HACER MAS DESPEJES COMO EL DE SACAR  LAS X O RAIZ TERCEARIA
def punto_fijo():

    #Iniciamos las listas de nuestros resultados
    resultado_ecuacion_1 = list()
    resultado_ecuacion_2 = list()

    #Pedir la x inicial
    ecuacion_1_xi = float(input("¿Cual es tu x inicial?: "))
    ecuacion_2_xi = ecuacion_1_xi

    #Obtener la ecuación
    ecuacion_list = pedir_ecuacion()

    #Despejar la ecuación
    ecuacion_1_despejada = despeje_x([*ecuacion_list])
    ecuacion_2_despejada = despeje_x_cuadrada([*ecuacion_list])

    #Guardar la x inicial en cada lista
    resultado_ecuacion_1.append(f"\n\nTu X0 es: {ecuacion_1_xi}\nTu ecuacion despejada es: {ecuacion_1_despejada}")
    resultado_ecuacion_2.append(f"----------------------------------\nTu X0 es: {ecuacion_2_xi}\nTu ecuacion despejada es: {ecuacion_2_despejada}")

    for i in range(10):
        #Guardamos los valores anteriores de las xi para poder obtener los errores
        valor_1_x_anterior = ecuacion_1_xi
        valor_2_x_anterior = ecuacion_2_xi

        #Obtenemos el nuevo valor de x
        ecuacion_1_xi, ignore = obtener_valores(ecuacion_1_despejada, (ecuacion_1_xi, 0))
        ecuacion_2_xi, ignore = obtener_valores(ecuacion_2_despejada, (ecuacion_2_xi, 0))

        #Guardar esa x y obtener el error
        error_ecuacion_1 = error_resta((valor_1_x_anterior, ecuacion_1_xi))
        error_ecuacion_2 = error_resta((valor_2_x_anterior, ecuacion_2_xi))

        #Guardar el valor junto con su error en el array
        resultado_ecuacion_1.append(
        f"""------------------------------------
        Tu X{len(resultado_ecuacion_1)} es: {ecuacion_1_xi}
        Con un error de: {error_ecuacion_1}""")
        resultado_ecuacion_2.append(
        f"""------------------------------------
        Tu X{len(resultado_ecuacion_2)} es: {ecuacion_2_xi}
        Con un error de: {error_ecuacion_2}""")

    #Retornar el valor de las listas pero unidas
    return [*resultado_ecuacion_1, *resultado_ecuacion_2]
#----------------------------------------------------------------
def despeje_x(ecuacion_list_copia):

    #Saco la x que voy a despejar
    x_despejada = ecuacion_list_copia[-2]
    del ecuacion_list_copia[-2]
    coeficiente_x = x_despejada.coeff(x)

    #Multiplico la matriz restante por -1
    ecuacion_list_despejada = multiplicar_lista(ecuacion_list_copia, -1)
    ecuacion_add_despejada = Add(*ecuacion_list_despejada)
    ecuacion_despejada = ecuacion_add_despejada/coeficiente_x

    return ecuacion_despejada
#----------------------------------------------------------------
def despeje_x_cuadrada(ecuacion_list_copia):

    #Saco la x que voy a despejar
    x_despejada = ecuacion_list_copia[-3]
    del ecuacion_list_copia[-3]
    coeficiente_x = x_despejada.coeff(x**2)

    #Multiplico la matriz restante por -1
    ecuacion_list_despejada = multiplicar_lista(ecuacion_list_copia, -1)
    ecuacion_add_despejada = Add(*ecuacion_list_despejada)
    ecuacion_dividida_despejada = ecuacion_add_despejada/coeficiente_x
    ecuacion_despejada = sqrt(ecuacion_dividida_despejada)

    return ecuacion_despejada
#_----------------------------------------------------------------
def multiplicar_lista(lista, multiplicador):

    #Recorremos a lista multiplicandola 
    for i in range(len(lista)):
        lista[i] = lista[i]*multiplicador
    return lista