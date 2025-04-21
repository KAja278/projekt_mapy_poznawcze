import os
import pandas as pd
import networkx as nx
from mapy.izomorfizm import ekstrakcja_kul_wierzcholkowych, sprawdz_izomorfizm
from mapy.entropia import oblicz_entropie_shannona
from mapy.rysowanie import rysuj_graf
from datetime import datetime

def main():
    # Ustaw ścieżki do folderów wyników
    wyniki_folder = 'wyniki'
    grafy_folder = os.path.join(wyniki_folder, 'grafy')
    wyniki_path = os.path.join(wyniki_folder, 'wyniki.csv')

    # Utwórz foldery na wyniki, jeśli nie istnieją
    os.makedirs(grafy_folder, exist_ok=True)

    # Sprawdzenie, czy istnieje już plik z wynikami i jego wczytanie
    if os.path.exists(wyniki_path):
        df = pd.read_csv(wyniki_path)
    else:
        df = pd.DataFrame(columns=['Nazwa', 'Liczba wierzchołków', 'Liczba klas równoważności', 'Entropia Shannona', 'Płeć', 'Kierunek'])

    while True:
        liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków: "))
        liczba_polaczen = int(input("Podaj liczbę połączeń: "))
        plec = input("Podaj płeć (k/m): ")
        kierunek = input("Podaj kierunek (h/s): ")
        nr_ankiety = input("Podaj numer ankiety: ")

        krawedzie = []
        for i in range(liczba_polaczen):
            a, b = map(int, input(f"Podaj połączenie {i+1} (wierzchołek1 wierzchołek2): ").split())
            krawedzie.append((a, b))
        
        G = nx.Graph()
        G.add_edges_from(krawedzie)
        
        kule = ekstrakcja_kul_wierzcholkowych(G)
        klasy = sprawdz_izomorfizm(kule)
        
        entropia_shannona = oblicz_entropie_shannona(klasy)

        print(f"Liczba wierzchołków: {liczba_wierzcholkow}")
        print(f"Liczba klas równoważności: {len(klasy)}")
        print(f"Entropia Shannona: {entropia_shannona}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nazwa_pliku = os.path.join(grafy_folder, f'graf_{G.number_of_nodes()}_{plec}_{kierunek}_{timestamp}.jpg')
        rysuj_graf(G, klasy, nazwa_pliku)

        new_row = pd.DataFrame({
            'Nazwa': [timestamp],
            'Liczba wierzchołków': [G.number_of_nodes()],
            'Liczba klas równoważności': [len(klasy)],
            'Entropia Shannona': [entropia_shannona],
            'Płeć': [plec],
            'Kierunek': [kierunek],
            'nr.ankiety' : [nr_ankiety]
        })

        df = pd.concat([df, new_row], ignore_index=True)
        
        kontynuuj = input("Czy chcesz wprowadzić kolejny graf? (tak/nie): ").lower()
        if kontynuuj != 'tak':
            break

    df.to_csv(wyniki_path, index=False)

if __name__ == "__main__":
    main()