import pandas as pd
from difflib import SequenceMatcher

# Karakter bazlı benzerlik hesapla
def character_similarity_oran(url):
    def character_similarity(url1, url2):
        similarity = SequenceMatcher(None, url1, url2).ratio()
        return similarity

    df = pd.read_excel('ZARARSIZ-URL.xlsx')
    url_list = df['ZARARSIZ URL'].tolist()

    most_similar_url = None
    similarity_score = 0

    # URL listesini dolaşarak en benzer URL ve benzerlik skorunu bul
    for ourl in url_list:
        similarity = character_similarity(url, ourl)
        if similarity > similarity_score:
            similarity_score = similarity
            most_similar_url = ourl
    return similarity_score

    # # Sonuçları göster
    # print("Girdi URL: ", input_url)
    # print("En benzer URL: ", most_similar_url)
    # print("Benzerlik oranı: ", similarity_score)
    # print("-------------------------")
    #
    #

def character_similarity_eslesen(url):
    def character_similarity(url1, url2):
        similarity = SequenceMatcher(None, url1, url2).ratio()
        return similarity

    df = pd.read_excel('ZARARSIZ-URL.xlsx')
    url_list = df['ZARARSIZ URL'].tolist()

    most_similar_url = None
    similarity_score = 0

    # URL listesini dolaşarak en benzer URL ve benzerlik skorunu bul
    for ourl in url_list:
        similarity = character_similarity(url, ourl)
        if similarity > similarity_score:
            similarity_score = similarity
            most_similar_url = ourl
    return most_similar_url