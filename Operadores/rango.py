# Script que verifica si un valor esta entre el rango 0 a 5
print("*** Valor dentro de rengo ***")
# Definición de Constantes
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

# Solicitar valor al usuario
valor = int(input(f"Introduce un valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: "))

# Verificar si está en rango
dentro_rengo = (valor >= VALOR_MINIMO) and (valor <= VALOR_MAXIMO)

# Imprimir resultado
print(f"Se encuentra el valor {valor} dentro de rango? {dentro_rengo}")