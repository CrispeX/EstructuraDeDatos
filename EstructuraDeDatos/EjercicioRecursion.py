#Ejemplos:


def abriruñeca(nummuñe):
  if nummuñe == 1:
    return print("Proceso finalizado:" + str(nummuñe))
  abriruñeca(nummuñe - 1)
  print("Proceso en muñeca:"+str(numnuñe))
abriruñeca(1)



def factorial(n):
  if n == 0:
    return 1
  return n*factorial(n-1)
factorial(5)


def digitos(n:int):
  assert isinstance(n, int) and n>=0, "Error n debe ser un entero postivo"
  if n == 0:
    return 0
  return 1+digitos(n//10)

digitos(-1)