import ctypes as c

# Carregar a DLL
dll = c.CDLL('./fatorial.dll')

# Definir o tipo de argumento e o tipo de retorno da função fatorial
dll.fatorial.argtypes = (c.c_int,)
dll.fatorial.restype = c.c_int

# Usar a função fatorial da DLL
n = 6
fat = dll.fatorial(n)
print(f"O fatorial de {n} eh: {fat}")
