#Datos tipo tupla
def cargar_fecha():
	dd = int(input("Ingrese número de día: "))
	mm = int(input("Ingrese número de mes: "))
	aa = int(input("Ingrese número de año: "))

	tupla = (dd, mm, aa)
	return tupla

def imprimir_fecha(fecha):
	print(fecha[0], fecha[1], fecha[2], sep = "/")

fecha = cargar_fecha()
imprimir_fecha(fecha)