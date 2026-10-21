def hamiltonian(n, graph):
    path = [-1] * n
    path[0] = 0

    def solve(pos):
        if pos == n:
            return graph[path[n - 1]][path[0]] == 1

        for v in range(1, n):
            if graph[path[pos - 1]][v] == 1 and v not in path:
                path[pos] = v

                if solve(pos + 1):
                    return True

                path[pos] = -1

        return False

    if solve(1):
        print("Hamiltonian Cycle:", [v + 1 for v in path] + [1])
    else:
        print("Hamiltonian cycle does not exist")


n = 5
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

hamiltonian(n, graph)