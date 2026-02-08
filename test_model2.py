from model import double

def test_double_integer():
    result = double(13) #la funcion double lo definí como elevado al cuadrado
    print(f"result:{result}")
    assert 169 == result #esta es la validacion de model.py
