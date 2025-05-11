import random

def walksat_solver(clauses, max_flips=1000, p=0.5):
    symbols = set(abs(l) for c in clauses for l in c)
    model = {s: random.choice([True, False]) for s in symbols}

    for _ in range(max_flips):
        unsatisfied = [c for c in clauses if not any(model.get(abs(l), False) == (l > 0) for l in c)]
        if not unsatisfied:
            return model

        clause = random.choice(unsatisfied)
        if random.random() < p:
            sym = abs(random.choice(clause))
        else:
            sym = max(clause, key=lambda l: evaluate_flip(clauses, model, abs(l)))[0]

        model[sym] = not model[sym]

    return False


def evaluate_flip(clauses, model, symbol):
    model[symbol] = not model[symbol]
    score = sum(any(model.get(abs(l), False) == (l > 0) for l in c) for c in clauses)
    model[symbol] = not model[symbol]
    return score
