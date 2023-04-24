from main import converter

def test_import_converter():
    try: 
        assert callable(converter), "converter is not callable"  
    except ImportError as error:  
        assert False, error


