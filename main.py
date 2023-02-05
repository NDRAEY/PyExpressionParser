import filter
import tokenizer
import builders
from pprint import pprint
import prec
import evaluator

def get_result(work):
    tk = tokenizer.advtok(work)
    tk = filter.no_whitespaces(tk)
    tk = builders.negative_numbers(tk)
    tk = builders.parenthesis2list(tk)

    tk = prec.build_precedence_once(tk)

    return evaluator.evaluate(tk)

if __name__=="__main__":
    while True:
        print(get_result(input("> ")))
