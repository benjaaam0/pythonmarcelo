#ValorNetoDeUnProducto
producto = input("ingrese el nombre del prroducto:") 
valorProducto = int(input("ingrese el valor del producto:")) 
valorNeto = float(0.81) 
valorSinIva = float(valorProducto * valorNeto)

print(f"-----Detalle producto-----") 
print(f"NOMBRE PRODUCTO: {producto}") 
print(f"VALOR PRODUCTO: {valorProducto}") 
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}")
