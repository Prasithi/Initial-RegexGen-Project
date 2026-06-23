from graphviz import Digraph

def create_dfa():

    dot = Digraph()

    dot.attr(rankdir='LR')

    dot.node('q0')
    dot.node('q1', shape='doublecircle')

    dot.edge('q0', 'q1', label='a')

    dot.render(
        'static/dfa',
        format='png',
        cleanup=True
    )

    return "dfa.png"