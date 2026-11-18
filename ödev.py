from cosine_similarity import calculate_cosine_similarity
from cosine_similarity import calculate_cosine_similarity_eslesen
from USOM import USOM
from sslx import ssl_kontrol
from DOMCTRL import domctrl
import pandas as pd
from Levenshtein1 import levenshtein
from Levenshtein1 import levenshtein_eslesen
from character_similarity import character_similarity_oran
from character_similarity import character_similarity_eslesen
from Selahattin3 import *
import time

fto = float(96.7)  # FREKANS TOPLAM ORANI )%( = 99,59

baslik = ['URL',
          'USOM_da_mevcut_mu',
          'SSL_mevcut_mu',
          'Kosinus_benzerligi_orani',
          'Kosinus_benzerligi_url_bilgisi',
          'Karakter_benzerligi_orani',
          'Karakter_benzerligi_url_bilgisi',
          'Levenshtein_benzerligi_orani',
          'Levenshtein_benzerligi_url_bilgisi',
          'Orijinal_domain_bilgisi',
          'Toplam_nokta_sayisi',
          'Toplam_yatik_cizgi_sayisi',
          'Toplam_cift_yatik_cizgi_sayisi',
          'Toplam_alt_cizgi_sayisi',
          'Toplam_tire_isareti_sayisi',
          'Toplam_esittir_isareti_sayisi',
          'Toplam_kucuktur_isareti_sayisi',
          'Toplam_buyuktur_isareti_sayisi',
          'Toplam_tilde_isareti_sayisi',
          'Toplam_yildiz_isareti_sayisi',
          'Toplam_arti_isareti_sayisi',
          'Toplam_url_uzunlugu_sayisi',
          'Toplam_com_sayisi',
          'Toplam_nokta_com_sayisi',
          'Toplam_unlem_isareti_sayisi',
          'Toplam_sesli_harflerin_sayisi',
          'Toplam_kalin_sesli_harflerin_sayisi',
          'Toplam_ince_sesli_harflerin_sayisi',
          'Toplam_sessiz_harflerin_sayisi',
          'Toplam_sert_unsuz_harflerin_sayisi',
          'Toplam_yumusak_unsuz_harflerin_sayisi',
          'Toplam_urlde_gecen_harflerin_sayisi',
          'Toplam_urlde_gecen_ingilizce_harflerin_sayisi',
          'saldiri_label']
# 'Toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto()',
# 'SONUÇ(GERÇEK/SAHTE)'
# ]

# OUT.xlsx dosyasını okuyarak var olan verileri al
try:
    df_existing = pd.read_excel('OUT.xlsx')
except FileNotFoundError:
    df_existing = pd.DataFrame()

