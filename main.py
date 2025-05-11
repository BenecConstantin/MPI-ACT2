from utils.parser import parse_dimacs_file
from solvers.resolution import resolution_solver
from solvers.dp import dp_solver
from solvers.dpll import dpll_solver
from solvers.cdcl import cdcl_solver
from solvers.walksat import walksat_solver
import sys

if __name__ == "__main__":
    filename = "test_files/problem1.cnf"
    clauses = parse_dimacs_file(filename)
    print (clauses)

    print("Resolution:", resolution_solver(clauses))
    print("DP:", dp_solver(clauses))
    print("DPLL:", dpll_solver(clauses))
    print("CDCL:", cdcl_solver(clauses))
    print("WalkSAT:", walksat_solver(clauses))