import unittest
from directedgraph import DirectedGraph


class DirectedGraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph("Graph")

    def test_init(self):
        self.assertEqual(self.graph.name, "Graph")
        self.assertEqual(self.graph.dict, {})

    def test_add_edge(self):
        self.assertEqual(
            {'Misho': [], 'Pesho': ['Misho']}, self.graph.add_edge("Pesho", "Misho"))
        self.assertEqual(self.graph.add_edge("Pesho", "Sasho"), {
                         'Sasho': [], 'Misho': [], 'Pesho': ['Misho', 'Sasho']})

    def test_get_neighbors_for(self):
        self.graph.add_edge("Pesho", "Misho")
        self.assertEqual(self.graph.get_neighbors_for("Pesho"), ["Misho"])

    def test_path_between(self):
        pass

    def test_str(self):
        # self.graph.add_edge("Pesho", "Misho")
        # self.graph.add_edge("Pesho", "Sasho")
        # self.graph.add_edge("Mitko", "Misho")
        # self.graph.__str__()
        pass

    def test_path_between(self):
        self.graph.add_edge("Pesho", "Misho")
        self.graph.add_edge("Misho", "Sasho")
        self.graph.add_edge("Sasho", "Mitko")
        self.assertTrue(self.graph.path_between("Pesho", "Mitko"))
if __name__ == '__main__':
    unittest.main()
