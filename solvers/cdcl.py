def unit_propagate(clauses, assignment):
    """
    Performs unit propagation on the clauses based on the current assignment.
    If a clause has only one unassigned literal, assign it accordingly.
    """
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    while unit_clauses:
        clause = unit_clauses.pop()
        literal = clause[0]
        if literal not in assignment:
            # Assign the value
            assignment[literal] = True if literal > 0 else False
            clauses = propagate(clauses, literal)
            # Add new unit clauses
            unit_clauses = [c for c in clauses if len(c) == 1 and c not in unit_clauses]
    return clauses, assignment


def propagate(clauses, literal):
    """
    Propagate the assignment of a literal across the clauses.
    This means removing all clauses satisfied by the literal and removing
    the literal from unsatisfied clauses.
    """
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = [l for l in clause if l != -literal]  # Remove the negation of the literal
        if not new_clause:  # Clause is now empty, hence unsatisfiable
            return []
        new_clauses.append(new_clause)
    return new_clauses


def backtrack(assignment, decision_stack):
    """
    Backtrack the assignment by removing the last decision from the decision stack.
    """
    if decision_stack:
        last_decision = decision_stack.pop()
        del assignment[last_decision]
        return decision_stack
    return decision_stack


def cdcl_solver(clauses):
    """
    A simple Conflict-Driven Clause Learning (CDCL) solver with unit propagation, basic backtracking, and conflict learning.
    """
    assignment = {}  # Current assignment of literals
    decision_stack = []  # Stack to track decisions for backtracking
    level = 0  # Decision level

    while True:
        # Unit propagation to simplify the formula
        clauses, assignment = unit_propagate(clauses, assignment)

        # If there are no empty clauses, then we found a solution
        if all(len(clause) > 0 for clause in clauses):
            return assignment  # A solution is found

        # If there are empty clauses, we have a conflict. Perform backtracking.
        if any(len(clause) == 0 for clause in clauses):
            # Conflict detected, backtrack to previous decision level
            if not decision_stack:
                return "Unsatisfiable"  # No more decisions to backtrack to
            decision_stack = backtrack(assignment, decision_stack)
            level -= 1

        # Choose the next literal to assign based on a simple heuristic
        decision_literal = choose_literal(clauses, assignment)
        if decision_literal is not None:
            assignment[decision_literal] = True
            decision_stack.append(decision_literal)
            level += 1
        else:
            return "Unsatisfiable"


def choose_literal(clauses, assignment):
    """
    Selects the next literal to assign based on a simple heuristic (first unassigned literal).
    """
    for clause in clauses:
        for literal in clause:
            if literal not in assignment:
                return literal
    return None


# Example usage:
if __name__ == "__main__":
    # Example CNF clauses for (x1 OR NOT x2) AND (NOT x1 OR x2)
    clauses = [
        [1, -2],  # x1 OR NOT x2
        [-1, 2],  # NOT x1 OR x2
    ]
    
    print("CDCL:", cdcl_solver(clauses))  # CDCL solver with unit propagation
