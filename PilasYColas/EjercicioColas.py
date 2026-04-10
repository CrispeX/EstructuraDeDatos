from .Estructura import LinkedList,Node, Queue

def interambiar_mitad(q1):

    mitad = q1.len()//2

    for _ in range(0, mitad):
        q1.encolar(q1.desencolar())
    
    print(q1) 

def fix_estring_mayusculas_minusculas(q1):

    aux = Queue()
    index = 0

    while index < q1.len()-2:
        
        if q1[index] != q1[index+1]: #Caso letras adyacentes diferentes
            if q1[index].lower() == q1[index+1] or q1[index] == q1[index+1].lower(): #Caso letras adyacentes iguales pero una mayuscula y otra minuscula
                index += 2
            else: #Caso letras adyacentes diferentes
                aux.encolar(q1[index])
                index += 1
        
        else: #Caso letras adyacentes iguales
            aux.encolar(q1[index])
            index += 1

    aux.encolar(q1[index]) if index < q1.len() else None #Caso letra final sin comparar

