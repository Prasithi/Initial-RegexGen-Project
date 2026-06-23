from graphviz import Digraph

dot = Digraph()

dot.node('A')
dot.node('B')

dot.edge('A', 'B')

dot.render('test_graph', format='png', cleanup=True)

print("Success")