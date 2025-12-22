print('*** Sistema de Autenticación ***')

# Constantes
USUARIO_VALIDO = 'Admin'
CONTRASENA_VALIDA = '1234'

# Solicitud de datos
usuario_ingresado = input('Ingresa su usuario: ')
contrasena_ingresada = input('Ingresa su contraseña: ')

# Validacion

validos = (USUARIO_VALIDO == usuario_ingresado.strip() and
           CONTRASENA_VALIDA == contrasena_ingresada.strip())

# Salida
print("Datos correctos: ", validos)
