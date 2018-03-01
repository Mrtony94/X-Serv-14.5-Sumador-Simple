#!/usr/bin/python3

import sys


Function_P = ['sumar', 'restar', 'multiplicar', 'dividir']

def suma(num1,num2):
    print(num1, "+", num2, "=", num1 + num2)

def resta(num1,num2):
    print(num1, "-", num2, "=", num1 - num2)

def mult(num1,num2):
    print(num1, "*", num2, "=", num1 * num2)

def div(num1,num2):
    try:
        print(num1, "/", num2, "=", num1 / num2)
    except ZeroDivisionError:
        print ("\nNo se puede dividir entre cero :Sorry\n")

def operaciones(num1, num2):
    if operacion == Function_P[0]:
    	return suma(num1, num2)
    elif operacion == Function_P[1]:
    	return resta(num1, num2)
    elif operacion == Function_P[2]:
    	return mult(num1, num2)
    elif operacion == Function_P[3]:
    	return div(num1, num2)
    else:
    	sys.exit("Argumento incorrecto, vuelva a intentarlo")

if __name__ == "__main__":
    len_P = len(sys.argv)
    operacion = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
    def comprobacion():
        if len_P != 4:
            sys.exit("Has cometido un error, vuelve a intentarlo")
    comprobacion()
    operaciones(num1,num2)
