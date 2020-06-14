#Listas y tuplas anidadas
def cargar_paises_poblacion():
	paises = []
	for x in range(5):
		nom = input("Ingrese el nombre del país: ")
		cant = input("Ingrese la cantidad de habitantes: ")
		paises.append((nom, cant))
	return paises

def imprimir(paises):
	print("Países y su población: ")
	for x in range(len(paises)):
		print(paises[x][0], paises[x][1])

def pais_mas_poblacion(paises):
	pos = 0
	for x in range(1, len(paises)):
		if paises[x][1] > paises[pos][1]:
			pos = x
	print("País con mayor cantidad de habitantes: ", paises[pos][0])


paises = cargar_paises_poblacion()
imprimir(paises)
pais_mas_poblacion(paises)