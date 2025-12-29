print('*** Estación del Año ***')

mes = int(input('Proporciona el valor del mes (1-12): '))
estacion = None
# Revisión del mes proporcionado
if mes in [1, 2, 12]:
    estacion = 'Invierno'
elif mes in [3, 4, 5]:
    estacion = 'Primavera'
elif mes in [6, 7, 8]:
    estacion = 'Verano'
elif mes in [9, 10, 11]:
    estacion = 'Otoño'
else:
    estacion = 'Estación desconocida'
# Imprimir el resultado
print(f'La estación para el mes {mes} es {estacion}')
