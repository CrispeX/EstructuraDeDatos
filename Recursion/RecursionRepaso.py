def reverse_string(palabra: str, index:int=0):
  if -(len(palabra)) == index:
    return ""
  index -= 1
  return palabra[index] + reverse_string(palabra, index)

s1 = "sarutcurtse"
s2 = "sotad ed"
s3 = "sacimánid"

print(f"ex1: {reverse_string(s1) == 'estructuras'}")
print(f"ex2: {reverse_string(s2) == 'de datos'}")
print(f"ex3: {reverse_string(s3) == 'dinámicas'}")