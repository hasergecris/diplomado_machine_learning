#Integrantes
"""
-	CRISTIAN CAMILO VEGA MORALES
-	DIDIER DAVID SANTAMARIA BENITEZ
-	DUMAR SULVARAN JIMENEZ
-	ALEX FERNEY RONDON CALDERON
-	WILVER JULIAN MARTIN JIMENEZ.

"""

# Definir los tipos de divisas y sus valores en relación a una divisa base (en este caso, USD)
divisas = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.75,
    'CAD': 1.2,
    'AUD': 1.3,
    'JPY': 1.8
}

# Mostrar las divisas disponibles al usuario
print("Divisas disponibles:")
for divisa in divisas:
    print(divisa)

# Obtener la divisa de origen y destino del usuario
divisa_origen = input("Ingrese la divisa de origen: ")
divisa_destino = input("Ingrese la divisa de destino: ")

# Verificar si las divisas ingresadas son válidas
if divisa_origen not in divisas or divisa_destino not in divisas:
    print("Las divisas ingresadas no son válidas.")
    exit()

# Obtener el monto a cambiar
monto_origen = float(input("Ingrese el monto a cambiar: "))

# Calcular el monto en la divisa de destino
monto_destino = monto_origen / divisas[divisa_origen] * divisas[divisa_destino]

# Calcular la ganancia para el comprador y el vendedor
ganancia_comprador = monto_origen - monto_destino
ganancia_vendedor = monto_destino - monto_origen

# Mostrar los resultados
print("Monto en", divisa_destino + ":", monto_destino)
print("Ganancia para el comprador:", ganancia_comprador)
print("Ganancia para el vendedor:", ganancia_vendedor)
