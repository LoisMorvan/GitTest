from hello import hello

def test_hello_prenom_normal():
    name = 'Loïs'
    result = hello(name)
    assert result == 'Hello Loïs'

def test_hello_aucun_prenom():
    name = ''
    try:
        hello(name)
    except Exception as EmptyName:
        assert True, EmptyName

def test_hello_too_long():
    name = 'SuperSuperSuperSuperSuperSuper'
    try:
        hello(name)
    except Exception as TooLong:
        assert True, TooLong