while True:
    secim = input("URL Manuel/Otomatik(dosyadan) kontrol? (M/O) veya çıkmak için q: ")

    if secim.lower() == 'q':
        print("kib by")
        break

    if secim.lower() == 'm':
        url = input("url: ")
        usom_sonuc = USOM(url)
        ssl_sonuc = ssl_kontrol(url)
        cos_similarity_oran_sonuc = calculate_cosine_similarity(url)
        cos_similarity_eslesen_sonuc = calculate_cosine_similarity_eslesen(url)
        character_similarity_oran_sonuc = character_similarity_oran(url)
        character_similarity_eslesen_sonuc = character_similarity_eslesen(url)
        levenshtein_oran_sonuc = levenshtein(url)
        levenshtein_eslesen_sonuc = levenshtein_eslesen(url)
        domctrl_sonuc = domctrl(url)
        toplam_nokta_sayisi_sonuc = toplam_nokta_sayisi(url)
        toplam_yatik_cizgi_sayisi_sonuc = toplam_yatik_cizgi_sayisi(url)
        toplam_cift_yatik_cizgi_sayisi_sonuc = toplam_cift_yatik_cizgi_sayisi(url)
        toplam_alt_cizgi_sayisi_sonuc = toplam_alt_cizgi_sayisi(url)
        toplam_tire_sayisi_sonuc = toplam_tire_sayisi(url)
        toplam_esittir_sayisi_sonuc = toplam_esittir_sayisi(url)
        toplam_kucuktur_sayisi_sonuc = toplam_kucuktur_sayisi(url)
        toplam_buyuktur_sayisi_sonuc = toplam_buyuktur_sayisi(url)
        toplam_tilde_sayisi_sonuc = toplam_tilde_sayisi(url)
        toplam_yildiz_sayisi_sonuc = toplam_yildiz_sayisi(url)
        toplam_arti_sayisi_sonuc = toplam_arti_sayisi(url)
        toplam_url_uzunlugu_sayisi_sonuc = toplam_url_uzunlugu_sayisi(url)
        toplam_com_sayisi_sonuc = toplam_com_sayisi(url)
        toplam_nokta_com_sayisi_sonuc = toplam_nokta_com_sayisi(url)
        toplam_unlem_sayisi_sonuc = toplam_unlem_sayisi(url)
        toplam_sesli_harflerin_sayisi_sonuc = toplam_sesli_harflerin_sayisi(url)
        toplam_kalin_sesli_harflerin_sayisi_sonuc = toplam_kalin_sesli_harflerin_sayisi(url)
        toplam_ince_sesli_harflerin_sayisi_sonuc = toplam_ince_sesli_harflerin_sayisi(url)
        toplam_sessiz_unsuz_sesli_harflerin_sayisi_sonuc = toplam_sessiz_unsuz_sesli_harflerin_sayisi(url)
        toplam_sert_unsuz_sesli_harflerin_sayisi_sonuc = toplam_sert_unsuz_sesli_harflerin_sayisi(url)
        toplam_yumusak_unsuz_sesli_harflerin_sayisi_sonuc = toplam_yumusak_unsuz_sesli_harflerin_sayisi(url)
        toplam_urlde_gecen_harflerin_sayisi_sonuc = toplam_urlde_gecen_harflerin_sayisi(url)
        toplam_urlde_gecen_harflerin_sayisi_ingilizce_sonuc = toplam_urlde_gecen_harflerin_sayisi_ingilizce(url)
        saldiri_label_sonuc = saldiri_label(url)

        # Verileri bir satır olarak oluştur
        row_data = [
            url,
            usom_sonuc,
            ssl_sonuc,
            cos_similarity_oran_sonuc,
            cos_similarity_eslesen_sonuc,
            character_similarity_oran_sonuc,
            character_similarity_eslesen_sonuc,
            levenshtein_oran_sonuc,
            levenshtein_eslesen_sonuc,
            domctrl_sonuc,
            toplam_nokta_sayisi_sonuc,
            toplam_yatik_cizgi_sayisi_sonuc,
            toplam_cift_yatik_cizgi_sayisi_sonuc,
            toplam_alt_cizgi_sayisi_sonuc,
            toplam_tire_sayisi_sonuc,
            toplam_esittir_sayisi_sonuc,
            toplam_kucuktur_sayisi_sonuc,
            toplam_buyuktur_sayisi_sonuc,
            toplam_tilde_sayisi_sonuc,
            toplam_yildiz_sayisi_sonuc,
            toplam_arti_sayisi_sonuc,
            toplam_url_uzunlugu_sayisi_sonuc,
            toplam_com_sayisi_sonuc,
            toplam_nokta_com_sayisi_sonuc,
            toplam_unlem_sayisi_sonuc,
            toplam_sesli_harflerin_sayisi_sonuc,
            toplam_kalin_sesli_harflerin_sayisi_sonuc,
            toplam_ince_sesli_harflerin_sayisi_sonuc,
            toplam_sessiz_unsuz_sesli_harflerin_sayisi_sonuc,
            toplam_sert_unsuz_sesli_harflerin_sayisi_sonuc,
            toplam_yumusak_unsuz_sesli_harflerin_sayisi_sonuc,
            toplam_urlde_gecen_harflerin_sayisi_sonuc,
            toplam_urlde_gecen_harflerin_sayisi_ingilizce_sonuc,
            saldiri_label_sonuc]
        # toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto_sonuc]
        # 'SONUÇ(GERÇEK/SAHTE)']

        # Yeni veriyi DataFrame'e ekle
        df_new = pd.DataFrame([row_data], columns=baslik)
        df_existing = pd.concat([df_existing, df_new], ignore_index=True)

        # Verileri OUT.xlsx dosyasına kaydet
        df_existing.to_excel('OUT.xlsx', index=False)

    elif secim.lower() == 'o':
        excel_dosya = "IN.xlsx"
        sheet = "Sayfa1"
        df = pd.read_excel(excel_dosya, sheet_name=sheet)
        urls = df['URL'].tolist()
        for url in urls:
            usom_sonuc = USOM(url)
            ssl_sonuc = ssl_kontrol(url)
            cos_similarity_oran_sonuc = calculate_cosine_similarity(url)
            cos_similarity_eslesen_sonuc = calculate_cosine_similarity_eslesen(url)
            character_similarity_oran_sonuc = character_similarity_oran(url)
            character_similarity_eslesen_sonuc = character_similarity_eslesen(url)
            levenshtein_oran_sonuc = levenshtein(url)
            levenshtein_eslesen_sonuc = levenshtein_eslesen(url)
            domctrl_sonuc = domctrl(url)
            toplam_nokta_sayisi_sonuc = toplam_nokta_sayisi(url)
            toplam_yatik_cizgi_sayisi_sonuc = toplam_yatik_cizgi_sayisi(url)
            toplam_cift_yatik_cizgi_sayisi_sonuc = toplam_cift_yatik_cizgi_sayisi(url)
            toplam_alt_cizgi_sayisi_sonuc = toplam_alt_cizgi_sayisi(url)
            toplam_tire_sayisi_sonuc = toplam_tire_sayisi(url)
            toplam_esittir_sayisi_sonuc = toplam_esittir_sayisi(url)
            toplam_kucuktur_sayisi_sonuc = toplam_kucuktur_sayisi(url)
            toplam_buyuktur_sayisi_sonuc = toplam_buyuktur_sayisi(url)
            toplam_tilde_sayisi_sonuc = toplam_tilde_sayisi(url)
            toplam_yildiz_sayisi_sonuc = toplam_yildiz_sayisi(url)
            toplam_arti_sayisi_sonuc = toplam_arti_sayisi(url)
            toplam_url_uzunlugu_sayisi_sonuc = toplam_url_uzunlugu_sayisi(url)
            toplam_com_sayisi_sonuc = toplam_com_sayisi(url)
            toplam_nokta_com_sayisi_sonuc = toplam_nokta_com_sayisi(url)
            toplam_unlem_sayisi_sonuc = toplam_unlem_sayisi(url)
            toplam_sesli_harflerin_sayisi_sonuc = toplam_sesli_harflerin_sayisi(url)
            toplam_kalin_sesli_harflerin_sayisi_sonuc = toplam_kalin_sesli_harflerin_sayisi(url)
            toplam_ince_sesli_harflerin_sayisi_sonuc = toplam_ince_sesli_harflerin_sayisi(url)
            toplam_sessiz_unsuz_sesli_harflerin_sayisi_sonuc = toplam_sessiz_unsuz_sesli_harflerin_sayisi(url)
            toplam_sert_unsuz_sesli_harflerin_sayisi_sonuc = toplam_sert_unsuz_sesli_harflerin_sayisi(url)
            toplam_yumusak_unsuz_sesli_harflerin_sayisi_sonuc = toplam_yumusak_unsuz_sesli_harflerin_sayisi(url)
            toplam_urlde_gecen_harflerin_sayisi_sonuc = toplam_urlde_gecen_harflerin_sayisi(url)
            toplam_urlde_gecen_harflerin_sayisi_ingilizce_sonuc = toplam_urlde_gecen_harflerin_sayisi_ingilizce(url)
            saldiri_label_sonuc = saldiri_label(url)

            # Verileri bir satır olarak oluştur
            row_data = [
                url,
                usom_sonuc,
                ssl_sonuc,
                cos_similarity_oran_sonuc,
                cos_similarity_eslesen_sonuc,
                character_similarity_oran_sonuc,
                character_similarity_eslesen_sonuc,
                levenshtein_oran_sonuc,
                levenshtein_eslesen_sonuc,
                domctrl_sonuc,
                toplam_nokta_sayisi_sonuc,
                toplam_yatik_cizgi_sayisi_sonuc,
                toplam_cift_yatik_cizgi_sayisi_sonuc,
                toplam_alt_cizgi_sayisi_sonuc,
                toplam_tire_sayisi_sonuc,
                toplam_esittir_sayisi_sonuc,
                toplam_kucuktur_sayisi_sonuc,
                toplam_buyuktur_sayisi_sonuc,
                toplam_tilde_sayisi_sonuc,
                toplam_yildiz_sayisi_sonuc,
                toplam_arti_sayisi_sonuc,
                toplam_url_uzunlugu_sayisi_sonuc,
                toplam_com_sayisi_sonuc,
                toplam_nokta_com_sayisi_sonuc,
                toplam_unlem_sayisi_sonuc,
                toplam_sesli_harflerin_sayisi_sonuc,
                toplam_kalin_sesli_harflerin_sayisi_sonuc,
                toplam_ince_sesli_harflerin_sayisi_sonuc,
                toplam_sessiz_unsuz_sesli_harflerin_sayisi_sonuc,
                toplam_sert_unsuz_sesli_harflerin_sayisi_sonuc,
                toplam_yumusak_unsuz_sesli_harflerin_sayisi_sonuc,
                toplam_urlde_gecen_harflerin_sayisi_sonuc,
                toplam_urlde_gecen_harflerin_sayisi_ingilizce_sonuc,
                saldiri_label_sonuc]
            # # toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto_sonuc,
            # 'SONUÇ(GERÇEK/SAHTE)']

            # Yeni veriyi DataFrame'e ekle
            df_new = pd.DataFrame([row_data], columns=baslik)
            df_existing = pd.concat([df_existing, df_new], ignore_index=True)

        # Verileri OUT.xlsx dosyasına kaydet
        df_existing.to_excel('OUT.xlsx', index=False)

    else:
        print("Geçersiz seçim! 'M' veya 'O' giriniz. Yada çıkmak için 'q' basınız")
