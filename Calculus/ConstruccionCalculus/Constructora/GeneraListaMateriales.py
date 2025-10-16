from Calculus.ConstruccionCalculus.Constructora import ElementosConstructivos as c
from Calculus.ConstruccionCalculus.Constructora import IntercambioDimensional as u
from Calculus.ConstruccionCalculus.Constructora import EspecificacionesMateriales as material
from Calculus.ConstruccionCalculus.Constructora import CalculadoraMateriales as calculate


def paredTabiquesVigasCerramiento_metros(tabique,alto,largo):
    pared = c.pared(u.m(alto),u.m(largo),tabique,material.vigaMuro,material.cerramientoComun)
    return pared

def material_ParedTabiquesCerramiento_metros(tabique,altoPared,largoPared):
    nombreTabique = tabique[5]+"s"
    paredPatioTabique = paredTabiquesVigasCerramiento_metros(tabique,altoPared,largoPared)
    numeroDeLineas = paredPatioTabique[0]
    tabiquesPorLinea = paredPatioTabique[1]

    print("Para una pared de",nombreTabique,"con un largo x altura (",largoPared,"m x",altoPared,"m ).")
    print("- Se requieren:",numeroDeLineas,"lineas de",tabiquesPorLinea,nombreTabique)
    print("   Total de",calculate.cantidadTabiques(paredPatioTabique),nombreTabique)
