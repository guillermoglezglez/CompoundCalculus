from traceback import format_exception_only


def divisa(listaMonedas, listaBilletes, nombreMoneda, nombrePais):
    denominacionMonedas = listaMonedas
    denominacionBilletes = listaBilletes
    return (denominacionBilletes,denominacionMonedas,nombreMoneda, nombrePais)

def caja(divisa,cantidadDeMonedas,cantidadDeBilletes):
    errores = 0
    cantidadDeBilletesPorDenominacion = len(cantidadDeBilletes)
    cantidadDenominacionDeBilletes = len(divisa[0])
    if(cantidadDenominacionDeBilletes != cantidadDeBilletesPorDenominacion):
        errores += 1
        print("Error         cantidad De Billetes              (",cantidadDeBilletesPorDenominacion,")",cantidadDeBilletes,
              "\n difiere de   cantidad Denominacion De Billetes (",cantidadDenominacionDeBilletes,")",divisa[0])

    cantidadDeMonedasPorDenominacion = len(cantidadDeMonedas)
    cantidadDenominacionDeMonedas = len(divisa[1])
    if(cantidadDenominacionDeMonedas != cantidadDeMonedasPorDenominacion):
        errores += 1
        print("Error         cantidad De Monedas               (",cantidadDeMonedasPorDenominacion,")",cantidadDeMonedas,
              "\n difiere de   cantidad Denominacion De Monedas  (",cantidadDenominacionDeMonedas,")",divisa[0])

    if errores == 0:
        return divisa,cantidadDeBilletes,cantidadDeMonedas
    else:
        return "ERROR"

def rellenaLista(formato,valor):
    largoFormato = len(formato)
    listaVacia = formato
    for i in range(0,largoFormato):
        listaVacia[i] = valor
    return listaVacia

def generaCambio(precio,pago,cajaDivisa):
    errores = 0
    # print("precio",precio,"pago",pago,"cambio",pago-precio)
    cambio = pago - precio
    cantidadBilletesCambio = rellenaLista(cajaDivisa[1],0)
    cantidadMonedasCambio = rellenaLista(cajaDivisa[2],0)
    if(cambio == 0):
        print("Muchas gracias vuelva pronto")
    if(cambio < 0):
        print("Favor de completar el pago, usted dio",pago,"y el producto cuesta",precio)
        errores += 1
    else:
        cantidadDeBilletes = len(cajaDivisa[0][0])
        cantidadDeMonedas = len(cajaDivisa[0][0])
        for i in range(0,cantidadDeBilletes):
            denominacionBillete = cajaDivisa[0][0][i]
            # print("cambio",cambio,">=","denom Billete",denominacionBillete)
            cantidadBilletesCambio[i] = 0
            while(cambio >= denominacionBillete):
                cantidadBilletesCambio[i] += 1
                cambio -= denominacionBillete
                # print("cambio",cambio)
        return(cantidadBilletesCambio)


monedas = [10,5,2,1,0.50]
cantidadMonedas = [100,100,100,100,100]
billetes = [1000,500,200,100,50,20]
cantidadBilletes = [100,100,100,100,100,100]
nombre = "peso"
pais = "Mexico"

MXN = divisa(monedas,billetes,nombre,pais)
cajaMXN = caja(MXN,cantidadMonedas,cantidadBilletes)
aha = generaCambio(100,120,cajaMXN)


monedas = [0.50,0.25]
cantidadMonedas = [100,100]
billetes = [100,50,20,5,2,1]
cantidadMonedas = [100,100,100,100,100,100]
nombre = "dolar"
pais = "USA"

USD = divisa(monedas,billetes,nombre,pais)



