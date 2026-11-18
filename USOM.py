import requests
import time

def USOM(url):
    global data
    try:
        # time.sleep(2)
        url2 = f"https://www.usom.gov.tr/api/address/index?q={url}&type=domain"
        while True:
            response = requests.get(url2, timeout=30)
            if response.status_code == 429:
                time.sleep(3)
                print(url, response.status_code)
                continue
            if response.status_code == 200:
                data = response.json().get("models", [])
                print(url, " yazıldı.")
                break
            else:
                print("USOM API request hata verdi :", response.status_code)
                response.raise_for_status()


        # print(data)
        for item in data:
            if item["url"] == url:
                # print(item["url"])
                return 1
        return 0

    except requests.exceptions.RequestException as e:
        print("İstek hatası:", e)
        return 0
        pass

    except ReadTimeoutError as e:
        print("Timeout hatası:", e)
        return 0
        pass  