from model import double

def test_double_integer():
    result = double(13) #la funcion double lo definí como elevado al cuadrado
    assert 169 == result #esta es la validacion de model.py

def test_double_integer2():
    result = double(17)
    assert 289 == result #esta es la validacion
