from Calculus.FinancialCalculus import DenominacionMoneda as denominacion

monedas = [0.50,0.25,0.10,0.05,0.01]
cantidadMonedas = [100,100,100,100,100]
billetes = [100,50,20,5,2,1]
cantidadBilletes = [100,100,100,100,100,100]
nombre = "dolar"
pais = "USA"

USD = denominacion.divisa(monedas,billetes,nombre,pais)
cajaUSD = denominacion.caja(USD,cantidadMonedas,cantidadBilletes)
cambio = denominacion.generaCambio(100,122.50,cajaUSD)
print(cambio)

print(USD)