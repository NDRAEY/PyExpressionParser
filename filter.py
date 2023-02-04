def no_whitespaces(tokens):
    return [i for i in tokens if i.value not in (" ", "\n", "\t")]
