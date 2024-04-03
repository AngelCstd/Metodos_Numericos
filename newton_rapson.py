from helpers import pedir_ecuacion, obtener_valores, error_resta
from sympy import symbols, Add, diff, E
x = symbols('x')

def newton_rapson():

    #Obtener la x inicial
    xi = float(input("¿Cual es tu x inicial?: "))

    #Iniciar lista donde se guardaran los valores
    resultados = list()

    #Obtener la ecuacion y sacar su derivada (Puedes ingresar tu funcion desde aqui si es muy complicada o pedirla si es mas sencilla)
    #ecuacion = Add(*pedir_ecuacion())
    ecuacion = E**x-1/x**2 #Este es el ejercicio que se puso en clase
    derivada = diff(ecuacion, x)

    #Guardar en la respuesta los valores iniciales y las ecuaciones
    resultados.append(f"\nTu X0 es: {xi}\nTu función es: {ecuacion}\nLa derivada de tu función es: {derivada}\n------------------------------")

    #Inicio de ciclo para generar los valores
    for i in range(10):
        #Obtener la x nueva y guardar la anterior para obtener el error
        xi_anterior = xi
        xi = obtener_x_newton_rapson(ecuacion, derivada, xi)

        #Obtener el error
        error = error_resta((xi_anterior, xi))

        #Guardarlo en el array de los resultados
        resultados.append(f"Tu x{len(resultados)} es: {xi}, con un error de: {error}")

        #En caso de que el error ya sea 0 terminar el ciclo
        if error == 0.0: break
    return resultados

#------------------------------------------------------------------------------------------------------
def obtener_x_newton_rapson(funcion, derivada, xi):
    valor_funcion = obtener_valores(funcion, [xi])[0]
    valor_derivada = obtener_valores(derivada, [xi])[0]
    return (xi-(valor_funcion/valor_derivada))
