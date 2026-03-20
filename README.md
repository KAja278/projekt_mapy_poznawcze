# Analiza map poznawczych

Program w Pythonie do analizy map poznawczych w sytuacjach zagrożenia. Na podstawie wprowadzonych połączeń między elementami mapy generuje graf i oblicza entropię Shannona, umożliwiając ocenę złożoności struktury poznawczej.

## Technologie

Python, NetworkX, NumPy, Pandas

## Uruchomienie

```bash
git clone https://github.com/twoj-user/cognitive-maps-analyzer.git
cd cognitive-maps-analyzer
python main.py
```

## Funkcje

* wprowadzanie relacji między elementami mapy poznawczej
* generowanie grafów na podstawie danych
* klasyfikacja wierzchołków (klasy równoważności)
* obliczanie entropii Shannona
* eksport wyników do pliku CSV

## Opis działania

Mapy poznawcze są reprezentowane jako grafy, w których wierzchołki odpowiadają pojęciom, a krawędzie relacjom między nimi. Na tej podstawie obliczana jest entropia Shannona, będąca miarą ilości informacji strukturalnej w grafie.
