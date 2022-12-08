def hello(name):
    if (isinstance(name, int)):
        name = str(name)
    elif (isinstance(name, float)):
        name = str(name)
    elif (isinstance(name, bool)):
        name = str(name)
    return "Hello super" + name