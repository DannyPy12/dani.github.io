from src.calculadora import sum, resta,multiplicacion,division, num_par

def test_sum():
    assert sum(4, 5) == 9

def test_resta():
    assert resta(8, 3) == 5

def test_multiplicacion():
    assert multiplicacion(3, 7) == 21

def test_division():
    assert division(10, 2) == 5

def test_num_par():
    assert num_par(4) == True
    assert num_par(5) == False