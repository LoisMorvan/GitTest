import hello

def test_hello():
    assert hello.hello('Loïs') == 'Hello Loïs'
    assert hello.hello('') == Exception
    assert hello.hello('SuperSuperSuperSuperSuperSuper') == Exception