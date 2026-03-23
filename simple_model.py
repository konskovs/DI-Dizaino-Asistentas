import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from database import session, ColorPalette

# 1. Uzsikrauname duomenis is musu SQLite bazes i Pandas lentele
def load_data():
    query = session.query(ColorPalette).statement
    df = pd.read_sql(query, session.bind)
    return df

# 2. Paprastas modelis: KNN (K-Nearest Neighbors)
def train_simple_model(df, input_emotion):
    # Paverciame tekstine emocija i skaicius (Label Encoding paprastumui)
    # Siame etape tiesiog filtruojame, bet KNN principas - rasti artimiausia atitikmeni
    
    # Sukuriame modeli (k=1 reiskia ieskome 1 artimiausio kaimyno)
    model = KNeighborsClassifier(n_neighbors=1)
    
    # Paruosiame duomenis: X yra emocija (skaiciais), y yra paletes ID
    # Kadangi musu duomenys mazi, naudojame paprasta atitikmeni
    # Veliau, kai turesime daugiau duomenu, naudosime sudetingesnius pozymius
    
    target_palette = df[df['emotion'] == input_emotion]
    
    if not target_palette.empty:
        res = target_palette.iloc[0]
        return f"Rasta palete emocijai '{input_emotion}': {res.hex_1}, {res.hex_2}, {res.hex_3}"
    else:
        return "Deja, tokios emocijos musu DB dar nera."

# Testuojame
if __name__ == "__main__":
    data = load_data()
    print(train_simple_model(data, 'Luxury'))
    print(train_simple_model(data, 'Playful'))