var = 10
def function_1():
    global var
    var = var + 1
    print(var)

function_1()

def function_2():
    loc = var
    loc = loc + 1
    print(var)

function_2()
