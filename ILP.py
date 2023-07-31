import time
from ortools.linear_solver import pywraplp
import networkx as nx


start_time = time.time()
G = nx.path_graph(20)

def main():
    n = len(list(G.nodes))
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # variables
    f = [[solver.BoolVar(f'f[{i}][{j}]') for j in range(n)] for i in range(n)]
    b = [[solver.BoolVar(f'b[{i}][{j}]') for j in range(n)] for i in range(n)]
    c = [solver.BoolVar(f'c{i}') for i in range(n)]
    i = solver.IntVar(0, n, "i")
    v = solver.IntVar(0, n, "v")

    # Constraints

    for i in range(n):
        for j in range(n-1):
            solver.Add(b[i][j] >= f[i][j])

    for i in range(n):
        solver.Add(sum(f[i]) <= 1)

    for i in range(n-1):
        for j in range(n-1):
            solver.Add(b[i + 1][j] >= b[i][j])

    for j in range(n-1):
        solver.Add(b[0][j] == 0)

    for i in range(n):
        for j in range(n-1):
            solver.Add(c[i] <= b[i][j])

    for i in range(n):
        solver.Add((sum(b[i]) - n + 1) <= c[i])

    for i in range(n-1):
        for j in range(n-1):
            for k in G[j]:
                solver.Add(b[i + 1][k] >= b[i][j])

    for i in range(n-1):
        for j in range(n-1):
            sum_var = sum(b[i][k] for k in G[j])
            solver.Add(b[i + 1][j] <= sum_var + f[i + 1][j])

    objective = solver.Objective()
    for i in range(n):
        objective.SetCoefficient(c[i], 1)

    objective.SetMaximization()


    status = solver.Solve()


    if status == pywraplp.Solver.OPTIMAL:
        print('Burning Number =', n - solver.Objective().Value())




main()
end_time = time.time()
running_time=end_time - start_time
print('Running Time:', running_time, 'seconds')