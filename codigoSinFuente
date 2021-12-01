# El codigo de Beimar
# Aunque no se de donde salio, pero funciona
# ¿Por que funciona? Quiza lo explore luego xd

from math import ceil, floor, sqrt
import time

def Cantidad(x):
    pi_ = ceil(0.5 * floor((2 * x + (-1) ** x - 6 * c_(x) + 5) / 3))
    return int(pi_)

def prime_(x):
    if ((((x - 1) / 3 )% 2) == 0) and ((x - 1) / 3 ).is_integer():
        z = ceil((sqrt(x)-1) / 3)
        for i in range(1, z + 1):
            r = (2*(x - 1) - 6*i + (-1) ** i-1) / (6 * i + 3 - (-1) ** i)
            if r.is_integer():
                return False
        return True
    elif (((x - 2) / 3) % 2) != 0 and ((x - 2) / 3).is_integer():
        z = ceil((sqrt(x-1)-1) / 3)
        for i in range(1, z):
            r = (2*(x - 2) - 6*i + (-1) ** i+1) / (6 * i + 3 - (-1) ** i)
            if r.is_integer():
                return False
        return True
    else:
        return False

def formula_1(x):
    if (x < 5):
        pass
    count = 2
    for i in range(5, x):
        if prime_(i):
            count += 1
    return count

values = [10, 100, 1000,10000,100000]

time.sleep(1)

print("MI METODO")

start_time = time.time()

for v in values:
    print(f"LA CANTIDAD DE PRIMOS MENORES A {v}, ES: {formula_1(v)}")

print(f"TARDA {time.time() - start_time} SEGUNDOS")

print("\n")

# Mi codigo

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

start_time = time.time()

print("MI METODO, o sea el mio no el de Beimar xd")

for v in values:
    primos = pri(v)
    print(f"LA CANTIDAD DE PRIMOS MENORES A {v} es: {len(primos)}")
print(f"TARDA {time.time() - start_time} SEGUNDOS")

def primo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

