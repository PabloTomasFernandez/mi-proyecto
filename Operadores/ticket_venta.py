print('*** Gerenación Ticket de Venta ***')

precio_leche = float(input('Ingresa el precio de la leche: '))
precio_pan = float(input('Ingresa el precio de la pan: '))
precio_lechuga = float(input('Ingresa el precio de la lechuga: '))
precio_platano = float(input('Ingresa el precio de la platano: '))


# Cálculo de subtotal (Sin inpuestos)

subtotal  = precio_leche + precio_pan + precio_lechuga + precio_platano

# Calculo con impuseto (21%)
impuesto = subtotal * 0.21

# Calculo total de la compra (Con impuesto)
costo_total_compra = subtotal + impuesto

print(f'''
Subtotal: ${subtotal:.2f}
Impuesto: ${impuesto:.2f}
Total: ${costo_total_compra:.2f}''')
