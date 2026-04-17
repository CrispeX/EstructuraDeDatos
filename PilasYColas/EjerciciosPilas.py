from Estructura import Node, LinkedList, Queue, Stack


def validate_expresion(math_expre):

    open_op = "([{"
    close_op = ")]}"
    stack = Stack()

    for c in math_expre:
        if c in open_op:
            stack.push(c)
        elif c in close_op:
            print("Operado de cierrre: ", c)
            print("Indice de cierre: ", close_op.index(c))
            if stack.is_empty():
                return False
            last_open = stack.pop()
            print("Operador de apertura: ", last_open)
            print("Indice de apertura: ", open_op.index(last_open))
            if open_op.index(last_open) != close_op.index(c):
                return False

    return stack.is_empty()

"""expresion1 = "([a+b])"
print(validate_expresion(expresion1))"""

