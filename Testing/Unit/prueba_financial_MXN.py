from Calculus.FinancialCalculus import DenominacionMoneda as denominacion

monedas = [10,5,2,1,0.50]
cantidadMonedas = [100,100,100,100,100]
billetes = [1000,500,200,100,50,20]
cantidadBilletes = [100,100,100,100,100,100]
nombre = "peso"
pais = "Mexico"

MXN = denominacion.divisa(monedas,billetes,nombre,pais)
cajaMXN = denominacion.caja(MXN,cantidadMonedas,cantidadBilletes)
cambio = denominacion.generaCambio(100,122.50,cajaMXN)
print(cambio)

print(MXN)