import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        g = Graph()
        g.addEdge('A', 'B')
        g.addEdge('A', 'C')
        g.addEdge('B', 'C')
        g.addEdge('B', 'D')
        g.addEdge('A', 'E')
        g.addEdge('E', 'D')
        g.addEdge('D', 'E')
        g.addEdge('E', 'A')

        self.g = g

    def test_adjacent(self):
        g = self.g
        self.assertTrue(g.adjacent('A', 'B'))
        self.assertTrue(g.adjacent('A', 'C'))
        self.assertTrue(g.adjacent('B', 'C'))
        self.assertFalse(g.adjacent('A', 'D'))

    def test_neighbors(self):
        g = self.g

        cases = [dict(actual=g.neighbors('A'), expect=('B', 'C')),
                 dict(actual=g.neighbors('B'), expect=('C', 'D'))]

        for c in cases:
            for i in c['expect']:
                self.assertTrue(i in c['actual'])

    def test_bfs(self):
        g = self.g

        cases = [dict(src='A', dst='B', result=True),
                 dict(src='A', dst='C', result=True),
                 dict(src='A', dst='D', result=True),
                 dict(src='B', dst='E', result=True),
                 dict(src='E', dst='D', result=True),
                 dict(src='D', dst='A', result=True),
                 dict(src='C', dst='A', result=False)]

        for c in cases:
            self.assertEqual(c['result'], g.bfs(c['src'], c['dst'])[0])

    def test_dfs(self):
        g = self.g

        cases = [dict(src='A', dst='B', result=True),
                 dict(src='A', dst='C', result=True),
                 dict(src='A', dst='D', result=True),
                 dict(src='B', dst='E', result=True),
                 dict(src='E', dst='D', result=True),
                 dict(src='D', dst='A', result=True),
                 dict(src='C', dst='A', result=False)]

        for c in cases:
            self.assertEqual(c['result'], g.dfs(c['src'], c['dst'])[0])
