from asyncio.windows_events import NULL
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
def close_window():
    root.destroy()
root = tk.Tk()
root.config(width=300, height=200)
mi_Label = ttk.Label(text="Ingrese su expresion regular")
mi_Label.place(x=50,y=25)
entry_var = tk.StringVar()
entry = ttk.Entry(textvariable=entry_var)
entry.place(x=50, y=50)
button = ttk.Button(text="Obtener expresion",command = close_window)
button.place(x=50, y=100)
root.mainloop()
expresionRegular=entry_var.get()
expresionRegular=expresionRegular.lower()
comprobador=list(expresionRegular)
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8,9])
G.add_edges_from([(1, 2),(1,3),(3,3),(2,4),(2,5),(4,6),(4,7),(6,7),(5,8),(8,7),(7,7),(5,9),(9,9)])
G.add_edges_from([(6,4),(8,5)])
pos = nx.circular_layout(G)
plt.figure()
nx.draw(
    G, pos=pos, edge_color='black', width=1, linewidths=1,
    node_size=300, node_color='red', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
nx.draw(G.subgraph([2,6,8]), pos=pos, node_color="green")
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={(1, 2): 'A', 
                 (1, 3): 'B',
                 (3, 3): 'AB',
                 (2, 4): 'A',
                 (2, 5): 'B',
                 (5, 9): 'B',
                 (4, 6): 'A',
                 (6, 4): 'A',
                 (4, 7): 'B',
                 (6, 7): 'B',
                 (5, 8): 'A',
                 (8, 7): 'A',
                 (7, 7): 'A',                                                                                                                                                                                            
                 (8, 5): 'B,A'},
    font_color='black'
)
bandera=True
if comprobador==[]:
    nx.draw(G.subgraph(1),pos=pos,node_color="blue")
elif comprobador[0]=='a':
    nx.draw(G.subgraph(1),pos=pos,node_color="blue")
    nx.draw(G.subgraph(2),pos=pos,node_color="purple")
    if comprobador[1]=='a':
        nx.draw(G.subgraph([2,4]),pos=pos,node_color="blue")
        if comprobador[2]=='a':
            nx.draw(G.subgraph(6),pos=pos,node_color="purple")
            if comprobador[3]=='b':
                nx.draw(G.subgraph(6),pos=pos,node_color="blue")
                nx.draw(G.subgraph(7),pos=pos,node_color="gray")
                bandera=False
    elif comprobador[1]=='b':
        nx.draw(G.subgraph(5),pos=pos,node_color="blue")
        if comprobador[2]=='a':
            nx.draw(G.subgraph(8),pos=pos,node_color="purple")
            if comprobador[3]=='a':
                nx.draw(G.subgraph(8),pos=pos,node_color="blue")
                nx.draw(G.subgraph(7),pos=pos,node_color="gray")
                bandera=False
        elif comprobador[2]=='b':
            nx.draw(G.subgraph(9),pos=pos,node_color="gray")
elif comprobador[0]=='b':
    nx.draw(G.subgraph(1),pos=pos,node_color="blue")
    nx.draw(G.subgraph(3),pos=pos,node_color="gray")
    bandera=False
plt.axis('off')
plt.show()
