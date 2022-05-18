from matplotlib import style
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Frame, Label, ttk
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
print(expresionRegular)
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8,9])
G.add_edges_from([(1, 2),(1,3),(3,3),(2,4),(2,5),(5,2),(4,6),(4,7),(6,7),(5,8),(8,7),(7,7),(5,9),(9,9)])
G.add_edges_from([(6,4),(8,5)])
pos = nx.spring_layout(G)
plt.figure()
opt = { 'node_color': 'green',
        'with_labels': True }
nx.draw(
    G, pos, edge_color='black', width=1, linewidths=1,
    node_size=300, node_color='white', alpha=0.9,
    labels={node: node for node in G.nodes()}
)
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
                 (8, 5): 'B'},
    font_color='black'
)
plt.axis('off')
plt.show()

