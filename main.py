
def converter(number):
    symbols = {'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
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
            result = ''
            for k, v in symbols.items():
                while number >= v:
                    result += k
                    number -= v
                if number == 0:
                    break
            return result
                    


