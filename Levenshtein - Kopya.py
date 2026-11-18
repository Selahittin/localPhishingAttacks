import pandas as pd
from difflib import SequenceMatcher

# Karakter bazlı benzerlik hesapla
def character_similarity(url1, url2):
    similarity = SequenceMatcher(None, url1, url2).ratio()
    return similarity

# Excel dosyasını oku
df = pd.read_excel('ZARARSIZ-URL.xlsx')
url_list = df['ZARARSIZ URL'].tolist()

while True:
    input_url = input("URL girin ('q' ile çıkış yapın): ")

    if input_url == 'q':
        break

    # En benzer URL ve benzerlik skoru için varsayılan değerleri ayarla
    most_similar_url = None
    similarity_score = 0

    # URL listesini dolaşarak en benzer URL ve benzerlik skorunu bul
    for url in url_list:
        similarity = character_similarity(input_url, url)
        if similarity > similarity_score:
            similarity_score = similarity
            most_similar_url = url

    # Sonuçları göster
    print("Girdi URL: ", input_url)
    print("En benzer URL: ", most_similar_url)
    print("Benzerlik oranı: ", similarity_score)
    print("-------------------------")

