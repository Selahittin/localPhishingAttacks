import requests

def ssl_kontrol(url):
    modified_url = "https://www." + url
    try:
        response = requests.get(modified_url)  # SSL sertifikasının doğruluğunu kontrol edin
        if response.text:
            if 'Strict-Transport-Security' in response.headers:
                ssl = True
                # print(f"SSL sertifikası geçerli: {response.headers['Strict-Transport-Security']}")
                # print(ssl)
                return 1
            else:
                ssl = False
                # print("SSL sertifikası geçersiz.")
                # print(ssl)
                return 0
            pass
            return 1
        else:
            print("response yok")
            return 0
    except requests.exceptions.ConnectionError as e:
        # print("Bağlantı hatası:", e)
        return 0
    except requests.exceptions.RequestException as e:
        # print("İstek hatası:", e)
        pass
        return 0


# url = "http://example.com"
#
# if url.startswith("http://") or url.startswith("https://"):
#     domain = url.split("://")[1]
#     ssl_result = ssl_kontrol(url)
#     print("SSL özelliği:", ssl_result)
# else:
#     print("kurallar")
