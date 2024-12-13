import pandas as pd

file_path = 'Negara - Negara.csv'  
df = pd.read_csv(file_path)

df = df.dropna(subset=['Benua'])

print("Data Frame:")
print(df)

mean_by_continent = df.groupby('Benua')[['Luas', 'Populasi']].mean()

std_by_continent = df.groupby('Benua')[['Luas', 'Populasi']].std()

print("\nRata-rata berdasarkan Benua:")
print(mean_by_continent)

print("\nStandar Deviasi berdasarkan Benua:")
print(std_by_continent)
