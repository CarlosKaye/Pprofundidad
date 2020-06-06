
import json
with open('base.json') as file:
	data = json.load(file)
ruta=[]

def primeroProfundidad(Carpeta,Archivo):
	
	if Carpeta == Archivo:
		return Archivo
		
	for d in data:
		if d[0] == Carpeta:
			ruta.append(Carpeta)
			arch=primeroProfundidad(d[1],Archivo)
			if arch:
				return arch
	if ruta:
		ruta.pop()


arch=primeroProfundidad("C:","ElMejorPorreoInteso.mp3"
)
rut = ""
if arch:
	for x in ruta:
		rut=rut+x+"/"
	rut=rut+arch
	print(rut)
else:
	print("No existe")

