import math
from Calculus.ConstruccionCalculus.Constructora.EspecificacionesMateriales import ladrillo,bloque,vigaMuro,cerramientoComun
from Calculus.ConstruccionCalculus.Constructora.ElementosConstructivos import pared

def cantidadTabiques(pared):
    ladrillosAlto = pared[0]
    parteEnteraLargoPared = int(pared[1])
    fragmentoTabique = pared[1] - parteEnteraLargoPared
    # Falta considerar la merma al cortar los tabiques
    fragmentosTabique = math.ceil(fragmentoTabique * ladrillosAlto)

    ladrillos = ladrillosAlto * parteEnteraLargoPared + fragmentosTabique
    return ladrillos
