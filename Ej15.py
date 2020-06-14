#Porciones de listas, tuplas y cadenas de caracteres
def meses_faltantes(inicio, final):
	meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
	return meses[inicio: final]

print("Imprimir los nombres de meses dentro de dos parámetros:")
inicio = int(input("Ingrese el mes de inicio: "))
final = int(input("Ingrese el mes final: "))
mesesfalta = meses_faltantes(inicio, final)
print(mesesfalta)