# logongmail.com


""" 1. usom
    2. ssl
    3. cosine_similarity
    4. longest_common_sequence 
    5. Levenshtein
    6. domctrl


    7. toplam_nokta_sayisi
    8. toplam_yatik_cizgi_sayisi
    9. toplam_cift_yatik_cizgi_sayisi
    10. toplam_alt_cizgi_sayisi
    11. toplam_tire_sayisi
    12. toplam_esittir_sayisi
    13. toplam_kucuktur_sayisi
    14. toplam_buyuktur_sayisi
    15. toplam_tilde_sayisi
    16. toplam_yildiz_sayisi
    17. toplam_arti_sayisi
    18. 
    19. toplam_com_sayisi
    20. toplam_nokta_com_sayisi
    21. toplam_unlem_sayisi
    22. toplam_sesli_harflerin_sayisi
    23. toplam_kalin_sesli_harflerin_sayisi
    24. toplam_ince_sesli_harflerin_sayisi
    25. toplam_sessiz_unsuz_sesli_harflerin_sayisi
    26. toplam_sert_unsuz_sesli_harflerin_sayisi
    27. toplam_yumusak_unsuz_sesli_harflerin_sayisi
    28. toplam_urlde_gecen_harflerin_sayisi

"""

""""
TODO :
1. USOM(VAR/YOK) (yazıldı entegrasyon gerekli)
2. SSL(VAR/YOK) +(yazıldı entegrasyon gerekli)
3. COS SIMILARITY ORANI (yazıldı entegrasyon gerekli)
4. ORG.DOM.KONTROL (yazıldı. hata giderilip entegre edilecek)



Analiz:

1. Satırdaki URL USOM'da var mı kontrol edilir. 
   USOM'da varsa ZARARLI olarak OUT.xlsx log dosyasına yaz. [gelen satır + ZARARLI]
   Zararlı olmayan satır için 2. adıma git.

2. SSL kontrolü yap. 
   SSL yoksa SSL sütununa "YOK" yaz. 
   SSL varsa SSL sütununa "VAR" yaz.

3. COS SIMILARITY ORANI
   Girilen URL ile zararsız URL listesindeki url'ler ile en yakın olanı bulunur ve oranı yazılır.

4. ORG.DOM.KONTROL ile 

hsbc-onlines.com
http://www.hsbc.com.tr
http://basvuru.hsbc.com.tr


Girilen bir adresle aşağıdaki URL formatlarıyla uyumlu 
Domain adresinde 1 nokta varsa : https://hsbc.com
Domain adresinde 2 nokta varsa : https://www.hsbc.com      
Domain adresinde 3 nokta varsa : https://www.hsbc.com.tr 



"""
