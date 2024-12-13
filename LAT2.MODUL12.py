import pandas as pd

# Membaca file CSV
file_path = 'Negara - Negara.csv'  
df = pd.read_csv(file_path)

# Menghapus baris dengan nilai NaN di kolom 'Benua'
df = df.dropna(subset=['Benua'])

# Menghitung rata-rata dan standar deviasi berdasarkan benua
mean_by_continent = df.groupby('Benua')[['Luas', 'Populasi']].mean()
std_by_continent = df.groupby('Benua')[['Luas', 'Populasi']].std()

# Menulis hasil ke file CSV
mean_by_continent.to_csv('NegaraMean.csv')
std_by_continent.to_csv('NegaraStandarDeviasi.csv')

print("File CSV telah dibuat: NegaraMean.csv dan NegaraStandarDeviasi.csv")
