from ConstructionCalculus.Constructora import IntercambioDimensional as u

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
