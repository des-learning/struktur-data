from queue import Queue

class Graph:
    def __init__(self):
        self.edges = dict()

    def addEdge(self, src, dst):
        edge = self.edges.get(src, set())
        edge.add(dst)
        self.edges[src] = edge

    def removeEdge(self, src, dst):
        edge = self.edges.get(src, None)
        if edge is not None:
            edge.remove(dst)
            if len(edge) == 0:
                del self.edges[src]

    def adjacent(self, src, dst):
        return dst in self.edges.get(src, set())

    def neighbors(self, src):
        return self.edges.get(src, set())

    def bfs(self, src, dst):
        queue = Queue()
        queue.put(src)
        visited = list(src)

        while not queue.empty():
            vertexes = self.edges.get(queue.get(), set())
            for v in vertexes:
                if v == dst:
                    visited.append(v)
                    return (True, visited)
                if v not in visited:
                    queue.put(v)
                    visited.append(v)

        return (False, visited)

    def dfs(self, src, dst):
        stack = list(src)
        discovered = list()
        while len(stack) != 0:
            vertex = stack.pop()
            if vertex not in discovered:
                discovered.append(vertex)
                if vertex == dst:
                    return (True, discovered)
                stack.extend(self.edges.get(vertex, set()))
        return (False, discovered)


    def __repr__(self):
        return repr(self.edges)
