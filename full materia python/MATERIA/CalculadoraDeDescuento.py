# Solicitar al usuario el precio original del producto
precio_original = float(input("Ingrese el precio original del producto: "))

# Calcular el precio con descuento (40%)
descuento = 0.4
precio_descuento = precio_original * (1 - descuento)

# Calcular el IVA (16%)
iva = 0.16
subtotal = precio_descuento
total = subtotal * (1 + iva)

# Mostrar los resultados
print(f"Subtotal (precio con descuento): ${precio_descuento:.2f}")
print(f"Total (incluyendo IVA al 16%): ${total:.2f}")
