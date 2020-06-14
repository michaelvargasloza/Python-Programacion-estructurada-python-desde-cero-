#Porciones de listas, tuplas y cadenas de caracteres
def meses_faltantes(inicio):
	meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
	return meses[:inicio]

print("Imprimir los nombres de meses anteriores al mes indicado:")
inicio = int(input("Ingrese el número de mes: "))
mesesfalta = meses_faltantes(inicio)
print(mesesfalta)