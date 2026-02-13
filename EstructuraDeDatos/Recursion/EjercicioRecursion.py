#Ejemplos:


"""def abriruñeca(nummuñe):
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

#Reversar palabra
def reversed_word(p):
  if len(p) == 1:
    return p
  return p[-1] + reversed_word(p[:-1])
reversed_word("mesa")

p = "mesa"
print(p[-1])
print(p[:-1])
print(p[::-1])

def reversed_word(p, index = 0):
  if len(p) == 1:
    return p
  return p[-1] + reversed_word(p[:-1])
reversed_word("mesa")

p = "mesa"
print(p[-1])
print(p[:-1])
print(p[::-1])

def reversed_word3(p, index = 0, pr = ""):
  if index == len(p):
    return pr
  return reversed_word3(p, index + 1, p[index]+pr) 
pq = "mesa"
print(reversed_word3(pq))

"""
#Implemente una funcion recursiva que valide si una palabra es palindrome, Retornando True o False
"""def es_palindrome(p, index1=-1, index2=-1):
  if index1 == -1 and index2 == -1:
    index1 = 0
    index2 = len(p)-1
  
  if index1 == index2 or index2 < index1:
    return True
  
  if p[index1] == p[index2]:
    return es_palindrome(p, index1+1, index2-1)
  
  else:
    return False

p1 = "rotor"
p2 = "mierda"
p3 = "massam"
print(es_palindrome(p1))
print(es_palindrome(p2))
print(es_palindrome(p3))

def es_palindrome(p):
  if len(p) == 1:
    return True
  if p[-1] == p[0]:
    return es_palindrome(p[1:-1])
  else:
    return False

p1 = "rotor"
p2 = "mierda"
print(es_palindrome(p1))
print(es_palindrome(p2))"""

#Implemente una funcion recursiva que reverse una lista

"""def reversed_list(l):
    if len(l) == 1:
        return l
    return [l[-1]]+reversed_list(l[:-1])

l = [4,5,6,7,111]
print(l)
print(reversed_list(l))

def reversed_list2(l, index=0, lr=[]):
    if index == len(l):
        return lr
    return reversed_list2(l, index+1, [l[index]]+lr)

l = [4,5,6,7,111]
print(l)
print(reversed_list(l))
"""

#Implemente una funcion recursiva
"""def busqueda_binaria(l, obj, i_low=-1, i_high=1):
    if i_low == -1 and i_high == 1:
        i_low = 0
        i_high = len(l)-1
    print("i_low", i_low)
    print("i_hight", i_high)
    i_med = (i_low+i_high)//2
    print(i_low, i_med, i_high)

    if l[i_med] == obj:
        return i_med
    
    if i_low > i_high:
      return "El objeto no fue encontrado"

    if obj < l[i_med]:
        #busqueda en la primera mitad
        print("obj < l[i_med]")
        return busqueda_binaria(l, obj, i_low, i_med-1)
    elif obj > l[i_med]:
      #busqueda en la segunda mitad
      return busqueda_binaria(l, obj, i_med+1, i_high)


l = [1,2,3,3,3,5,6,7,8,33,444,222,4,4545]
v1 = 3
v2 = 4
v3 = 8
print(f"El valor {v1} esta en la posicion {busqueda_binaria(l, v1)}")
print(f"El valor {v2} esta en la posicion {busqueda_binaria(l, v2)}")
print(f"El valor {v3} esta en la posicion {busqueda_binaria(l, v3)}")"""