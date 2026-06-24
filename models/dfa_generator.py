from graphviz import Digraph

def create_dfa(regex_type):

    dot = Digraph()
    dot.attr(rankdir='LR')

    if regex_type == "digits":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', '0-9')
        dot.edge('q1', 'q1', '0-9')

    elif regex_type == "binary":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', '0,1')
        dot.edge('q1', 'q1', '0,1')

    elif regex_type == "alphabets":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', 'a-z')
        dot.edge('q1', 'q1', 'a-z')

    elif regex_type == "email":

        dot.node('q0')
        dot.node('q1')
        dot.node('q2')
        dot.node('q3', shape='doublecircle')

        dot.edge('q0', 'q1', 'user')
        dot.edge('q1', 'q2', '@')
        dot.edge('q2', 'q3', 'domain')

    elif regex_type == "alphanumeric":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', 'A-Z,a-z,0-9')
        dot.edge('q1', 'q1', 'A-Z,a-z,0-9')

    elif regex_type == "hexadecimal":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', '0-9,A-F')
        dot.edge('q1', 'q1', '0-9,A-F')

    elif regex_type == "float":

        dot.node('q0')
        dot.node('q1')
        dot.node('q2', shape='doublecircle')

        dot.edge('q0', 'q1', 'digits')
        dot.edge('q1', 'q2', '.')
        dot.edge('q2', 'q2', 'digits')

    elif regex_type == "start":

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', 'start')
        dot.edge('q1', 'q1', 'any')

    elif regex_type == "end":

        dot.node('q0')
        dot.node('q1')
        dot.node('q2', shape='doublecircle')

        dot.edge('q0', 'q1', 'any')
        dot.edge('q1', 'q2', 'end')

    elif regex_type == "substring":

        dot.node('q0')
        dot.node('q1')
        dot.node('q2', shape='doublecircle')

        dot.edge('q0', 'q1', 'substring')
        dot.edge('q1', 'q2', 'accept')

    else:

        dot.node('q0')
        dot.node('q1', shape='doublecircle')

        dot.edge('q0', 'q1', 'input')

    filename = 'static/dfa'

    dot.render(filename, format='png', cleanup=True)

    return 'dfa.png'