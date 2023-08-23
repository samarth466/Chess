def flatten(seq) -> list:
    if len(seq) == 0:
        return seq
    if isinstance(seq[0], (set, list, tuple)):
        return flatten(seq[0]) + flatten(seq[1:])
    return seq[:1] + flatten(seq[1:])