from sympy import symbols, Add
from helpers import pedir_ecuacion, error_division, obtener_valores
x = symbols('x')

def biseccion():

    #Iniciamos nuestro array que mandaremos como resultado
    resultado = list()

    #Obtenemos el rango inicial e iniciamos la lista de nuestros valores
    intervalo1 = float(input("¿Donde empieza tu rango de valores?: "))
    intervalo2 = float(input("¿Donde termina tu rango de valores?: "))
    rango_x = (intervalo1, intervalo2)
    valores = [intervalo1, intervalo2]

    #Obtenemos la funcion
    ecuacion_list = pedir_ecuacion()
    ecuacion = Add(*ecuacion_list)

    #Verificamos si la funcion cumple con el teorema
    resultado_x1, resultado_x2 = obtener_valores(ecuacion,rango_x)
    if (((resultado_x1 < 0) & (resultado_x2 > 0))|((resultado_x1 > 0) & (resultado_x2 < 0)) == False):
        return ["Lo siento, la ecuacion y el rango no cumplen con el teorema, no se puede realizar este método"]    

    #Si el teorema se cumple mandamos a nuetro resultado los valores iniciales
    resultado.append(f"\n#------------------------------\nTu función es: {ecuacion}")
    resultado.append(f"Tu rango inicial es: [{rango_x[0]},{rango_x[1]}]")

    for i in range(20):
        #Obtenemos el punto medio y el nuevo rango de valores
        punto_medio = valor_intermedio(rango_x)
        rango_x = definir_rango_nuevo(rango_x, punto_medio, ecuacion)

        #Agregamos el nuevo valor a la lista y obtenemos el error para agregarlo a nuestra lista de resultados
        valores.append(punto_medio)
        error = error_division((valores[-2], valores[-1]))
        resultado.append(
            f"""----------------------------------------------------------------------------
            Tu C{len(valores)} es: {punto_medio}, tiene un error de {error}
            Tu nuevo rango queda de la forma: [{rango_x[0]}, {rango_x[1]}]""")

    return resultado
#------------------------------------------------------------------------------
def valor_intermedio(rango):

    #Desempaquetamos la tupla de rango y sacamos el valor intermedio entre esos
    a, b = rango
    return (a+b)/2
#-------------------------------------------------------------------------------
def definir_rango_nuevo(rango, intermedio, ecuacion):

    #Acomodamos nuestros valores
    resultado_x1, resultado_x2, resultado_intermedio = obtener_valores(ecuacion, (*rango, intermedio))

    #Retornamos segun nuestro nuevo rango
    if(((resultado_x1 <= 0)&(resultado_intermedio <= 0)) | ((resultado_x1 > 0)&(resultado_intermedio > 0))):
        return (intermedio, rango[1])
    if(((resultado_x2 <= 0)&(resultado_intermedio <= 0)) | ((resultado_x2 > 0)&(resultado_intermedio > 0))):
        return (rango[0], intermedio)