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
    #create a graph with ancestor relationships as edges
    g = Graph()
    for anc in ancestors:
        if anc[0] not in g.vertices:
            g.add_vertex(anc[0])

        if anc[1] not in g.vertices:
            g.add_vertex(anc[1])

        g.add_edge(anc[1], anc[0])

    #do a depth first traversal, which returns the entire graph with Nones where there was a dead end
    parents = g.dft(start)
    indexes = []
    #loop through parents backwards if there is a pattern of None number None number, those were tied for path length. If they Nones are more spread out, then they were not of equal length. Save the indexes of the numbers at the end of the longest path(s) in indexes
    for i in range(len(parents)-1, -1, -1):
        if parents[i] == None:
            indexes.append(i-1)
    #initialize an array to hold the oldest ancestors, beginning with the first
    ends = [parents[indexes[0]]]
    for i in range(len(indexes)-1):

        #if the differences of the indexes is 2, the lengths are equal, add to ends array
        if indexes[i+1] - indexes[i] == -2:
            ends.append(parents[indexes[i+1]])
    #grab the minimum number, as instructed if there is more than one
    result = min(ends)
    #if this number is the same as the starting number, there was no ancestor, so return -1
    if result == start:
        return -1
    #otherwise return oldest ancestor
    else:
        return result



# print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 8))

