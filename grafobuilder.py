# Graphviz Documentation
#   https://graphviz.org/documentation/

# Graphviz with Python
#   https://graphviz.readthedocs.io/en/stable/

# Digraph é um grafo direcionado
from graphviz import Digraph

dot = Digraph('Gerador de autômatos', filename='automato-gerado')

dot.attr(rankdir='LR')

dot.attr('node', shape='circle')
dot.attr('edge', arrowsize='0.8')

dot.node('inicio', '', shape='plaintext')

with open("02-teste-AFND.txt","r") as data:
    for line in data:
        if line.strip() == "#S":
            break
    
    firststate = data.readline().rstrip()
    dot.edge('inicio', firststate, shape='invis')

    for line in data:
        if line.strip() == "#F":
            break

    for state in data.readline().rstrip().split():
        dot.node(state, state, shape='doublecircle')

    # Encontrar início das transições
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