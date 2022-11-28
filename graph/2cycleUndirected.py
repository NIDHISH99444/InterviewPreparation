

from collections import defaultdict
graph= defaultdict(list)

def addEdge(u ,v):
    graph[u].append(v)

def printStru(u):
    for i in range(u):
        print(i ,graph[i])

def cycle(vertex ,parent,visited):
    visited[vertex] =True
    for neighbour in graph[vertex]:

        if neighbour == parent:
            continue
        else:
            if visited[neighbour]==True:
                return  True
        if cycle(neighbour,vertex,visited) :
            return True
        return  False


addEdge(1, 2)
addEdge(2, 3)
addEdge(3, 4)
addEdge(4, 5)
addEdge(5, 3)
visited =[False] *6
print(cycle(1,-1,visited))






