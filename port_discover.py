#!/usr/bin/python3
import socket
import sys

def pedirDatos():
    while(True):
        print("Selecciona una opción:")
        print("1. Escaneo de un puerto concreto")
        print("2. Escaneo de un rango de puertos")
        entrada = int(input())
        if(entrada == 1 or entrada == 2):
            break    
    return entrada

def modo(entrada):
    if(entrada == 1):
        puerto_escaneo = input("Introduce el puerto que quieres escanear: ")
        ip_escaneo = input("Introduce la dirección que quieres escanear: ")
        swescaner(ip_escaneo, puerto_escaneo,None)
    elif(entrada == 2):
        puerto_inicio = input("Introduce el puerto de inicio: ")
        puerto_fin = input("Introduce el puerto de fin: ")
        ip_escaneo = input("Introduce la dirección que quieres escanear: ")
        swescaner(ip_escaneo, puerto_inicio, puerto_fin)

def swescaner(ip,p_inicio,p_fin):
    if(p_fin == None):
        respuesta = escaner(ip,p_inicio)
        if(respuesta == True):
            print("El puerto "+p_inicio+" está abierto en "+ip)
        else:
            print("El puerto "+p_inicio+" está cerrado en "+ip)
    else:
        for puerto in range(int(p_inicio),int(p_fin)):
            respuesta = escaner(ip,puerto)
            if(respuesta == True):
                print("El puerto "+puerto+" está abierto en "+ip)


def escaner(ip,puerto):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        respuesta = skt.connect((ip, int(puerto)))
        skt.close()
        return True
    except:
        skt.close()
        return False
    
def main():
    print("Bienvenido al escaner de puertos")
    entrada = pedirDatos()
    modo(entrada)

main()