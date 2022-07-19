import psycopg2

from functions.select import *
from functions.update import *
from functions.delete import *
from functions.ctd import *
from functions.insert import *

print("¡Hola! Bienvenido a la base de datos ciclista de Samuel :)")
print("Soy Kira, tu compañera computacional. Primero quiero saber quien eres.")


print("1.- Cliente. Deseo ver algunas bicis :)")
print("2.- Negocio registrado. Deseo modificar la base de datos.")
opcion = int(input())
if opcion==1:
    print("¿Qué desea realizar?")
    print("1.- Buscar las bicicletas en mi propiedad.")
    print("2.- Saber disponibilidad de tallas.")
    print("Cualquier otro numero: Salir")
    print("Opción:")
    opcion2 = int(input())
    if opcion2==1:
        select_bicicletas()
    elif opcion2==2:
        print("Ingrese la talla que desee consultar (S, M o L): ")
        talla = input()
        if talla=='s' or talla=='S':
            talla_s(talla)
        elif talla=='m' or talla=='M':
            talla_m(talla)
        elif talla=='l' or talla=='L':
            talla_l(talla)
        else:
            print("Ingrese talla admitida")

elif opcion==2:
    print("¿Qué desea realizar?")
    print("1.- Agregar una bicicleta vendida.")
    print("2.- Eliminar registro de bicicleta vendida.")
    print("3.- Actualizar precio de una bicicleta.")
    print("4.- Inscribir nuevo local.")
    print("5.- Inscribir datos de nuevo cliente.")
    print("6.- Revisar preferencias en tipo de bicicleta de un usuario.")
    print("Cualquier otro numero: Salir")
    print("Opción:")
    opcion3 = int(input())
    if opcion3==1:
        insertar_bicicleta()
    elif opcion3==2:
        delete()
    elif opcion3==3:
        update()
    elif opcion3==4:
        insertar_tienda()
    elif opcion3==5:
        insertar_cliente()
    elif opcion3==6:
        select_disciplinas()
else:
    print("Por favor, elije una opcion correcta :c.")

print("¡Adios!")