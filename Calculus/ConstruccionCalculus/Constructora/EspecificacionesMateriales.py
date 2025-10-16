from Calculus.ConstruccionCalculus.Constructora import MaterialesConstruccion as matCons

# Unidad centimetros
# Block    espesor 10 15 20 altura 20 largo 40 metro 12.5 pz 16  lineas 12
# Ladrillo espesor 14       altura 7  largo 25 metro 50   pz 6   lineas 20

# union de 1 a 1.2 cm

union = 1
camisa = 3
bloque = matCons.tabique(15, 20, 40, union, 12, "bloque")
ladrillo = matCons.tabique(14,7,25,union,20,"ladrillo")
lego = matCons.tabique(10,10,20,union,25,"lego")
varillaN3 = matCons.varilla(3,"varilla corrugada #3")
varillaN5 = matCons.varilla(5,"varilla corrugada #5")
vigaMuro = matCons.viga(varillaN3,2,20,camisa,"viga muro")
vigaCarga = matCons.viga(varillaN5,3,20,camisa, "viga carga")

cerramientoComun = matCons.cerramiento(20,camisa,"cerramiento comun")