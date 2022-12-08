def hello(name):
    if (isinstance(name, int)):
        name = str(name)
    elif (isinstance(name, float)):
        name = str(name)
    elif (isinstance(name, bool)):
        name = str(name)
    return "Hello " + name

def test_hello():
    assert hello('Loïs') == 'Hello Loïs'
    assert hello('') == 'Hello '
    assert hello(5) == 'Hello 5'
    assert hello(5.5) == 'Hello 5.5'
    assert hello(True) == 'Hello True'