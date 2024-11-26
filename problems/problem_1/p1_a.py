from collections import deque

def is_bipartite(g_l):
    color = {}  #dict of colors

    for node in g_l:
        if node not in color:  #unvisited node
            queue = deque([node])
            color[node] = 0  
            for neighbor in g_l[node]:
                    if neighbor in color: 
                         color[node] = 1- color[neighbor]
            

            while queue:
                current = queue.popleft()

                for neighbor in g_l[current]:
                    if neighbor not in color: 
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:  
                        return 0  # Graph is not bipartite

    return 1  # Graph is bipartite
