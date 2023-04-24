
def converter(number):
    if type(number)==str:
        number = set(number)
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
            if k in number:
                result += v
        return int(result)
    