import math
from ConstruccionCalculus.Constructora import IntercambioDimensional as u
from ConstruccionCalculus.Constructora.EspecificacionesMateriales import ladrillo, vigaMuro, bloque,cerramientoComun


def pared(alto,largo,tabique,viga,cerramiento):
    largoConVigasEstandar = u.m(2.4)

    # Distancia entre columnas no mayor al doble de la altura del muro
    altoTabique = tabique[1]
    largoTabique = tabique[2]
    union = tabique[3]
    cantidadDeLineas = tabique[4]

    alturaDelCerramiento = cerramiento[0]

    #Muro solo ladrillo
    alturaMuroEstandar = (altoTabique + union) * cantidadDeLineas
    largoMuroEstandar = largoConVigasEstandar - 2 * viga
    largoVigaMuro = viga + largoMuroEstandar

    if(alto <= alturaMuroEstandar):
        altoMuroLadrillos = alto
    else:
        altoMuroLadrillos = alto - alturaDelCerramiento
    ladrillosAltura = math.ceil(altoMuroLadrillos / (altoTabique + union))

    if(largo <= largoConVigasEstandar):
        cantidadMuros = 0
    else:
        cantidadMuros = int((largo - viga) / largoVigaMuro)

    largoMuroExtra = largo - (largoMuroEstandar * cantidadMuros)
    largoMuroLadrillos = cantidadMuros + largoMuroExtra
    ladrillosLargo = round(largoMuroLadrillos / (largoTabique + union),2)

    return [ladrillosAltura,ladrillosLargo]