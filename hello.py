def hello(name):
    if (name == ''):
        raise Exception("The name can not be empty !")
    if (len(name) > 30):
        raise Exception("The name can not have more than 30 characters !")
    return "Hello " + name