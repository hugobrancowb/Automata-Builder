# Graphviz Documentation
#   https://graphviz.org/documentation/

# Graphviz with Python
#   https://graphviz.readthedocs.io/en/stable/

# Import graphviz
from graphviz import Digraph

dot = Digraph('automata-builder', filename='automata')

dot.attr(rankdir='LR')

dot.attr('node', shape='circle')
dot.attr('edge', arrowsize='0.8')

# 'nullplace' is a invisible node created so we can put an arrow pointing to the automata's start place
dot.node('nullplace', '', shape='plaintext', fixedsize='shape', width='0.01')

transitions = []
ignore = []

with open("01-teste-AFD.txt","r") as data:
    # Find where the line where we say the place the automata begins
    for line in data:
        if line.strip() == "#S":
            break
    
    # Gets that place and points an arrow to it
    firststate = data.readline().rstrip()
    dot.edge('nullplace', firststate)

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

        transitions.append([ei, le, ef])

# Merge paths with same begining and ending
for i in range(len(transitions)):
    ei, le, ef = transitions[i]

    for j in range(i-1, 0, -1):
        if ei == transitions[j][0] and ef == transitions[j][2]:
            transitions[j][1] += ', ' + le
            ignore.append(transitions[i])    

for i in range(len(transitions)):
    if transitions[i] not in ignore:
        dot.edge(transitions[i][0], transitions[i][2], label=transitions[i][1])

dot.render()