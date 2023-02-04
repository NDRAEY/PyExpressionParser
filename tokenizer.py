from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    NUMBER = 0
    OPERATOR = 1
    UNKNOWN = 2

TOKENLIST = "(){}[],.:;*+-/@#$\"\' =^~|%<>\n"

@dataclass
class Token:
    start: int
    end: int
    value: str
    type: TokenType

def tokenize(code):
    tokens = []
    sptokens = []
    for i in code:
        if i in TOKENLIST:
            if len(sptokens):
                tokens.append(''.join(sptokens))
                sptokens = []
            tokens.append(i)
        else:
            sptokens.append(i)

    if len(sptokens):
        tokens.append(''.join(sptokens))
        sptokens = []
    return tokens

def token_type(i):
    if i in "+-/*":
        return TokenType.OPERATOR
    elif i.isdigit():
        return TokenType.NUMBER
    else:
        return TokenType.UNKNOWN

def advtok(tokenized):
    total = []
    pos = 0
    for i in tokenize(tokenized):
        total.append(Token(
            pos, pos+len(i), i, token_type(i)
        ))
        pos += len(i)
    return total
