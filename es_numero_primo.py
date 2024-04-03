import unittest
#clase 20/03
"""def suma (valor):
    return 1
def suma_de_los_valores_anteriores (valor):
    result = valor
    while result > 0 :
        valor = valor -1
        result = result + valor #si ejecuto un break dentro del while salgo del while de una, el continue vuelve a la condicion y vuelve a empezar
    return result"""
def es_primo(value):
    divisor = value - 1
    while divisor > 1:
        if value  % divisor ==0:
            return False
        divisor=divisor-1
    return True
class TestSumadeprimos (unittest.TestCase):
    def test_num_primo_1(self):
        result = es_primo(1)
        self.assertTrue(result)
    
    def test_num_primo_2(self):
        result = es_primo(2)
        self.assertTrue(result)
    
    def test_num_primo_3(self):
        result = es_primo(3)
        self.assertTrue(result)
    
    def test_num_primo_4(self): #4 no es primo
        result = es_primo(4)
        self.assertFalse(result) 

    def test_num_primo_5(self):
        result = es_primo(5)
        self.assertTrue(result)

    def test_num_primo_6(self):
        result = es_primo(6)
        self.assertFalse(result)
unittest.main()

