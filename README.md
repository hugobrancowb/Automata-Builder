# automata-builder
Program that reads a text file that represents an automata and builds a graphical representation using Graphviz.

* Input format
The automata must match the format proposed by Prof. Dr. Ruben Carlo Benante <rcb@upe.br>, as shown below:

```
    #K
    3
    #A
    b
    #S
    0
    #F
    1
    #D
    0 a 1
    0 b 2
    1 a 1
    1 b 1
    2 a 1
    2 b 2
```

Where K represents the number of places, A represents the "biggest" letter from the alfabet, S represents the initial state, F represents the final place or places of the automata (in case of more than one state, they must be separated by single spaces) and D represents the transitions.

* How to run the code

To run the code you'll need to have installed in your system the following packages:
` python3 python3-pygraphviz `

and run the command in terminal:

    $ python3 automata-builder.py 