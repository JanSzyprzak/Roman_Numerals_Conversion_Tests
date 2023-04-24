from main import converter

def test_import_converter():
    try: 
        assert callable(converter), "converter is not callable"  
    except ImportError as error:  
        assert False, error


def test_if_converter_accepts_one_argument():
    argument = 1
    try:
        converter(argument)
    except TypeError:
        assert False, "Converter accepts one argument"

def test_if_converter_converts_basic_roman_numerals_to_int():
    numerals = converter("D")
    assert type(numerals) == int 

def test_if_converter_converts_int_to_basic_roman_numerals():
    numeral = converter(500)
    assert type(numeral) == str 

def test_if_converter_converts_complex_roman_numerals_to_int():
    numeral = converter("MDCCLIX")
    assert numeral == 1759

def test_if_converter_converts_complex_int_into_roman_numerals():
    numeral = converter(1759)
    assert numeral == "MDCCLIX"