import click
import os
import time

class Archivo():
    def __init__(self, ruta):
        """ Crea un objeto Archivo a partir de ruta """
        self.__ruta = ruta
        try:
            self.tamanio = os.path.getsize(ruta)
            self.fecha = os.path.getmtime(ruta)
        except FileNotFoundError:
            pass
        except OSError:
            pass

    @property
    def get_ruta(self):
        """ Obtiene el valor de ruta """
        return self.__ruta
    
    @property
    def fecha_str(self):
        """ Regresa la fecha en formato str """
        return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(self.fecha) )

    def __str__(self):
        """ Define la represrentación en str de Archivo """
        return self.__ruta

    def texto(self):
        """ Representación en texto plano de un Archivo """
        fecha: tuple = time.localtime(self.fecha)
        fecha: str = time.strftime("%d-%m-%Y %H:%M:%S", fecha)
        return f"{self.tamanio:12}  {fecha:19}  {self.__ruta}"
    
    @property
    def tupla_str(self):
        """ Representación en tupla de los atributos de un Archivo """
        return (self.tamanio, self.fecha_str, self.__ruta)

    
class Carpeta(Archivo):
    def lista_elementos(self):
        """ Obtener la lista de elementos de la Carpeta """
        try:
            archivos: list = os.listdir(self.get_ruta)  # archivos -> ["uno.py", "dos.py", ...]
        except PermissionError:
            archivos = []
        # elementos -> [Archivo("uno.py"), Archivo("dos.py"), Carpeta("datos"), ....]
        elementos = []
        for arch in archivos:
            # arch -> ruta + "uno.py", "datos"
            ruta = os.path.join(self.get_ruta, arch)  # "/home/rcotrr/uno.py"
            if os.path.isdir(ruta):
                carpeta = Carpeta(ruta)
                elementos.append( carpeta )
                # elementos = elementos + Carpeta(ruta).lista_elementos()
                elementos += carpeta.lista_elementos()
                # i = i + 1
                # i += 5
                # i -= 5
                # i *= 2 -> i = i * 2
                # i++ <- No existe en Python
            else:
                elementos.append( Archivo(ruta) )
        return elementos

    def texto(self):
        """ Representación en texto plano de un Archivo """
        return super().texto() + "/"


def imprime_en_texto(lista):
    """
    Imprime los elementos de lista en la salida estándar en
    formato texto plano.
    """
    for arch in lista:  # lista -> [Archivo(), Carpeta(), Archuvo(), ...]
        # type(arch) ? , str [x], Archivo() o Carpeta()
        print( arch.texto() )

def guarda_en_archivo(lista, ruta):
    """
    Guarda los elementos de lista en el archivo en ruta en formato texto
    """
    with open(ruta, "w") as arch_texto:
        for elemento in lista:  # lista -> [Archivo(), Carpeta(), Archuvo(), ...]
            # type(arch) ? , str [x], Archivo() o Carpeta()
            # arch_texto.write(elemento.texto())
            # arch_texto.write("\n")
            arch_texto.write(elemento.texto() + "\n")

def genera_html(lista):
    """ Genera una cadena con la lista formateada usando HTML """
    filas = []
    for arch in lista:
        columnas = ""
        for col in arch.tupla_str:
            columnas += f"<td>{col}</td>"
        fila = f"<tr>{columnas}</tr>"
        filas.append(fila)
    filas: str = "\n".join(filas)
    html = f"""
    <!doctype html>
    <html>
    <body>
    <h2>Lista de archivos</h2>
    <table>
    <tr><th>Tamaño</th><th>Fecha</th><th>Nombre</th></tr>
    {filas}
    </table>
    </body>
    </html>
    """
    
    return html
    

@click.command()
@click.argument("carpeta", default=".", type=click.Path(exists=True))
def main(carpeta):
    """
    Imprime la lista de archivos y carpetas de la carpeta actual o de la
    CARPETA proporcionada por el usuario.
    """
    carpeta_obj = Carpeta(carpeta)
    elementos: list = carpeta_obj.lista_elementos()
    # imprime_en_texto(elementos)
    guarda_en_archivo(elementos, "salida.txt")

if __name__ == '__main__':
    main()
