# Problem 2
from collections import defaultdict, deque

def find_paths(n, paths):
    from collections import defaultdict, deque

def find_paths(n, paths):
    """
    Compute the minimal number of paths to block so that there’s no path between junctions 1 and n.

    Parameters:
    n (int): Total number of junctions.
    paths (list of tuple): List of tuples representing bidirectional edges (x, y).

    Returns:
    int: The minimum number of paths to block.
    """
    graph = defaultdict(list)
    capacity = [[0] * (n + 1) for _ in range(n + 1)]

    for x, y in paths:
        graph[x].append(y)
        graph[y].append(x) 
        capacity[x][y] += 1
        capacity[y][x] += 1

    # Edmonds-Karp implementation of max flow
    def bfs(source, sink, parent):
        """Perform BFS to find an augmenting path."""
        visited = [False] * (n + 1)
        queue = deque([source])
        visited[source] = True

        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if not visited[neighbor] and capacity[current][neighbor] > 0:  
                    parent[neighbor] = current
                    visited[neighbor] = True
                    if neighbor == sink:
                        return True
                    queue.append(neighbor)
        return False

    def edmonds_karp(source, sink):
        """Find the maximum flow using Edmonds-Karp algorithm."""
        parent = [-1] * (n + 1)
        max_flow = 0

        while bfs(source, sink, parent):

            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, capacity[parent[s]][s])
                s = parent[s]

            v = sink
            while v != source:
                u = parent[v]
                capacity[u][v] -= path_flow
                capacity[v][u] += path_flow
                v = u

            max_flow += path_flow

        return max_flow


    return edmonds_karp(1, n)
