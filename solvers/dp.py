def dp_solver(clauses):
    symbols = set(abs(lit) for clause in clauses for lit in clause)
    return dp_recursive(clauses, symbols)


def dp_recursive(clauses, symbols):
    if not clauses:
        return True
    if [] in clauses:
        return False

    P = next(iter(symbols))
    rest = symbols - {P}

    return (dp_recursive(simplify(clauses, P), rest) or
            dp_recursive(simplify(clauses, -P), rest))


def simplify(clauses, literal):
    simplified = []
    for clause in clauses:
        if literal in clause:
            continue
        new_clause = [l for l in clause if l != -literal]
        simplified.append(new_clause)
    return simplified
