# -*- coding: cp1252 -*-
#SEMINARIO 1 DE PYTHON (versi�n 3.6)
#Parte 1: Variables
#Contexto: Hacklab_UPM
#Fecha: jueves, 5 de octubre de 2017
#Impartido por: Javier Rojo Mu�oz




#COMENTARIOS y miscel�nea
#El int�rprete de Python ignora todo lo que encuentre despu�s del '#'
#al definir listas/tuplas/diccionarios las comas ',' permiten seguir en otra l�nea f�sica.
#Se pueden concatenar varias l�neas l�gicas en una l�nea f�sica:
x=2;print(x)


#############################################################################

#VARIABLES SIMILARES A OTROS LENGUAJES
x= True        #Un booleano
x= 1           #un n�mero entero
x= 2.3         #un n�mero decimal (float)
x= "casa"      #una cadena de caracteres (String)
x= 5+2j        #un n�mero imaginario
x= complex(5,2)#otra manera de crear un n�mero imaginario

#Python permite algunas sintaxis de asignaci�n especiales:
x=y=4          #ahora x=4 e y=4
x,y=1,5        #ahora x=1 e y=5


#############################################################################

#ELIMINAR VARIABLES
#para eliminar una variable al completo usamos 'del'
del y          #ahora cualquier operaci�n con y dar�a error.


#############################################################################

#LA FUNCI�N PRINT() Y LAS CADENAS DE CARACTERES

#La funci�n print() imprime (normalmente en la consola) el par�metro que pasemos.
#En Python 3 se vuelve obligatorio el uso de par�ntesis.
print("hola mundo")
print(x)
print("Esta l�nea se imprimir�\
en una sola l�nea de consola.")
print("Detr�s de esta l�nea no imprimir� un salto de l�nea",end="")
print("""Esto representa un p�rrafo
donde se respetar�n los saltos,
espacios y "comillas" literales.""")

#Podemos concatenar cadenas con '+', y podemos unir distintos objetos con ','
print("Nueva "+"Zelanda")               #Nueva Zelanda
print("Tengo", 20, "a�os.")             #Tengo 20 a�os. Por defecto sustituye la coma por espacios
print("Soy", "un", "Robot", sep="-")    #Soy-un-robot

#Si intentamos concatenar una cadena y un n�mero tendremos que
#transformar el n�mero en un literal (cadena). Cuidado:
#No hay espacios en la concatenaci�n. Es una uni�n literal.
print("Tengo "+str(20)+" a�os")


#ACCEDER A LOS ELEMENTOS DE UNA CADENA
#Estos m�todos ser�n muy �tiles ya que se repetir�n en otras estructuras como las listas
mi_cadena = "Python es genial."
print(mi_cadena[0])   #P
print(mi_cadena[1])   #y

print(mi_cadena[:2])  #Py
#Significa "empieza a coger elementos hasta que llegues al segundo (�ndice 1).

print(mi_cadena[2:])  #thon es genial.
#Significa "ponte en el elemento de �ndice 2 (t) y recorre hasta el final.

print(mi_cadena[0:])  #Python es genial. V�ase el ejemplo anterior.
#0 significa el inicio de la cadena

#NO se pueden asignar valores a elementos concretos de la cadena.
#mi_cadena[0]='a'

#Como ya hemos visto, se pueden concatenar cadenas.



#############################################################################

#TIPOS ESPECIALES DE VARIABLES
#Una vez hemos visto los tipos de variables m�s b�sicos podemos
#centrarnos en los m�s "especiales", curiosos o simplemente diferentes
#Es importante se�alar que en todos estos tipos podemos incluir otros objetos
#de ese mismo tipo (por ejemplo, una lista de listas, una tupla con un diccionario, etc.)


#############################################################################

#LISTAS
#Una lista es un conjunto ORDENADO y MUTABLE de objetos.
#Es parecido en cierto sentido a un vector en C.
#Se indican con [] y tienen �ndices

mi_lista = [1, "hola", 3.14, 4-2j, [2,3,4], "�ltimo"]
print(mi_lista)        #imprime toda la lista
print(mi_lista[2])     #imprime 3.14
print(mi_lista[:3])    #imprime [1,"hola",3.14]
print(len(mi_lista))   #imprime 6 (el n�mero de elementos)
#Los �ndices negativos se pueden usar para indicar valores empezando por el final
print(mi_lista[-2])    #imprime [2,3,4]
print(mi_lista[-3:])   #imprime [4-2j, [2,3,4], "�ltimo"]

#Para modificar valores:
mi_lista[0]= "primero"             #sustituye el elemento [0] por "primero"
mi_lista.append("nuevo elemento")  #a�ade un elemento al final.
print(mi_lista)


#############################################################################

#TUPLAS
#Las tuplas son conjuntos ORDENADOS, pero INMUTABLES
#Si intentamos dar un nuevo valor a una tupla ya creada obtenemos un error.
#Se representan con (), pero al llamar por el �ndice se hace exactamente igual que las listas
tupla_semanal = ("Lunes", "Martes", "Mi�rcoles", "Jueves", "Viernes", "S�bado", "Domingo")
print(tupla_semanal[2])  #imprime "Mi�rcoles"


#############################################################################

#DICCIONARIOS
#Son conjuntos NO ORDENADOS y MUTABLES.
#Esto quiere decir que s�lo nos importa "si el elemento existe en el diccionario".
#Al imprimir el conjunto entero no podemos saber en qu� orden lo har�.
#Est�n formados por parejas de claves (keys) y valores (values)
#Sintaxis: {key1:value1, key2:value2, ...}
#Veremos en profundidad c�mo iterar en diccionarios cuando veamos bucles

nivel_genialidad = {"C":9000,"Python":9001, "java":"�Y ese qui�n es?", "otros":mi_lista}
otro_ejemplo ={"Pedro":"Picapiedra",
               "Homer":"Simpson",
               "Seilmour":"Skinner",
               "Armin":"Tanzanian"}

print(nivel_genialidad)          #imprime todo el diccionario con sus parejas
print(nivel_genialidad["Python"])#imprime 9001
print(nivel_genialidad.keys())   #imprime:  C, Python, java, otros
print(nivel_genialidad.values()) #imprime:  9000,9001,"�Y ese qui�n es?", mi_lista(imprime toda la lista)

#Para modificar valores (si existen) o a�adirlos autom�ticamente:
otro_ejemplo["Pedro"]="Almod�var"
otro_ejemplo["Sentido de la vida"]=42
print(otro_ejemplo)

#un adelanto sobre booleanos:
#Si escribimos 'in' dicccionario buscar� ese elemento entre las claves.

print("Homer" in otro_ejemplo)             #True. Por defecto busca entre las clavesprint("Homer" in otro_ejemplo.keys())      #True. Busca entre las claves
print("Simpson" in otro_ejemplo)           #False. Busca entre las claves por defecto
print("Simpson" in otro_ejemplo.values())  #True. Busca entre los valores de otro_ejemplo



