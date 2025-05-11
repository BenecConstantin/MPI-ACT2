def dpll_solver(clauses, assignment={}):
    clauses = unit_propagate(clauses, assignment)
    if clauses is False:
        return False
    if not clauses:
        return assignment

    l = choose_literal(clauses)
    for val in [l, -l]:
        new_assignment = assignment.copy()
        new_assignment[abs(val)] = val > 0
        result = dpll_solver(simplify(clauses, val), new_assignment)
        if result:
            return result
    return False


def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        unit_clauses = [c for c in clauses if len(c) == 1]
        for uc in unit_clauses:
            val = uc[0]
            assignment[abs(val)] = val > 0
            clauses = simplify(clauses, val)
            if clauses is False:
                return False
            changed = True
    return clauses


def simplify(clauses, literal):
    result = []
    for clause in clauses:
        if literal in clause:
            continue
        new_clause = [x for x in clause if x != -literal]
        if not new_clause:
            return False
        result.append(new_clause)
    return result


def choose_literal(clauses):
    for clause in clauses:
        for literal in clause:
            return abs(literal)
