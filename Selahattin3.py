from USOM import USOM

# 'Toplam_nokta_sayisi',
# 'Toplam_yatik_cizgi_sayisi',
# 'Toplam_cift_yatik_cizgi_sayisi',
# 'Toplam_alt_cizgi_sayisi',
# 'Toplam_tire_sayisi',
# 'Toplam_esittir_sayisi',
# 'Toplam_kucuktur_sayisi',
# 'Toplam_buyuktur_sayisi()',
# 'Toplam_tilde_sayisi()',
# 'Toplam_yildiz_sayisi()',
# 'Toplam_arti_sayisi()',
# 'Toplam_url_uzunlugu_sayisi()',
# 'Toplam_com_sayisi()',
# 'Toplam_nokta_com_sayisi()',
# 'Toplam_unlem_sayisi()',
# 'Toplam_sesli_harflerin_sayisi()',
# 'Toplam_kalin_sesli_harflerin_sayisi()',
# 'Toplam_ince_sesli_harflerin_sayisi()',
# 'Toplam_sessiz_unsuz_sesli_harflerin_sayisi()',
# 'Toplam_sert_unsuz_sesli_harflerin_sayisi()',
# 'Toplam_yumusak_unsuz_sesli_harflerin_sayisi()',
# 'Toplam_urlde_gecen_harflerin_sayisi()',
# 'Toplam_urlde_gecen_harflerin_sayisi_ingilizce()',
# 'Toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto()',
# 'SONUÇ(GERÇEK/SAHTE)',


def toplam_nokta_sayisi(url):
    deger = url.__str__().count('.')
    sonuc = deger
    return sonuc


def toplam_yatik_cizgi_sayisi(url):
    deger = url.__str__().count('/')
    sonuc = deger
    return sonuc


def toplam_cift_yatik_cizgi_sayisi(url):
    deger = url.__str__().count('//')
    sonuc = deger
    return sonuc


def toplam_alt_cizgi_sayisi(url):
    deger = url.__str__().count('_')
    sonuc = deger
    return sonuc


def toplam_tire_sayisi(url):
    deger = url.__str__().count('-')
    sonuc = deger
    return sonuc


def toplam_esittir_sayisi(url):
    deger = url.__str__().count('=')
    sonuc = deger
    return sonuc


def toplam_kucuktur_sayisi(url):
    deger = url.__str__().count('<')
    sonuc = deger
    return sonuc


def toplam_buyuktur_sayisi(url):
    deger = url.__str__().count('>')
    sonuc = deger
    return sonuc


def toplam_tilde_sayisi(url):
    deger = url.__str__().count('~')
    sonuc = deger
    return sonuc


def toplam_yildiz_sayisi(url):
    deger = url.__str__().count('*')
    sonuc = deger
    return sonuc


def toplam_arti_sayisi(url):
    deger = url.__str__().count('+')
    sonuc = deger
    return sonuc


def toplam_url_uzunlugu_sayisi(url):
    deger = len(str(url))
    sonuc = deger
    return sonuc


def toplam_com_sayisi(url):
    deger = url.__str__().count('com')
    sonuc = deger
    return sonuc


def toplam_nokta_com_sayisi(url):
    deger = url.__str__().count('.com')
    sonuc = deger
    return sonuc


def toplam_unlem_sayisi(url):
    deger = url.__str__().count('!')
    sonuc = deger
    return sonuc


def toplam_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'aeıioöuü'
    print(url)
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_kalin_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'aıou'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_ince_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'eiöü'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_sessiz_unsuz_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'bcçdfgğhjklmnprsştvyz'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_sert_unsuz_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'çfhkpsşt'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_yumusak_unsuz_sesli_harflerin_sayisi(url):
    global toplam
    alfabe = 'bcdgğjlmnrvyz'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_urlde_gecen_harflerin_sayisi(url):
    global toplam
    alfabe = 'AaBbCcÇçDdEeFfGgĞğHhİiIıJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def toplam_urlde_gecen_harflerin_sayisi_ingilizce(url):
    global toplam
    alfabe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    toplam = 0
    for harf in alfabe:
        toplam = (toplam + url.__str__().count(harf))
    deger = toplam
    sonuc = deger
    return sonuc


def saldiri_label(url):
    if USOM(url) == True:
        return 1
    else:
        return 0



# def toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto(url):
#     global toplam
#     toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto_degeri = sutun[22] / fto
#     sutun.append(format(toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto_degeri, " 111.2f"))
#     print(format(toplam_urlde_gecen_harflerin_sayisi_ingilizce_bolu_fto_degeri, " 111.2f"))
#     # print(sutun)
