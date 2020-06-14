#Funciones que retornan datos
def retorno_superficie(lado):
	sup = lado + lado
	return sup

va = int(input("Introduce el valor del cuadrado: "))
superficie = retorno_superficie(va)
print("Al algoritmo del cuadrado es: ", superficie)