	
## Reto calculadora

### OBJETIVO 

- Utilizar distintos tipos de datos
- Utilizar operadores lógicos y algebraicos
- Escribir estructuras condicionales
- Leer y escribir cadenas de texto


#### REQUISITOS 

1. Python 3

#### DESARROLLO

Crea una calculadora:

1. Se deben solicitar al usuario dos números
1. Se puede seleccionar entre diferentes operaciones(suma, resta, multiplicación y división).
1. Obtener el resultado de la operación solicitada
1. Considerar división entre cero
1. Considerar caracteres no definidos como operaciones
1. Imprimir resultados

Ejemplo de resultado:

```bash
$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 31
Selecciona la operación a realizar +, -, *, /: +

El resultado de 11.0 + 31.0 = 42.0

$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 31
Selecciona la operación a realizar +, -, *, /: -

El resultado de 11.0 - 31.0 = -20.0

$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 31
Selecciona la operación a realizar +, -, *, /: *

El resultado de 11.0 * 31.0 = 341.0

$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 31
Selecciona la operación a realizar +, -, *, /: /

El resultado de 11.0 / 31.0 = 0.3548387096774194

$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 0
Selecciona la operación a realizar +, -, *, /: /
Error: en una división el denominador no puede ser cero

$ python calculadora.py 
Escribe el número 1: 11
Escribe el número 2: 31
Selecciona la operación a realizar +, -, *, /: x
Error: operación no definida
```
