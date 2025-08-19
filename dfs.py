from collections import deque

# def dfs(graph,node,visited = None):
#     if visited is None:
#         visited = set()
#     visited.add(node)
#     print(node,end ='')
#     for neighbour in graph[node]:
#         if neighbour not in visited:
#             dfs(graph, neighbour,visited)
# graph ={
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':['F'],
#     'F':[]
# 
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print()

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }
graph = {
    'A': ['D', 'E'],
    'B': ['B', 'C'],
    'C': ['D'],
    'D': ['B','C'],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')