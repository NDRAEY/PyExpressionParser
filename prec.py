import tokenizer
SORTED_OPS = (("+", 1), ("-", 1), ("*", 2), ("/", 2))

def tok_prio(tokstr: str):
    for i in SORTED_OPS:
        if i[0] == tokstr:
            return i[1]

def build_precedence_once(tokens):
    result = [1, 0]
    i = 0

    while i < len(tokens):
        if (type(tokens[i]) is tokenizer.Token) and \
           tokens[i].type == tokenizer.TokenType.OPERATOR:
            if tok_prio(tokens[i].value) >= result[0] :
                result = (tok_prio(tokens[i].value), i)
        i += 1

    toks = tokens[result[1]-1:result[1]+2]
    del tokens[result[1]-1:result[1]+2]

    tokens.insert(result[1]-1, toks)

    return tokens
