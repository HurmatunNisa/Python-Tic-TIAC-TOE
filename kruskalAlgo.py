class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

    def kruskal_algorithm(self):
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        i = 0
        while len(result) < self.vertices - 1:
            src, dest, weight = self.graph[i]
            i += 1

            root_src = self.find_parent(parent, src)
            root_dest = self.find_parent(parent, dest)

            if root_src != root_dest:
                result.append((src, dest, weight))
                self.union(parent, rank, root_src, root_dest)

        return result


# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.kruskal_algorithm()
print("Minimum Spanning Tree:", minimum_spanning_tree)
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

    def kruskal_algorithm(self):
        result = []

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        i = 0
        while len(result) < self.vertices - 1:
            src, dest, weight = self.graph[i]
            i += 1

            root_src = self.find_parent(parent, src)
            root_dest = self.find_parent(parent, dest)

            if root_src != root_dest:
                result.append((src, dest, weight))
                self.union(parent, rank, root_src, root_dest)

        return result


# Example usage:
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

minimum_spanning_tree = g.kruskal_algorithm()
print("Minimum Spanning Tree:", minimum_spanning_tree)
