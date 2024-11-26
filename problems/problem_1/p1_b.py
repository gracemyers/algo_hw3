# Problem 1b


def maximal_bipartite_match(g) -> int:
    def bpm(u, match_r, visited):
        for v in range(len(g[0])):  
            if g[u][v] == 1 and not visited[v]: 
                visited[v] = True  #

                if match_r[v] == -1 or bpm(match_r[v], match_r, visited):
                    match_r[v] = u  
                    return True
        return False

    num_left = len(g)  # Rows
    num_right = len(g[0])  # Columns

    # Array to store matches (-1 means no match)
    match_r = [-1] * num_right

    # Count of matches
    result = 0
    for u in range(num_left):
        visited = [False] * num_right
        if bpm(u, match_r, visited):
            result += 1

    return result