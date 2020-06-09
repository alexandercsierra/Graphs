from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        #uses a stack
        start = starting_vertex
        s = Stack()
        s.push(starting_vertex)

        visited = []

        while s.size() > 0:

            #pop current
            current = s.pop()
            #add current vertex to visited if it isn't already there
            if current not in visited:
                # print(current)
                visited.append(current)

                #add all neighbors to q
                if len(self.get_neighbors(current)) > 0:
                    for vert in self.get_neighbors(current):
                        s.push(vert)
                else:
                    visited.append(None)
        return visited
        
def earliest_ancestor(ancestors, start):
    g = Graph()
    for anc in ancestors:
        if anc[0] not in g.vertices:
            g.add_vertex(anc[0])

        if anc[1] not in g.vertices:
            g.add_vertex(anc[1])

        g.add_edge(anc[1], anc[0])


    parents = g.dft(start)
    indexes = []
    for i in range(len(parents)-1, -1, -1):
        if parents[i] == None:
            indexes.append(i-1)
    ends = [parents[indexes[0]]]
    for i in range(len(indexes)-1):


        if indexes[i+1] - indexes[i] == -2:
            ends.append(parents[indexes[i+1]])

    result = min(ends)
    if result == start:
        return -1
    else:
        return result



# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8))

