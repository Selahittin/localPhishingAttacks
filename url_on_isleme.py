import pandas as pd
import time

def remove_prefix(url):
    prefixes = ["https://www.", "http://www.", "http://", "https://", "www."]
    for prefix in prefixes:
        if url.startswith(prefix):
            return url[len(prefix):]
    return url

input_excel_filename = "dosya_1.xlsx"  # Giriş Excel dosyasının adı
output_excel_filename = "dosya_2.xlsx"  # Çıkış Excel dosyasının adı

try:
    # Başlangıç zamanını al (ms cinsinden)
    start_time = time.time() * 1000 
    
    df = pd.read_excel(input_excel_filename)  # Giriş Excel dosyasını oku
    
    # Excel dosyasındaki satır sayısını bul
    data_count = len(df)
    
    df['ZARARSIZ URL'] = df['ZARARSIZ URL'].apply(remove_prefix)  # URL'leri düzenle
    
    # Düzenlenmiş verileri yeni bir Excel dosyasına yaz
    df.to_excel(output_excel_filename, index=False)
    
    # Bitiş zamanını al (ms cinsinden)
    end_time = time.time() * 1000  

    # Çalışma süresi hesapla
    elapsed_time = end_time - start_time  
    
    # Ortalama süreyi hesapla (ms/veri)
    avg_time_per_data = elapsed_time / data_count if data_count > 0 else 0
    
    print("İşlem tamamlandı. Sonuçlar", output_excel_filename, "dosyasına yazıldı.")
    print("Giriş Excel dosyasındaki veri sayısı:", data_count)
    print(f"Çalışma süresi: {elapsed_time:.2f} ms")
    print(f"Bir veri için ortalama süre: {avg_time_per_data:.4f} ms")
    
except FileNotFoundError:
    print("Giriş Excel dosyası bulunamadı.")
except Exception as e:
    print("Bir hata oluştu:", e)
