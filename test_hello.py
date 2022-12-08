import hello

def test_hello():
    assert hello.hello('Loïs') == 'Hello Loïs'
    assert hello.hello('') == 'Hello '
    assert hello.hello(5) == 'Hello 5'
    assert hello.hello(5.5) == 'Hello 5.5'
    assert hello.hello(True) == 'Hello True'