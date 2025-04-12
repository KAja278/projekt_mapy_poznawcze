import numpy as np

def oblicz_entropie_shannona(klasy):
    """Obliczanie entropii Shannona na podstawie klas izomorficznych."""
    liczba_wierzcholkow = sum(len(klasa) for klasa in klasy)
    prawdopodobienstwa = [len(klasa) / liczba_wierzcholkow for klasa in klasy]
    entropia_shannona = -sum(p * np.log2(p) for p in prawdopodobienstwa if p > 0)
    return entropia_shannona