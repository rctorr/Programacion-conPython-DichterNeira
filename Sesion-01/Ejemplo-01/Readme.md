# Haz tu primera aplicación con python

¡Bienvenido a Python! Python es un lenguaje de programación de alto nivel, fácil de usar, versátil y potente. Es uno de los lenguajes más populares actualmente según el ínidce de TIOBE:


## Objetivo

* Conocer la sintaxis básica de Python, variables y tipos de datos; operadores lógicos y condiciones, así como ciclos de control.

## Usos

Python tiene diversos campos de aplicación:
 - Aplicaciones web (Flask, Django...)
 - Aplicaciones multiplataforma (PyQt, TCL, click..)
 - Aplicaciones móviles (Kivy)
 - Electrónica, IOT (Micropython)
 - Data science (List, NumPy, Pandas, Tensorflow, Scipy...)
 - Robótica (ROS)
 - ...

## Instalación

La instalación dependerá del sistema operativo que tengamos. Para este curso, cualquier versión superior a Python 3.5 es válida para seguirlo, además es importante conocer que la instalación de **Python** se puede realizar de varias formas, sin embargo para éste curso, se instalará la versión conocida como **Python Miniconda**, que inicialmente fué pensado sólo para hacer Ciencia de Datos, pero hoy en día se puede usar para desarrollar cualquier tarea que se necesiten.

El sitio para descargar e instalar es: https://docs.conda.io/en/latest/miniconda.html

En la primer tabla están los links de descarga para cada sistema operativo:

- Para usuarios con MacOSX descargen del link que dice bash al final
- Para usuario con Linux descarguen la que dice sólo Miniconda Linux 64 bit
- Para usuarios con Windows descarguen la que corresponda a su sistema operativo, que hoy en día es casi seguro la que termina en 64-bit.

Ahora para usuarios con Windows se descargará un archivo ejecutable (.exe) que le pueden dar doble click y dar click en siguiente dejado seleccionadas las opciones por omisión hasta que termines el proceso de instalación, para verificar que su instalación ha sido exitosa buscar la aplicación o programa **Anaconda Prompt** y ejecutarlo, esto abrirá una ventana con fondo obscuro conocida como Consola o Terminal donde podremos ejecutar comandos, por ejemplo escribe el siguiente comando y presionar ENTER:

```
C:/users/rctorr> python -V
Python 3.9.5
```
El texto `C:/users/rctorr>` es el prompt o señal del sistema operativo, se imprime en automático y puede cambiar dependiendo de la versión del Window, idioma o configuración.

El texto `python -V` es el comando que deberás de escribir y al terminar presionar la tecla ENTER

El texto `Python 3.9.5` es la respuesta de la ejecución del comando.

También puedes descargar [Ubuntu para Windows 10](https://www.microsoft.com/es-mx/p/ubuntu/9nblggh4msv6), y así tener un sistema Linux en tu equipo accesible desde Windows.

Para usuarios con Linux o MacOSX el procedimiento de instalación no es dando doble click, si no por medio del uso del programa la **Terminal** y la ejecución de algunos comandos como se muestra a continuación, recuerda presionar la tecla ENTER tras escribir cada comando:

1. Abrir la aplicación Terminal
1. Cambiarse a la carpeta de descargas por lo general se puede realizar con el comando: `cd Downloads`
1. Iniciar la instalación con el comando: `bash Miniconda3-latest-MacOSX-x86_64.sh` para usuarios Mac OSX o `bash Miniconda3-latest-Linux-x86_64.sh` para usuarios Linux, esto mostrará la licencia en pantalla que se puede leer presionando la tecla de **Espacio** y luego aceptando los términos.
1. Seguir las indicaciones de la instalación hasta su término usando los valores por defecto cuando se pida escribir algo.
1. Cerrar la ventana de la Terminal y en caso de tener más Terminales abiertas cerrarlas todas, esto con la finalidad de que Miniconda pueda iniciar adecuadamente.
1. Abrir una Terminal nuevamente, entonces al inicio del prompt debe aparecer algo como lo siguiente: `(base) rctorr@gatem:~$`, notar que al inicio dice `(base)` esto es indicativo de que ya está instalado miniconda.
1. También puede verificar la instalación ejecutando el siguiente comando:

```
(base) rctorr@gatem:~$ python -V
Python 3.9.5
```
Donde el texto `rctorr@gatem:~$` es el prompt o señal del sistema operativo, se imprime en automático y puede cambiar dependiendo de la versión del Linux, Mac OS, idioma o configuración.

El texto `python -V` es el comando que deberás de escribir y al terminar presionar la tecla ENTER

El texto `Python 3.9.5` es la respuesta de la ejecución del comando.

---

## Hola mundo

Usualmente, el primer programa que se realiza al aprender un lenguaje es imprimir la frase "Hola Mundo"

En Python:

```
print("Hola Mundo")
```