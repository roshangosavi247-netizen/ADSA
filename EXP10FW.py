INF = float('inf')

def floyd_warshall(graph, n):
    # Initialize dist matrix as a deep copy of graph
    dist = [row[:] for row in graph]

    # Outer loop for intermediate vertex k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

    # Check for negative-weight cycles
    for i in range(n):
        if dist[i][i] < 0:
            print("Warning: Graph contains a negative-weight cycle!")
            return None

    # Print resulting distance matrix
    print("Shortest Distance Matrix (All-Pairs):")
    for row in dist:
        print("".join(f"{'INF':>7}" if d == INF else f"{d:>7}" for d in row))

    return dist


if __name__ == "__main__":
    n = 4
    graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]

    floyd_warshall(graph, n)
