import os
def parse_dimacs_file(filename):
    with open(filename, 'r') as file:
        clauses = []
        for line in file:
            line = line.strip()
            if line.startswith('c') or line.startswith('p') or not line:
                continue
            literals = list(map(int, line.split()))
            if literals[-1] == 0:
                literals = literals[:-1]
            clauses.append(literals)
    return clauses

# Test the parser directly
if __name__ == "__main__":
    path = os.path.join("test_files", "problem1.cnf")
    result = parse_dimacs_file(path)
    print("Parsed clauses:", result)
