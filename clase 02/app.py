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

