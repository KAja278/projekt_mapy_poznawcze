import networkx as nx
from networkx.algorithms.isomorphism import GraphMatcher

def ekstrakcja_kul_wierzcholkowych(graf):
    """Ekstrakcja kul wierzchołkowych z grafu."""
    kule = {}
    for wierzcholek in graf.nodes():
        podgraf = nx.ego_graph(graf, wierzcholek, radius=1)
        kule[wierzcholek] = podgraf
    return kule

def sprawdz_izomorfizm(kule):
    """Sprawdzanie izomorfizmu między kulami wierzchołkowymi."""
    izomorficzne_klasy = []
    odwiedzone = set()
    
    for w1, k1 in kule.items():
        if w1 in odwiedzone:
            continue
        klasa = [w1]
        odwiedzone.add(w1)
        
        for w2, k2 in kule.items():
            if w2 in odwiedzone:
                continue
            matcher = GraphMatcher(k1, k2)
            if matcher.is_isomorphic():
                klasa.append(w2)
                odwiedzone.add(w2)
        
        izomorficzne_klasy.append(klasa)
    
    return izomorficzne_klasy