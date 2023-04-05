import unittest
from words import count_words

class TestCountWords(unittest.TestCase):
    def test_simple0(self):
        result = count_words(' ')
        self.assertEqual(result, "Sin palabras")
    def test_simple00(self):
        result = count_words('  ')
        self.assertEqual(result, "Sin palabras")
    def test_simple1(self):
        result = count_words('hola')
        self.assertEqual(result, {'hola':1})
    def test_dificl(self):
        result = count_words('hola mundo')
        self.assertEqual(result, 
                {'hola':1,
                 'mundo':1,})
    def test_dificil2(self):
        result = count_words('hola mi mundo')
        self.assertEqual(result, 
                {'hola':1,
                 'mundo':1,
                 'mi': 1})
    def test_dificil8(self):
        result = count_words("hola mundo, yo soy un perro que habla")
        self.assertEqual(result, 
                {'hola':1,
                 'mundo,':1,
                 'yo':1,
                 'soy':1,
                 'un':1,
                 'perro':1,
                 'que':1,
                 'habla':1})
    def test_dificil10(self):
        result = count_words('hola mundo, yo soy un perro que habla muchos idiomas.')
        self.assertEqual(result, 
                {'hola':1,
                 'mundo,':1,
                 'yo':1,
                 'soy':1,
                 'un':1,
                 'perro':1,
                 'que':1,
                 'habla':1,
                 'muchos':1,
                 'idiomas.':1})
    def test_difici14(self):
        result = count_words('hola mundo, yo soy un perro que habla muchos idiomas. Espanol, ingles, chino y frances.')
        self.assertEqual(result, 
                {'hola':1,
                 'mundo,':1,
                 'yo':1,
                 'soy':1,
                 'un':1,
                 'perro':1,
                 'que':1,
                 'habla':1,
                 'muchos':1,
                 'idiomas.':1,
                 'Espanol,':1,
                 'ingles,':1,
                 'chino':1,
                 'y':1,
                 'frances.':1})

if __name__ == '__main__':
    unittest.main()