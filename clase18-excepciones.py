
try:
    import cpickle
except  ImportError:
    import pickle

def division(a,b):
    #Try-except-else-finally
    cociente = 0
    try:
        cociente = a / b
    except ZeroDivisionError:
        cociente = "Indef"

    return cociente

print( division(12,0) )

try:
    a = 10
    a = a+1
    print("El valor de a es: ", aa)
except NameError:
    print("Error en el nombre de una variable")
except:
    print("Error genérico")
else:
    print("Bloque try ejecutado sin problemas")
finally:
    print("Bloque finally ejecutado")


try:
    archivo  = open("C://Users//Luciano//Luciano_es_físico.py", "r")
except FileNotFoundError:
    print("El archivo no existe, por favor verifica que exista")


print("La vida debe continuar")

