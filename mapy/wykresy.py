import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    df = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
    df.columns = df.columns.str.strip()
    return df

def analiza_wykresy(df, folder='wyniki/wykresy'):
    os.makedirs(folder, exist_ok=True)


    kolumny = ['Liczba klas równoważności','Entropia Shannona','Płeć']

    for kolumna in kolumny:
        print (f"{kolumna}")
        if kolumna not in df.columns:
            raise ValueError(f"Brakuje kolumny: {kolumna}")

    # histogram liczby klas równoważności
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='Liczba klas równoważności')
    plt.title('Rozkład liczby klas równoważności')
    plt.xlabel('Liczba klas')
    plt.ylabel('Liczba przypadków')
    plt.tight_layout()
    plt.savefig(os.path.join(folder, 'klasy_rownowaznosci.png'))
    plt.close()

    # rozklad entropii Shannona
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x='Entropia Shannona', kde=True, bins=10)
    plt.title('Rozkład entropii Shannona')
    plt.xlabel('Entropia Shannona')
    plt.tight_layout()
    plt.savefig(os.path.join(folder, 'entropia_histogram.png'))
    plt.close()

    # etropia i plec
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x='Płeć', y='Entropia Shannona')
    plt.title('Entropia Shannona wg płci')
    plt.tight_layout()
    plt.savefig(os.path.join(folder, 'entropia_plec.png'))
    plt.close()


if __name__ == "__main__":
 
    file_path = "wyniki/wyniki.csv"

    df = load_data(file_path)

    analiza_wykresy(df)
