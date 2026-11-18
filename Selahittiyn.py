import sys

import pandas as pd
from difflib import SequenceMatcher
import Levenshtein

def character_similarity(url1, url2):
    similarity = SequenceMatcher(None, url1, url2).ratio()
    return similarity

def calculate_levenshtein_distance(url1, url2):
    distance = Levenshtein.distance(url1, url2)
    return distance

# Excel dosyasını oku
df = pd.read_excel('ZARARSIZ-URL.xlsx')
url_list = df['ZARARSIZ URL'].tolist()

while True:
    input_url = input("URL girin ('q' ile çıkış yapın): ")

    if input_url == 'q':
        sys.exit()
        break

    # En benzer URL ve benzerlik skoru için varsayılan değerleri ayarla
    most_similar_url = None
    similarity_score_LCS = 0
    similarity_levenshtein = 0

    # URL listesini dolaşarak en benzer URL ve benzerlik skorunu bul
    for url in url_list:
        similarity = character_similarity(input_url, url)
        distance = calculate_levenshtein_distance(input_url, url)
        if distance > similarity_levenshtein:
            similarity_levenshtein = distance
        if similarity > similarity_score_LCS:
            similarity_score_LCS = similarity
            most_similar_url = url


    # Sonuçları göster
    print("Girdi URL: ", input_url)
    print("En benzer URL: ", most_similar_url)
    print("Levenshtein Benzerlik oranı: ", similarity_levenshtein)
    print("LCS Benzerlik oranı: ", similarity_score_LCS)
    print("-------------------------")

    # # Sonuçları göster
    # print("Girdi URL: ", input_url)
    # print("En benzer URL: ", most_similar_url)
    # print("Benzerlik oranı: ", similarity_score)
    # print("-------------------------")