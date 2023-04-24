
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
    
    result = 0
    for k, v in symbols.items():
        
        if type(number)==str:     
            previous_value = 0 
            for l in number:
                value = symbols[l]
                if value > previous_value:
                    result += value - 2 * previous_value
                else:
                    result += value
                previous_value = value
            return result


        elif type(number)==int:
            if v == number:
                result = k
                return result
            


