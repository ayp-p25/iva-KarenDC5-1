"""
Se ingresa una cantidad sin iva y se regresa el total de la cantidad con iva
Karen Durán
757136
Ingeniería Civil
Algoritmos y Programación 
ESI232B2
14/02/25
5 minutos 
"""

# Declaraciones
tasa_iva = 0.16

# Entradas
cantidad = float(input("Ingrese la cantidad sin IVA:"))

# Proceso
iva = cantidad * tasa_iva
total = cantidad + iva

# Salidas
print("Total", total)
