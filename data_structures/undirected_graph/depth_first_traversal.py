class DepthFirstTraversal:

    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.parents = {}
        self.has_cycles = False

    def traverse(self):
        for start_node in self.graph.nodes:
            if start_node in self.visited:
                continue
            self.traverse_node(start_node)

    def traverse_node(self, node, parent=None):
        print("-----------------")
        print(f"Node: {node!r}")
        print(f"Parent: {parent!r}")
        print(f"Parents: {self.parents!r}")
        print("------------------")
        if node in self.visited:
            if node not in self.parents[parent]:
                self.has_cycles = True
            return
        self.visit(node)
        self.set_parent(node, parent)
        for connected_node in node.connections:
            self.traverse_node(connected_node, node)

    def visit(self, node):
        self.visited.add(node)

    def set_parent(self, node, parent):
        data = parent.key if parent else None
        self.parents[node.key] = data

