# DFS IMPLEMENTATION 2 (https://www.youtube.com/watch?v=PMMc4VsIacU&list=PLpXOY-RxVRTPPVLBP6-sz6CMWxhtrI-v_&index=3)

# Setup graph (must be consecutive numbers)
graph = []

# Each array item corresponds to where each index connects to
# Example: This is vertex zero - the array is the connections
graph.append([1, 2, 3])
# This is vertex 1
graph.append([0, 3])
# and so on...
graph.append([0, 3])
graph.append([0, 1, 2, 4])
graph.append([3])

# Run DFS
marked = [False] * len(graph)

def dfs_iterative(graph, givenVertex):
    stack = [givenVertex]
    while (len(stack) > 0):
        currentVertex = stack.pop()
        print(currentVertex)
        if not marked[currentVertex]:
            neighbors = graph[currentVertex]
            marked[currentVertex] = True
            for v in neighbors:
                if not marked[v]:
                    # add each neighbor to the stack (or queue)
                    stack.append(v)
        # if len(stack) > 10:
        #     break

dfs_iterative(graph, 0)
print(marked)