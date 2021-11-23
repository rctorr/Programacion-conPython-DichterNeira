import operaciones

# Cada elemento se prueba por medio de una función
def test_suma():
    """ Definiendo batería de pruebas para suma() """
    assert operaciones.suma(2, 3) == 5
    assert operaciones.suma(3) == 3

def test_resta():
    """ Definiendo batería de pruebas para resta() """
    assert operaciones.resta(2, 3) == -1
    assert operaciones.resta(10, 3) == 7

def test_producto():
    """ Definición de batería de pruebas para producto() """
    assert operaciones.producto(1, 5) == 5
    assert operaciones.producto(5) == 5
    assert operaciones.producto(3, 5) == 15


