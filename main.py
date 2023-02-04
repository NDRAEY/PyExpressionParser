import filter
import tokenizer
import builders
from pprint import pprint
import prec
import evaluator

work = "6 + (-3 - 1)"

if __name__=="__main__":
    tk = tokenizer.advtok(work)
    tk = filter.no_whitespaces(tk)
    tk = builders.negative_numbers(tk)

    pprint(tk)
    print("--------------")
    
    tk = builders.parenthesis2list(tk)

    print(work)
    
    tk = prec.build_precedence_once(tk)
    pprint(tk)

    r = evaluator.evaluate(tk)

    print("Result: ", r)
