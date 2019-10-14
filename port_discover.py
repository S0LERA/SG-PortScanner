#!/usr/bin/python3
import socket
import sys

def pedirDatos():
    while(True):
        print("Selecciona una opción:")
        print("1. Escaneo de un puerto concreto")
        print("2. Escaneo de un rango de puertos")
        opcion = int(input())
        if(opcion == 1 or opcion == 2):
            break    
    return opcion

def modo(opcion):
    if(opcion == 1):
        puerto_escaneo = input("Introduce el puerto que quieres escanear")
        ip_escaneo = input("Introduce la dirección que quieres escanear: ")
        print("Ip: " + ip_escaneo + " ,puerto: "+ puerto_escaneo)
    elif (opcion == 2):
        puerto_inicio = input("Introduce el puerto de inicio ")
        puerto_fin = input("Introduce el puerto de fin")
        ip_escaneo = input("Introduce la dirección que quieres escanear: ")
        print("Ip: " + ip_escaneo + " ,puerto inicio: "+ puerto_inicio + " ,puerto fin: " + puerto_fin)

def main():
    print("Bienvenido al escaner de puertos")
    opcion = pedirDatos()
    modo(opcion)

main()