from graphviz import Digraph
import re


def create_dfa(regex):

    dot = Digraph("DFA", format="png")

    dot.attr(rankdir="LR")
    dot.attr(bgcolor="white")
    dot.attr(splines="true")
    dot.attr(nodesep="0.8")
    dot.attr(ranksep="1")

    dot.attr(
        "node",
        shape="circle",
        fontsize="16",
        fontname="Arial",
        width="1",
        height="1"
    )

    dot.node("", shape="none")
    dot.node("q0")
    dot.node("q1", shape="doublecircle")

    dot.edge("", "q0")

    if re.fullmatch(r"\^\[0-9\]\+\$", regex):

        dot.edge("q0", "q1", "0-9")
        dot.edge("q1", "q1", "0-9")

    elif re.fullmatch(r"\^\[a-zA-Z\]\+\$", regex):

        dot.edge("q0", "q1", "A-Z a-z")
        dot.edge("q1", "q1", "A-Z a-z")

    elif re.fullmatch(r"\^\[01\]\+\$", regex):

        dot.edge("q0", "q1", "0 , 1")
        dot.edge("q1", "q1", "0 , 1")

    elif regex.startswith("^"):

        text = regex.replace("^", "").replace(".*", "")

        dot.edge("q0", "q1", text)
        dot.edge("q1", "q1", "Σ")

    elif regex.endswith("$"):

        text = regex.replace("$", "").replace(".*", "")

        dot.edge("q0", "q1", "Σ")
        dot.edge("q1", "q1", text)

    elif ".*" in regex:

        text = regex.replace(".*", "")

        dot.edge("q0", "q1", text)
        dot.edge("q1", "q1", "Σ")

    elif "@" in regex:

        dot.node("q2")
        dot.node("q3", shape="doublecircle")

        dot.edge("", "q0")

        dot.edge("q0", "q1", "username")
        dot.edge("q1", "q2", "@")
        dot.edge("q2", "q3", "domain")

    else:

        dot.edge("q0", "q1", "input")
        dot.edge("q1", "q1", "input")

    dot.render("static/dfa", cleanup=True)

    return "dfa.png"