#Funciones con parámetros
def mostrar_mensaje(mensaje):
	#Función con parámetro simple
	print("***************************")
	print(mensaje)
	print("***************************")

def cargar_suma():
	valor1 = int(input("Ingrese el primer valor: "))
	valor2 = int(input("Ingrese el segundo valor: "))
	suma = valor1 + valor2
	print("La suma de los valores es: ", suma)

mostrar_mensaje("Cálculo de la suma de dos valores:")
cargar_suma()