import hello

def test_hello():
    assert hello.hello('Loïs') == 'Hello Loïs'
    try:
        hello.hello('')
        assert False
    except Exception:
        assert True

    try:
        hello.hello('SuperSuperSuperSuperSuperSuper')
        assert False
    except Exception:
        assert True