from nodo import Nodo # <--- Importamos la clase Nodo del archivo nodo.py

# el comentario de una linea inicia con el simbolo de #
"""
    Este es un comentario de varias lineas
    inicia y finaliza con tres comillas dobles
"""

#Declaracion de variables
numero = 10
textoResultado = "Resultado: "
numero2 = 2
textRandom = "Random"

union = str(numero2) +textRandom
union2 = textRandom + str(numero2)

#la funcion type() nos permite saber el tipo de dato de una variable
type(numero)


print(union)
print(union2)

blnActivo = True
intEdad = 10
strNombre = "Leonel"

print(type(blnActivo))
print(type(intEdad))
print(type(strNombre))

#Concatenacion de variables en una cadena de texto
print("El valor de la variable blnActivo es: " + str(blnActivo))
print("El valor de la variable intEdad es: " + str(intEdad))
print("El valor de la variable strNombre es: " + strNombre)


#Operadores aritmeticos
# + - * / % ** //
modulo = numero % numero2
potencia = numero ** numero2

print(textoResultado + str(modulo))
print(textoResultado + str(potencia))

#Operadores relacionales
# == != > < >= <=
if numero == numero2:
    print("Los numeros son iguales")

if numero != numero2:
    print("Los numeros son diferentes")

#Operadores logicos
# and or not
if numero == numero2 and numero == 10:  
    print("Los numeros son iguales")

if numero != numero2 or numero == 10:
    print("Los numeros son diferentes")

#Operadores de asignacion
# = += -= *= /= %= **= //=
numero += 1
print(numero)

numero -= 1

numero**=numero2 #numero = numero**numero2

print(numero)

#Operadores de incremento y decremento
# ++ --
numero += 1

#arreglo (se puede modificar)
notasProyectos= [90,89,99]

for nota in notasProyectos:
    print(nota)

notasProyectos[0] = 100 #modificar el valor de una posicion del arreglo

#tupla (no se puede modificar)
notasParciales = (90,89,99)
for nota in notasParciales:
    print(nota)

#notasParciales[0] = 100 #no se puede modificar el valor de una posicion del arreglo

for i in range(0,10):
    print(i)

while numero < 10:
    numero -= 1
    print(numero)
    numero += 1

#uso de la clase nodo
objetoNodo = Nodo()
print(objetoNodo.getIndice()) #imprime 0

