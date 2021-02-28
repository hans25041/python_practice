from data_structures.undirected_graph.depth_first_traversal \
    import DepthFirstTraversal
from data_structures.undirected_graph.undirected_graph import UndirectedGraph


class TestDepthFirstTraversal:
    def test_initialization(self):
        graph = self._create_cyclic_graph()
        dft = DepthFirstTraversal(graph)
        assert isinstance(dft, DepthFirstTraversal)
        assert dft.graph == graph

    def test_traverse_cyclic_graph(self):
        graph = self._create_cyclic_graph()
        traversal = DepthFirstTraversal(graph)
        assert traversal.graph == graph
        traversal.traverse()
        assert traversal.visited == set(graph.nodes)
        assert traversal.has_cycles
        assert 3 in traversal.cycle_lengths

    def test_traverse_acyclic_graph(self):
        graph = self._create_acyclic_graph()
        traversal = DepthFirstTraversal(graph)
        assert traversal.graph == graph
        traversal.traverse()
        assert traversal.visited == set(graph.nodes)
        assert not traversal.has_cycles

    def _create_cyclic_graph(self):
        from_product = [1, 2, 2, 3, 4]
        to_product = [2, 3, 4, 4, 5]
        return UndirectedGraph.from_lists(5, from_product, to_product)

    def _create_acyclic_graph(self):
        from_product = [1, 2, 3, 3, 4]
        to_product = [2, 3, 4, 5, 6]
        return UndirectedGraph.from_lists(5, from_product, to_product)
