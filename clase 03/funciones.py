def quejar():
    print("¡No viene la luz!")

def valASCII(caracter):
    return ord(caracter)

def funcionIncompleta():
    pass

def conParametro(num1, num2):
    #if(type(num2)int(int, float))
    if(type(num1) == int and type(num2) == int):
        return num1 + num2
    else:
        return "los valores enviados deberian ser enteros"
    
quejar()

print(valASCII("a"))
