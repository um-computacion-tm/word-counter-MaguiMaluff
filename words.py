import unittest

def count_words(frase):
    result = {}
    list = frase.split(' ')
    for word in list:
        lower_word = word.lower()
        if lower_word == '':
            return "Sin palabras"
        elif lower_word in result:
            result[lower_word] += 1
        else:
            result[lower_word] = 1
    return result

    
if __name__ == '__main__':
    unittest.main()