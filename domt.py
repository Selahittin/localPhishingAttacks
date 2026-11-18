import pandas as pd
import tldextract

# Excel dosyasını okuyun
df = pd.read_excel(r"ZARARSIZ-URL.xlsx", sheet_name="Sheet1")
print(df.head())

while True:
    url = input("URL'yi girin ('q' yazarak çıkabilirsiniz): ")
    if url.lower() == "q":
        break

    is_safe = False

    # URL'yi alt alan adıyla birlikte ayırın
    subdomain, domain, suffix = tldextract.extract(url)
    combined_url = f"{domain}.{suffix}"  # Domain ve suffix değerlerini birleştir

    # Her satırı kontrol edin
    for index, row in df.iterrows():
        row_url = row["ZARARSIZ URL"]

        # Excel'deki URL'yi alt alan adıyla birlikte ayırın
        row_subdomain, row_domain, row_suffix = tldextract.extract(row_url)
        row_combined_url = f"{row_domain}.{row_suffix}"  # Domain ve suffix değerlerini birleştir

        # URL kontrolü yapın
        if combined_url == row_combined_url:
            is_safe = True
            break

    if is_safe:
        print("ZARARSIZ")
    else:
        print("ZARARLI OLABİLİR")



    # D:\Masaüstü\PYTHON SCR\Selahattin\ÖDEV\ZARARSIZ-URL.xlsx
