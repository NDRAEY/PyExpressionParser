from pprint import pprint
from tokenizer import TokenType

def parenthesis2list(tokens):
    total = []

    n = 0

    while n < len(tokens):
        i = tokens[n]
        
        if i.value == "(":
            n += 1
            newtoks = parenthesis2list(tokens[n:])
            total.append(newtoks)

            while i.value != ")":
                i = tokens[n]
                n += 1
            # n += len(newtoks)
        elif i.value == ")":
            return total
        else:
            total.append(i)

        n += 1

    return total

def negative_numbers(tokens):
    i = 0

    while i < len(tokens):
        p = tokens[i]

        if p.type == TokenType.OPERATOR and \
           tokens[i+1].type == TokenType.NUMBER and \
           p.value == "-":
           ntok = p
           ntok.end = tokens[i+1].end
           ntok.value = p.value + tokens[i+1].value
           ntok.type = TokenType.NUMBER
           tokens[i] = ntok
           del tokens[i+1]
           break
        
        i += 1

    return tokens
