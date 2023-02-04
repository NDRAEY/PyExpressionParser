import tokenizer as tok
from pprint import pprint

def evaluate(tokens):
    result = 0
    i = 0

    if type(tokens) is tok.Token:
        return int(tokens.value)

    while i < len(tokens):
        if len(tokens[i:i+3]) == 1:
            return evaluate(tokens[i])
            
        lhs, op, rhs = tokens[i:i+3]
        '''
        print("====")
        pprint(lhs)
        print("====", op)
        pprint(rhs)
        print("====")
        '''

        if type(lhs) is list:
            lhs = evaluate(lhs)

        if type(rhs) is list:
            rhs = evaluate(rhs)

        lhs, rhs = int(lhs.value) if type(lhs) is tok.Token else lhs, \
                   int(rhs.value) if type(rhs) is tok.Token else rhs

        if op.value == "+":
            return int(lhs) + int(rhs)
        elif op.value == "-":
            return int(lhs) - int(rhs)
        elif op.value == "*":
            return int(lhs) * int(rhs)
        elif op.value == "/":
            return int(lhs) / int(rhs)
        
        i += 1

    return result
