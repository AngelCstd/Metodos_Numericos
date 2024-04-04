from helpers import obtener_matriz, verificar_elementos_nulos, convertir_dominante, despeje_ecuaciones_lineales, obtener_valores_variables, error_division
from sympy import symbols
x = symbols('x')
y = symbols('y')
z = symbols('z')

def jacobi():

    #Obtener la matriz y iniciar la lista de resultados, junto con los indices iniciales
    xi = 0
    yi = 0
    zi = 0
    resultados = list()
    matriz = obtener_matriz()

    #Revisar que la matris no tenga elementos nulos
    if verificar_elementos_nulos(matriz): return ["No se puede tener elementos nulos"]

    #Revisar que no se repitan filas ni columnas
    #CHECAR BIEN ESTA FUNCION PORQUE AUN NO A HAGO JAJSJASJA
    if verificar_que_no_se_repitan_filas(matriz): return ["No se pueden repetir filas ni columnas"]

    #Revisar que exista la matriz dominante
    matriz_dominante = convertir_dominante(matriz)
    if not matriz_dominante: return ["No se puede realizar ya que no existe la matriz dominante"]
    resultados.append(f"\n----------------------------------Tu matriz inicial es:\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}")
    resultados.append(f"---------------------------------\nTu matriz dominante es:\n{matriz_dominante[0]}\n{matriz_dominante[1]}\n{matriz_dominante[2]}")

    #Obtener el despeje de las ecuaciones
    ecuacion_x = despeje_ecuaciones_lineales([*matriz_dominante[0]], x, 0)
    ecuacion_y = despeje_ecuaciones_lineales([*matriz_dominante[1]], y, 1)
    ecuacion_z = despeje_ecuaciones_lineales([*matriz_dominante[2]], z, 2)
    resultados.append(f"""-----------------------------
Tus ecuaciones son:
x = {ecuacion_x}
y = {ecuacion_y}
z = {ecuacion_z}""")

    #Iniciar ciclo y guardar la i0 anterior
    for i in range(1,90+1):
        xi_anterior = xi
        yi_anterior = yi
        zi_anterior = zi

        #Obtener la nueva i de cada valor
        xi = obtener_valores_variables(ecuacion_x, ((x, xi_anterior),(y, yi_anterior), (z, zi_anterior)))
        yi = obtener_valores_variables(ecuacion_y, ((x, xi_anterior),(y, yi_anterior), (z, zi_anterior)))
        zi = obtener_valores_variables(ecuacion_z, ((x, xi_anterior),(y, yi_anterior), (z, zi_anterior)))

        #Obtener el error
        error_x = error_division((xi_anterior, xi))
        error_y = error_division((yi_anterior, yi))
        error_z = error_division((zi_anterior, zi))

        #Guardar los valores en la lista de resultados
        resultados.append("---------------------------------------------------")
        resultados.append(f"Tu x{i} es igual a: {xi} con un error de: {error_x}")
        resultados.append(f"Tu y{i} es igual a: {yi} con un error de: {error_y}")
        resultados.append(f"Tu z{i} es igual a: {zi} con un error de: {error_z}")

    return resultados

#----------------------------------------------------
def verificar_que_no_se_repitan_filas(matriz):
    return False
