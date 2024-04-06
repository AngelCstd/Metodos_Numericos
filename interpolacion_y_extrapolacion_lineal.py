def inter_extra_lineal():

    #Pedir valores y guardarlos en un array de tuplas e iniciar un booleano para el menu
    lista_valores = pedir_valores_interpolaciones()
    seguir_ciclo = True

    #Iniciar un ciclo con menu para preguntar si quiere interpolacion o extrapolacion lineal
    while seguir_ciclo:
        opcion = int(input("""Ingresa el número de la opcion que deseas realizar:
1 .- Extrapolación
2 .- Interpolación
3 .- Salir"""))
        if opcion == 1: extrapolacion(lista_valores)
        elif opcion == 2: interpolacion(lista_valores)
        elif opcion == 3: seguir_ciclo = False
        else: print("Lo siento, no encontramos la opcion que escribiste")

#---------------------------------------------------------------------
def pedir_valores_interpolaciones():
    resultado = list()
    limite_valores = int(input("¿Cuántos datos vas a ingresar?: "))

    #Pedir valores
    for i in range(limite_valores):
        x = int(input(f"Ingresa el tiempo de tu par de valores numero {i+1}: "))
        y = int(input(f"Ingresa la poblacion de tu par de valores numero {i+1}: "))
        resultado.append((x, y))

    return resultado

def extrapolacion(lista_valores):
    #Con el numero hacer la pendiente promedio de todos los valores y obtener una idea de ese valor
    
    print("hola")
def interpolacion(lista_valores):
    #Encontrar entre que numeros se encuentra el numero que mandamos y hacer el calculo de la pendiente
    print("hola")
def obtener_pendiente(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return((y2-y1)/(x2-x1))
def definir_funcion(pendiente, punto1):
    print("hola")
