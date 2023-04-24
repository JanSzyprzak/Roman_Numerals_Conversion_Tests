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