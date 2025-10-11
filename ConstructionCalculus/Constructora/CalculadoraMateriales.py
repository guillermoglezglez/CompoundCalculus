import math
from ConstructionCalculus.Constructora.EspecificacionesMateriales import ladrillo,bloque,vigaMuro,cerramientoComun
from ConstructionCalculus.Constructora.ElementosConstructivos import pared

def cantidadTabiques(pared):
    ladrillosAlto = pared[0]
    parteEnteraLargoPared = int(pared[1])
    fragmentoTabique = pared[1] - parteEnteraLargoPared
    # Falta considerar la merma al cortar los tabiques
    fragmentosTabique = math.ceil(fragmentoTabique * ladrillosAlto)

    ladrillos = ladrillosAlto * parteEnteraLargoPared + fragmentosTabique
    return ladrillos

muroLadrillo = pared(100,100,ladrillo,vigaMuro,cerramientoComun)
muroBloque = pared(100,100,bloque,vigaMuro,cerramientoComun)
print(cantidadTabiques(muroLadrillo))
print(cantidadTabiques(muroBloque))