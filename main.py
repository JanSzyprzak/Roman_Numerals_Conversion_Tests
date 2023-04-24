
def converter(number):
    symbols = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1

        }
    
    if type(number)==str:
        number = set(number)
        
        result = 0
        for k, v in symbols.items():
            if k in number:
                result += v
        return int(result)
    
    elif type(number)==int:
        result = 0
        for k, v in symbols.items():
            if v == number:
                result = k
                return result