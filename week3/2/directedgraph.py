class DirectedGraph:

    def __init__(self, name):
        self.name = name
        self.dict = {}

    def add_edge(self, node_a, node_b):
        if node_a not in self.dict:
            self.dict[node_a] = []
        if node_b not in self.dict:
            self.dict[node_b] = []
        self.dict[node_a].append(node_b)
        return self.dict

    def get_neighbors_for(self, node):
        return self.dict[node]

    def path_between(self, node_a, node_b):
        if node_a not in self.dict or node_b not in self.dict:
            return False
        elif node_b in self.get_neighbors_for(node_a):
            return True

        for node in self.get_neighbors_for(node_a):
            if self.path_between(node, node_b):
                return True
        return False

    def __str__(self):
        for edge in self.dict:
            for node in self.dict[edge]:
                print (edge , " -> ", node)
