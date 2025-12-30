# 🐍 Portafolio de Ejercicios en Python

Bienvenido a mi repositorio de prácticas de desarrollo profesional en Python. Este proyecto compila algoritmos de lógica, estructuras de control (condicionales y bucles) y simulaciones de sistemas reales, todo organizado profesionalmente en la carpeta `src/`.

## 📂 Contenido del Proyecto

### 🏧 Sistemas Interactivos y Juegos (Ciclos `while` y `for`)
Aplicaciones que mantienen una interacción continua con el usuario mediante menús y bucles:

* **`src/cajero_automatico.py`**: Simulación completa de cajero con saldo persistente, depósitos, retiros y validaciones de fondos.
* **`src/calculadora.py`**: Calculadora aritmética con menú iterativo que permite realizar múltiples operaciones sin salir.
* **`src/juego_adivinar.py`**: Juego de "Adivina el número secreto" (1-50) con contador de intentos y pistas (mayor/menor).
* **`src/creacion_validacion_password.py`**: Validador de seguridad que obliga al usuario a crear una contraseña de mínimo 6 caracteres.
* **`src/menu_iterativo.py`**: Estructura esqueleto (plantilla) para crear menús de administración de sistemas.

### 🔄 Algoritmos de Repetición y Patrones
Ejercicios enfocados en el uso técnico de `for`, `range`, `break` y `continue`:

* **`src/dibujar_triangulo.py`**: Generador de patrones visuales (pirámide de asteriscos) según el número de filas.
* **`src/suma_acumulativa.py`**: Demostración de acumuladores dentro de un ciclo `while` para sumar series de números.
* **`src/imprimir_mensaje_range.py`**: Uso básico de `range()` para repetición controlada de tareas.
* **`src/break_continue.py`**: Ejemplo técnico de cómo interrumpir (`break`) o saltar (`continue`) iteraciones en un ciclo.

### 🏢 Logística y Negocios (Condicionales `if/elif`)
Scripts que resuelven lógica de negocio específica:

* **`src/sistema_envios.py`**: Calculadora de tarifas logísticas (Nacional/Internacional) según peso.
* **`src/tienda_linea_descuentos.py`**: Motor de descuentos para e-commerce según monto y membresía.
* **`src/reserva_hotel.py`**: Cotizador de estancias con tarifas dinámicas (vista al mar vs estándar).
* **`src/ticket_venta.py`**: Generador de recibos de compra con cálculo de impuestos y subtotales.

### 🔐 Seguridad y Salud
* **`src/sistema_autenticacion.py`**: Login robusto con mensajes de error específicos (usuario vs password).
* **`src/aplicacion_salud_fitness.py`**: App de salud para cálculo de calorías y metas de pasos.
* **`src/sistema_bancario.py`**: Flujo básico de salida segura de un sistema.
* **`src/authentication_system.py`**: Versión básica de validación de credenciales.

### 🧠 Lógica y Conversiones
* **`src/estacion_anio.py`**: Determinador de estación según el mes numérico.
* **`src/sistema_calificaciones.py`**: Conversor de notas numéricas a letras (A-F).
* **`src/rango.py`**: Validador booleano de límites numéricos.
* **`src/operador_ternario.py`**: Simplificación de condicionales en una línea.

---

## 🚀 Instrucciones de Ejecución

Todos los scripts están en la carpeta `src`. Para probar las aplicaciones interactivas (como el cajero), ejecuta:

```bash
# Ejemplo: Iniciar el Cajero Automático
python src/cajero_automatico.py

# Ejemplo: Iniciar el Juego de Adivinanza
python src/juego_adivinar.py
```