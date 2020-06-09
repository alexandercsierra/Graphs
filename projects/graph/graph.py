"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

visited_nodes = []

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
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

    def bft(self, starting_vertex):
        #uses a queue
        start = starting_vertex
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:

            #deq current
            current = q.dequeue()
            #add current vertex to visited if it isn't already there
            if current not in visited:
                print(current)
                visited.add(current)

                #add all neighbors to q
                for vert in self.get_neighbors(current):
                    q.enqueue(vert)
            

    def dft(self, starting_vertex):
        #uses a stack
        start = starting_vertex
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:

            #pop current
            current = s.pop()
            #add current vertex to visited if it isn't already there
            if current not in visited:
                print(current)
                visited.add(current)

                #add all neighbors to q
                for vert in self.get_neighbors(current):
                    s.push(vert)

    def dft_recursive(self, starting_vertex):
        curr = starting_vertex
        print(curr)
        if curr not in visited_nodes:
            visited_nodes.append(curr)

            for vert in self.get_neighbors(curr):
                if vert not in visited_nodes:
                    self.dft_recursive(vert)
                

    def bfs(self, starting_vertex, destination_vertex):
        
        start = starting_vertex
        q = Queue()
        q.enqueue([starting_vertex])

        while q.size() > 0:
            current_path = q.dequeue()
            if current_path[-1] == destination_vertex:
                return current_path

            for vert in self.get_neighbors(current_path[-1]):
                
                new_path = [*current_path, vert]
                q.enqueue(new_path)
                





    def dfs(self, starting_vertex, destination_vertex):
        start = starting_vertex
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            current_path = s.pop()
            if current_path[-1] == destination_vertex:
                return current_path

            for vert in self.get_neighbors(current_path[-1]):
                
                new_path = [*current_path, vert]
                s.push(new_path)
        

    def dfs_recursive(self, starting_vertex, destination_vertex):
        current_path = starting_vertex
        if type(starting_vertex) == int:
            current_path = [starting_vertex]

        if current_path[-1] == destination_vertex:
            return current_path

        for vert in self.get_neighbors(current_path[-1]):
                new_path = [*current_path, vert]
                self.dfs_recursive(new_path, destination_vertex)


    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     current_path = starting_vertex
    #     if type(starting_vertex) == int:
    #         current_path = [starting_vertex]

    #     print('current_path', current_path)
    #     if current_path[-1] == destination_vertex:
    #         print('in if', current_path)
    #         return current_path
    #     if current_path[-1] not in visited_nodes:
    #         visited_nodes.append(current_path[-1])

    #     for vert in self.get_neighbors(current_path[-1]):
    #         if vert not in visited_nodes:
    #             new_path = [*current_path, vert]
    #             self.dfs_recursive(new_path, destination_vertex)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # print(graph.dft_recursive(1))

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
