# DFS IMPLEMENTATION 1 (https://www.youtube.com/watch?v=PMMc4VsIacU&list=PLpXOY-RxVRTPPVLBP6-sz6CMWxhtrI-v_&index=3)

# Setup graph (must be consecutive numbers)
graph = []

# Each array item corresponds to where each index connects to
graph.append([1, 2, 3])
graph.append([0, 3])
graph.append([0, 3])
graph.append([0, 1, 2, 4])
graph.append([3])

# Run DFS
marked = [False] * len(graph)
print(marked, len(marked))

def dfs(graph, givenVertex):
    print(givenVertex)
    # "visit" givenVertex
    neighbors = graph[givenVertex]
    # marked the vertex as seen before
    marked[givenVertex] = True
    
    # for each vertex
    for v in neighbors:
        if not marked[v]:
            dfs(graph, v)

dfs(graph, 0)
print(marked)

## VISUALIZING / RENDERING GRAPH ON SCREEN ##

