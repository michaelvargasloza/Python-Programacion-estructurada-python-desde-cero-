#Porciones de listas, tuplas y cadenas de caracteres
def meses_faltantes(numero):
	meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
	return meses[numero:]

print("Imprimir los nombres de meses que faltan hasta fin de año:")
numero = int(input("Ingrese el número de mes: "))
mesesfalta = meses_faltantes(numero)
print(mesesfalta)