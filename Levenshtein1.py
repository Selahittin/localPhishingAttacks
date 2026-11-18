import pandas as pd
import Levenshtein
from Levenshtein import distance
from difflib import SequenceMatcher

def levenshtein(url):
    def levenshtein_mesafesi(url1, url2):
        return Levenshtein.distance(url1, url2)
    
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
            similarity_levenshtein = levenshtein_mesafesi(url, ourl)
    return similarity_levenshtein



def levenshtein_eslesen(url):
    def levenshtein_mesafesi(url1, url2):
        return Levenshtein.distance(url1, url2)
    
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