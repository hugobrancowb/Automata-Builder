# Graphviz Documentation
#   https://graphviz.org/documentation/

# Graphviz with Python
#   https://graphviz.readthedocs.io/en/stable/

# Import graphviz
from graphviz import Digraph

dot = Digraph('automata drawer', filename='automato-gerado')

dot.attr(rankdir='LR')

dot.attr('node', shape='circle')
dot.attr('edge', arrowsize='0.8')

# 'nullplace' is a invisible node created so we can put an arrow pointing to the automata's start place
dot.node('nullplace', '', shape='plaintext')

with open("02-teste-AFND.txt","r") as data:
    # Find where the line where we say the place the automata begins
    for line in data:
        if line.strip() == "#S":
            break
    
    # Gets that place and points an arrow to it
    firststate = data.readline().rstrip()
    dot.edge('nullplace', firststate, shape='invis')

    # Find where the line where we say the place or places the automata ends
    for line in data:
        if line.strip() == "#F":
            break

    for state in data.readline().rstrip().split():
        dot.node(state, state, shape='doublecircle')

    # Find where the line where we list all automata's transitions
    for line in data:
        if line.strip() == "#D":
            break

    for line in data:
        line = line.rstrip('\r\n')
        
        if len(line) == 0:
            break
        
        ei, le, ef = line.split()

        dot.edge(ei, ef, label=le)

dot.render(view=True)