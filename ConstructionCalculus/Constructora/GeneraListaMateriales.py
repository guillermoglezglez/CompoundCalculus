from ConstructionCalculus.Constructora import ElementosConstructivos as c
from ConstructionCalculus.Constructora import IntercambioDimensional as u
from ConstructionCalculus.Constructora import EspecificacionesMateriales as material
from ConstructionCalculus.Constructora import CalculadoraMateriales as calculate

from ConstructionCalculus.Constructora.EspecificacionesMateriales import ladrillo, bloque


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

material_ParedTabiquesCerramiento_metros(ladrillo,1,1)
material_ParedTabiquesCerramiento_metros(bloque,1,1)