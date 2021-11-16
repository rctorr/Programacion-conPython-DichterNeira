import os
import sqlite3

class ArchivosDB():
    pass
        

def main():
    """ función principal del módulo """
    r_archivos = (
        (12345, "01-02-2021 01:02:03", "uno.txt"),
        (23456, "01-02-2021 01:02:03", "dos.txt"),
        (34567, "02-02-2021 03:02:03", "tres.py"),
        (45678, "03-02-2021 05:02:03", "cuatro.csv"),
        (4512, "10-03-2021 09:02:03", "cinco.json")
    )
    DB = "test.sqlite3"
    t_archivos = "Archivo"
    c_archivos = (
        "tamanio INTEGERT",
        "fecha VARCHAR(19)",
        "nombre VARCHAR(512)"
    )

    archivos_db = ArchivosDB(DB)
    archivos_db.crear_tabla(t_archivos, c_archivos)
    archivos_db.insertar(t_archivos, r_archivos)
    for reg in archivos_db.listar_todo(t_archivos):
        print( "{:5}  {:10}  {}  {}".format(*reg) )
    archivos_db.cerrar()
    if os.path.exists(DB):
        os.remove(DB)


if __name__ == "__main__":
    main()