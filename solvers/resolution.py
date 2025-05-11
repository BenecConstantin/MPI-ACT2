# resolution.py - Resolving clauses using the resolution rule

def resolve(ci, cj):
    """
    Resolves two clauses ci and cj by removing complementary literals.
    For example: ci = [1, -2], cj = [-1, 3] -> Resolvent = [-2, 3]
    """
    resolvent = set(ci)  # Convert list to set to perform set operations
    for literal in cj:
        if -literal in resolvent:  # If complementary literal is found
            resolvent.remove(-literal)  # Remove the complementary literal
            resolvent.add(literal)  # Add the current literal from cj
    return list(resolvent)  # Convert the set back to a list


def resolution_solver(clauses):
    """
    Applies the resolution rule to the clauses until no more resolutions can be made.
    """
    resolvents = set()
    for i in range(len(clauses)):
        for j in range(i + 1, len(clauses)):
            # Resolve each pair of clauses ci and cj
            new_clause = resolve(clauses[i], clauses[j])
            if new_clause:  # Only add non-empty resolvents
                resolvents.add(tuple(new_clause))  # Store resolvent as a tuple to avoid duplicates

    # Convert back to list and return the resolvents
    return [list(resolvent) for resolvent in resolvents]

# Example usage:
if __name__ == "__main__":
    # Example CNF clauses for (x1 OR NOT x2) AND (NOT x1 OR x2)
    clauses = [
        [1, -2],  # x1 OR NOT x2
        [-1, 2],  # NOT x1 OR x2
    ]
    
    print("Resolution:", resolution_solver(clauses))
