from data_structures.undirected_graph.undirected_graph import UndirectedGraph


class TestUndirectedGraph:
    def test_initialization(self):
        graph = UndirectedGraph()
        assert isinstance(graph, UndirectedGraph)

    def test_build_graph_from_lists(self):
        from_product = [1, 2, 2, 3, 4]
        to_product = [2, 3, 4, 4, 5]
        graph = UndirectedGraph.from_lists(5, from_product, to_product)

        node1 = graph.nodes[0]
        node2 = graph.nodes[1]
        node3 = graph.nodes[2]
        node4 = graph.nodes[3]
        node5 = graph.nodes[4]

        assert node1.key == 1
        assert node2 in node1.connections

        assert node2.key == 2
        assert node1 in node2.connections
        assert node3 in node2.connections
        assert node4 in node2.connections

        assert node3.key == 3
        assert node2 in node3.connections
        assert node4 in node3.connections

        assert node4.key == 4
        assert node2 in node4.connections
        assert node3 in node4.connections
        assert node5 in node4.connections

        assert node5.key == 5
        assert node4 in node5.connections


class TestUndirectedGraphNode:
    def test_initialization(self):
        node = UndirectedGraph.Node()
        assert isinstance(node, UndirectedGraph.Node)

    def test_node_with_data(self):
        node = UndirectedGraph.Node(1)
        assert node.data == 1

    def test_connect_nodes(self):
        node1 = UndirectedGraph.Node(1)
        node2 = UndirectedGraph.Node(2)
        node1.connect(node2)
        assert node2 in node1.connections
        assert node1 in node2.connections
