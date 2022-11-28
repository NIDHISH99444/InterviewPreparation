

from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v):
    graph[u].append(v)


def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def topologicalDFS(vertex ,stack):
    visited[vertex]=1
    for neighbour in graph[vertex]:
        if visited[neighbour]!=1:
            topologicalDFS(neighbour,stack)
    stack.append(vertex)



def check(vis,stack):
    for i in range(0,6):
        if vis[i]!=1:
            topologicalDFS(i,stack)
    print("Topological Ordering is : ")
    while stack:
        print(stack.pop())



addEdge(5, 0)
addEdge(5, 2)
addEdge(4, 0)
addEdge(4, 1)
addEdge(2, 3)
addEdge(3, 1)


print(graph)
visited =[0] *6
print(visited)
stack=[]
print(check(visited,stack))









