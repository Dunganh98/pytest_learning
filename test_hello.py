from hello import sayHi, sayHello


def test_say_hi():
    assert "Hi" == sayHi()


def test_say_hello():
    assert "Hello" == sayHello()
