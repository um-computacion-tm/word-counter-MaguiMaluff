import unittest

def count_words(frase):
    result = {}
    list = frase.split(' ')
    for word in list:
            if word == '':
                return "Sin palabras"
            else:
                result[word] = 1
    return result

    
if __name__ == '__main__':
    unittest.main()