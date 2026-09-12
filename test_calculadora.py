import calculadora

def test_add():
 #Hola, este es un comentario
    calc = calculadora.Calculadora()
    assert calc.add(2, 3) == 5
def test_multiply():
    calc = calculadora.Calculadora()
    assert calc.multiply(4, 5) == 20