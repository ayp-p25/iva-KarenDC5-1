"""
Calcular IVA y total con IVA
Karen Durán
757136
Ingeniería Civil
Algoritmos y Programación 
ESI232B2
14/02/25
5 minutos 
"""

# Declaraciones
TASA_IVA = 0.16

# Entradas
cantidad = float(input("Cantidad: "))

# Proceso
iva = cantidad * TASA_IVA
total_con_iva = cantidad + iva

# Salidas
print("IVA", iva)
print("Total", total_con_iva)
