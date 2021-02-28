class UndirectedGraph:

    def __init__(self):
        self.nodes = []
        self.nodes_by_value = {}

    @classmethod
    def from_lists(cls, list_length, from_list, to_list):
        graph = cls()
        for i in range(list_length):
            from_node = graph.node(from_list[i])
            to_node = graph.node(to_list[i])
            from_node.connect(to_node)
        return graph

    def node(self, i):
        if i not in self.nodes_by_value:
            node = UndirectedGraph.Node(i)
            self.nodes.append(node)
            self.nodes_by_value[i] = self.nodes[-1]
        return self.nodes_by_value[i]

    class Node:
        def __init__(self, data=None):
            self.data = data
            self.connections = set()

        def __str__(self):
            return self.data

        def __repr__(self):
            connections = [c.key for c in self.connections]
            return f"{self.data} -> {connections}"

        def connect(self, other):
            self.connections.add(other)
            other.connections.add(self)
