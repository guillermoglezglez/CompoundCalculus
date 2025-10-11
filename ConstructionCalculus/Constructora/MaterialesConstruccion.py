import IntercambioDimensional as u

def varilla(numero,nombre):
    fraccion = 8
    grosor = u.inch(numero,fraccion) # 3 : 3/8 in
    inches = numero,fraccion
    return grosor,inches,nombre

def tabique(espesor,alto,largo,union,lineas,nombre):
    return [espesor,alto,largo,union,lineas,nombre]

def viga(varilla,cantidadVarillasALoLargo,separacion,camisa,nombre):
    cantidadDeSeparaciones = cantidadVarillasALoLargo - 1
    varillaEnCentimetros = varilla[0]
    ancho = varillaEnCentimetros * cantidadVarillasALoLargo + separacion * (cantidadDeSeparaciones) + 2 * camisa
    return ancho

def cerramiento(altura):
    return(altura)

def cerramiento(estructura,camisa,nombre):
    alturaCerramiento = estructura + 2 * (camisa)
    return(alturaCerramiento,camisa,nombre)

union = 1
camisa = 3
bloque = tabique(15, 20, 40, union, 12, "bloque")
ladrillo = tabique(14,7,25,union,20,"ladrillo")
lego = tabique(10,10,20,union,25,"lego")
varillaN3 = varilla(3,"varilla corrugada #3")
varillaN5 = varilla(5,"varilla corrugada #5")
vigaMuro = viga(varillaN3,2,20,camisa,"viga muro")
vigaCarga = viga(varillaN5,3,20,camisa, "viga carga")

cerramientoComun = cerramiento(20,camisa,"cerramiento comun")

print(bloque)
print(ladrillo)
print(lego)
print(varillaN3)
print(varillaN5)
print(vigaMuro)
print(vigaCarga)

print(cerramientoComun)
