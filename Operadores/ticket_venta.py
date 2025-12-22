print('*** Gerenación Ticket de Venta ***')

precio_leche = float(input('Ingresa el precio de la leche: '))
precio_pan = float(input('Ingresa el precio de la pan: '))
precio_lechuga = float(input('Ingresa el precio de la lechuga: '))
precio_platano = float(input('Ingresa el precio de la platano: '))

# Descuento aplicado
descuento_porcentaje = int(input('Ingresa el descuento (%): '))


# Cálculo de subtotal (Sin inpuestos)

subtotal  = precio_leche + precio_pan + precio_lechuga + precio_platano

# Amplicar descuento
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Calculo con impuseto (21%)
impuesto = subtotal_con_descuento * 0.21

# Calculo total de la compra (Con impuesto)
costo_total_compra = subtotal_con_descuento + impuesto

print(f'''
Subtotal: ${subtotal:.2f}
Descuento: ${descuento:.2f} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento:.2f}
Impuesto (21%): ${impuesto:.2f}
Total: ${costo_total_compra:.2f}''')
