import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def rysuj_graf(G, klasy, nazwa_pliku):
    """Rysowanie grafu i zapisywanie go do pliku."""
    pos = nx.spring_layout(G)
    colors = plt.cm.rainbow(np.linspace(0, 1, len(klasy)))
    
    for index, klasa in enumerate(klasy):
        nx.draw_networkx_nodes(G, pos, nodelist=klasa, node_color=[colors[index]], label=f"Klasa {index+1}")
    
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.savefig(nazwa_pliku)
    plt.close()