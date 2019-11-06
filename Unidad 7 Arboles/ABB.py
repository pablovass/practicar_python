#!/usr/bin/python3

from graphviz import Digraph

class NodoArbol:
    def __init__(self, dato = None):
        self.data = dato
        self.left = None
        self.right = None

    def treePlot(self, dot):
        if self.hasLeft():
            dot.node(str(self.left.data), str(self.left.data))
            dot.edge(str(self.data), str(self.left.data))
            self.left.treePlot(dot)
        if self.hasRight():
            dot.node(str(self.right.data), str(self.right.data))
            dot.edge(str(self.data), str(self.right.data))
            self.right.treePlot(dot)

class ABB:
    def __init__(self):
        self.root = None

    def treePlot(self, fileName='tree'):
        if not self.isEmpty():
            treeDot = Digraph()
            treeDot.node(str(self.root.data), str(self.root.data))
            self.root.treePlot(treeDot)
            treeDot.render(fileName, view=True)
