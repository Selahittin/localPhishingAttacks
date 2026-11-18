import nltk
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from collections import Counter
import re
import math
from difflib import SequenceMatcher


def calculate_cosine_similarity(url):
    def get_word_frequencies(text):
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        words = re.findall(r'\w+', text)
        return Counter(words)

    def cosine_similarity(vec1, vec2):
        dot_product = sum(vec1[word] * vec2[word] for word in vec1 if word in vec2)
        norm1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
        norm2 = math.sqrt(sum(value ** 2 for value in vec2.values()))
        return dot_product / (norm1 * norm2)

    def calculate_cosine_similarity(text1, text2):
        freq1 = get_word_frequencies(text1)
        freq2 = get_word_frequencies(text2)
        
        similarity = cosine_similarity(freq1, freq2)
        return similarity
        
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
            similarity_cosine = calculate_cosine_similarity(url, ourl)
    return similarity_cosine


def calculate_cosine_similarity_eslesen(url):
    def get_word_frequencies(text):
        text = re.sub(r'\s+', ' ', text)
        text = text.lower()
        words = re.findall(r'\w+', text)
        return Counter(words)

    def cosine_similarity(vec1, vec2):
        dot_product = sum(vec1[word] * vec2[word] for word in vec1 if word in vec2)
        norm1 = math.sqrt(sum(value ** 2 for value in vec1.values()))
        norm2 = math.sqrt(sum(value ** 2 for value in vec2.values()))
        return dot_product / (norm1 * norm2)

    def calculate_cosine_similarity(text1, text2):
        freq1 = get_word_frequencies(text1)
        freq2 = get_word_frequencies(text2)
        
        similarity = cosine_similarity(freq1, freq2)
        return similarity
        
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
