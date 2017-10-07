# -*- coding: cp1252 -*-
#SEMINARIO 1 DE PYTHON (versi�n 3.6)
#Parte 2: Bucles y funciones
#Contexto: Hacklab_UPM
#Fecha: jueves, 5 de octubre de 2017
#Impartido por: Javier Rojo Mu�oz

#############################################################################

Bool_ej=True
Bool_ej2=False
lista_ej = ["elem1", "elem2", "elem3", "elem4"]


#############################################################################

#BOOLEANOS Y OPERACIONES L�GICAS
#En Python3 usamos las palabras not, and, or para describir las operaciones booleanas
#las comparaciones son iguales a otros lenguajes de programaci�n (<,>,<=,>=,==)
#Recordemos que == significa comparaci�n y que = significa asignaci�n
print(1<2 and 3==3)           #True. Ambas son verdaderas
print(1<2 and 4==3)           #False. No se cumple la condici�n 'and'
print(1<2 or 4==3)            #True. Una de las dos condiciones se cumple
print("elem1" not in lista_ej)#False. 'in lista_ej' devuelve True y NOT lo niega



#############################################################################

#La sintaxis de Python marca que aquello que pertenece a una categor�a inferior
#(l�neas dentro de un if, de un bucle, el contenido de una funci�n) debe se�alarse
#mediante indentaci�n (recomendada 4 espacios). El inicio se marca con dos puntos
#y lo importante es ser coherente. Es decir, que aquello que est� indentado con
#8 espacios sea porque est� dos niveles por debajo del c�digo principal. Ejemplo:


#V�LIDO Y  RECOMENDADO
#if x==5:
#    print("x era igual a 5")
#else:
#    print("Vuelva a intentarlo")


#V�LIDO PERO NO RECOMENDADO
#if x==5:
#  print("x era igual a 5")
#else:
#  print("Vuelva a intentarlo")


#NO V�LIDO
#if x==5:
#    print("x era igual a 5")
#else:
#  print("Vuelva a intentarlo")


#############################################################################

#IF,ELIF,ELSE
#Si se cumple la condici�n del if python ejecutar� las l�neas que se encuentren dentro.
#Una vez acabado el if saltar�a al final del else para continuar con el c�digo.
#Si no se cumple la condici�n del if, Python evaluar� la condici�n del primer elif.
#Python proceder� de manera an�loga al if con todos los 'elif' (diminutivo de
#'else if'. Finalmente, si no se ha cumplido ninguna condici�n ejecuta el interior
#de 'else'. No es necesario incluir elif ni else, pero suele ser conveniente
#para controlar qu� sucede en caso de "error"


print("antes del if-elif-else")
if Bool_ej:
    print("El booleano de ejemplo era cierto")
elif Bool_ej2:
    print("El booleano 1 era falso, pero al menos el 2 es cierto")
else:
    print("Ninguno de los dos booleanos era cierto.")
print("despu�s del if-elif-else")

#Puedes jugar con el valor de estos booleanos (al inicio del c�digo) para ver
#qu� resultado sale.
#Los 'else' tienen otros posibles usos que veremos con los bucles

#############################################################################

#RANGE()
#La funci�n range() es muy �til para generar sucesiones de n�meros.
#si solo incluimos un par�metro har� una sucesi�n desde cero hasta ese n�mero.
#si incluimos dos n�meros har� una sucesi�n del primero al segundo.
#un tercer par�metro indicar�a el "salto". Es decir, que coja los valores de
#dos en dos o de tres en tres:
print(list(range(5)))          #0,1,2,3,4
print(list(range(3,10)))       #3,4,5,6,7,8,9
print(list(range(10,3)))       #inv�lido. No imprime nada. Habr�a que a�adir como
                               #tercer factor un (-1)
print(list(range(2,20,2)))     #2,4,6,8,10,12,14,16,18
print(list(range(100,50,-10))) #100,90,80,70,60


#############################################################################

#BUCLES FOR Y RECORRER LISTAS

#Los bucles for los podemos usar de dos formas:
#O bien iteramos a lo largo de una lista/tupla/diccionario
#o bien iteramos a lo largo de un rango de n�meros range() cuando sabemos el n�mero de iteraciones.
#'continue' hace que pasemos a la siguiente iteraci�n
#'break' hace que se acabe el bucle

for x in lista_ej:
    if x=="elem2":  #si topamos con elem2 "abortamos" la ITERACI�N. Break saldr�a del BUCLE
        continue
    print(x,end="-")

#En el for, la variable x se crea al iniciar el bucle (o podr�a estar ya creada de antes)
#Podriamos haberla llamado como quisieramos (p.ej.:for elem in lista_ej:)
#Para cada iteraci�n del bucle, adquiere el valor del siguiente elemento de la lista.
#Dentro del bucle se puede usar ahora esta variable para hacer operaciones (como imprimirlo por pantalla)

print("")
for x in range(10):
    print(x,end=".")


#si incluimos un else despu�s entra s�lo si ha salido del bucle normalmente (no por un break)
#Prueba a cambiar la condici�n del if para que sea True o False y mira el resultado
print("")
for x in range(5):
    if x==6:
        break
    print(x,end="_")
else:
    print("dentro del else. Todo ha ido bien")
print("detr�s del for")



#############################################################################

#BUCLES WHILE
#usamos while cuando no sabemos el n�mero de iteraciones, sino que queremos
#realizar la acci�n hasta que se cumpla una condici�n.
#por ejemplo, hasta que el n�mero de dni introducido sea mayor que 0
#Un else se ejecuta si se sale normalmente al comprobar que la condici�n es falsa
#Un else no se ejecutar� si se sale con un break
#Pueden surgir f�cilmente bucles infinitos si, por ejemplo, el booleano siempre es True
while Bool_ej2:
    print("dentro del while")
else:
    print("La condici�n era falsa. Todo controlado")



#############################################################################

#FUNCIONES SIMPLES
#Las funciones las definimos con 'def nombre(posibles_par�metros):'
#Como el int�rprete salta de l�nea en l�nea necesitamos definir la funci�n
#antes de utilizarla. Las funciones pueden devolver objetos mediante return.
#Todo lo que quede detr�s del return se ignorar�, ya que volveremos al c�digo principal.
def saludar():
    print("hola")

saludar()  #llamar� a la funci�n y se empezar�n a ejecutar las l�neas dentro de �sta

def imprimir(mensaje):
    print(mensaje)

imprimir("llamada a funci�n con par�metro")

#Podemos dar valores por defecto a los par�metros con ciertas condiciones:
#1:Los valores por defecto deben ir al final
#2:En la llamada a la funci�n todo par�metro sin valor por defecto debe ser expl�cito
#3:Podemos redefinir par�metros o bien por el orden o bien por el nombre:

def sumayresta(A,B=0,C=0):
    #por defecto b y c valen cero, pero siempre hay que pasar un valor de a
    return A+B-C

print(sumayresta(1))         #1+0-0=1. Es obligatorio dar valor a A, ya que no tiene valor default
print(sumayresta(1,3))       #1+3-0=4. Se lo asignamos al primer par�metro sin valor default
print(sumayresta(1,3,2))     #1+3-2=2. Sustituimos todos los valores por defecto
print(sumayresta(1,C=2,B=3)) #1+3-2=2. Si lo indicamos con el nombre no necesitamos el orden



#############################################################################

#PASS
#La palabra clave 'pass' no hace nada. Se utiliza mientras se programa cuando
#sint�cticamente necesitas rellenar un hueco, pero no quieres que haga nada:

def megafuncion():
    #ya escribir� despu�s el c�digo
    pass


