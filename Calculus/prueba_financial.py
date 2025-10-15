from FinancialCalculus import DenominacionMoneda as denominacion

monedas = [10,5,2,1,0.50]
cantidadMonedas = [100,100,100,100,100]
billetes = [1000,500,200,100,50,20]
cantidadBilletes = [100,100,100,100,100,100]
nombre = "peso"
pais = "Mexico"

MXN = denominacion.divisa(monedas,billetes,nombre,pais)
cajaMXN = denominacion.caja(MXN,cantidadMonedas,cantidadBilletes)
cambio = denominacion.generaCambio(100,120,cajaMXN)
print(cambio)

monedas = [0.50,0.25]
cantidadMonedas = [100,100]
billetes = [100,50,20,5,2,1]
cantidadMonedas = [100,100,100,100,100,100]
nombre = "dolar"
pais = "USA"

USD = denominacion.divisa(monedas,billetes,nombre,pais)


print(MXN)
print(USD)