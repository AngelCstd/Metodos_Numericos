from biseccion import biseccion
from punto_fijo import punto_fijo
from newton_rapson import newton_rapson
from gauss_seidel import gauss_seidel
from jacobi import jacobi
from interpolacion_y_extrapolacion_lineal import inter_extra_lineal
from gauss_jordan import gauss_jordan
#___________________________
#resultado = biseccion()
#for texto in resultado:
#    print(texto)
#___________________________
#resultado = punto_fijo()
#for texto in resultado:
#    print(texto)
#___________________________
#resultado = newton_rapson()
#for texto in resultado:
#    print(texto)
resultado = gauss_seidel()
for texto in resultado:
    print(texto)
#resultado = jacobi()
#for texto in resultado:
#    print(texto)
#inter_extra_lineal()
#gauss_jordan()