import math # Para usar ceil
import time # Comparar tiempos

def Eit(n):
	if n % 1 != 0 or n < 1:
		return 0
	else:
		return 1
    
def A(x):
	return math.ceil(1/2 * math.floor((2 * x + (-1) ** x - 7)/3)) # Confio en que python realiza el orden correcto de las operaciones
 
def m(x):
	return math.ceil( (-1 + math.sqrt(1 + 3 * A(x)))/3 )

def C(x):
	suma = 0
	for i in range(1, m(x) + 1):
		sumaIntermedia = 0
		for j in range(8, A(x) + 1):
			numerador = 4 * j - (-1) ** j + (2 * i + 1) * (-1) ** (i + j) + (2 * i - 1) * (-1) ** i - 12 * i ** 2 + 5
			denominador = 12 * i + 6 - 2 * (-1) ** j
			sumaIntermedia += Eit(numerador / denominador)
		suma += Eit(sumaIntermedia)
	return suma
 
def pi(x):
	numerador = 2 * x + (-1) ** x - 6 * C(x) + 5
	return math.ceil(1/2 * math.floor(numerador / 3))

# El siguiente codigo es la forma estandar de encontrar numeros primos
def pri(x = 1): # Si no se ingresa numero, entonces se asume que el numero ingresado es 1.
	primo = [2]
	for i in range(3, x):
		esPrimo = True
		for j in primo:
			if i % j == 0:
				esPrimo = False
				break
		if esPrimo:
			primo.append(i)
	return primo

# Comparacion final:
def comparaPiConPri(x):
	inicio = time.time()
	print("Pi de x es: " + str(pi(x)))
	print("Esto tardo " + str(time.time() - inicio))
	inicio = time.time()
	print("Pri de x es: " + str(pri(x)))
	print("Esto tardo " + str(time.time() - inicio))
