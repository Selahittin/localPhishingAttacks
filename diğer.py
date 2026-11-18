"""
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


def toplam_nokta_sayisi():
    print("satırdaki toplam nokta sayısı : ")
    deger = line.__str__().count('.')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)

    # print(type(sonuc))
    # print(','.join(str(x) for x in sonuc))


def toplam_yatik_cizgi_sayisi():
    print("\nsatırdaki / sayısı : ")
    deger = line.__str__().count('/')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_cift_yatik_cizgi_sayisi():
    print("\nsatırdaki // sayısı : ")
    deger = line.__str__().count('//')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_alt_cizgi_sayisi():
    print("\nsatırdaki _ sayısı : ")
    deger = line.__str__().count('_')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_tire_sayisi():
    print("\nsatırdaki - sayısı : ")
    deger = line.__str__().count('-')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_esittir_sayisi():
    print("\nsatırdaki = sayısı : ")
    deger = line.__str__().count('=')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_kucuktur_sayisi():
    print("\nsatırdaki < sayısı : ")
    deger = line.__str__().count('<')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_buyuktur_sayisi():
    print("\nsatırdaki > sayısı : ")
    deger = line.__str__().count('>')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_tilde_sayisi():
    print("\nsatırdaki ~ sayısı : ")
    deger = line.__str__().count('~')
    sutun.append(deger)
    sonuc = (line, deger)
    print(str(sonuc))
    # print(sutun)


def toplam_yildiz_sayisi():
    print("\nsatırdaki * sayısı : ")
    deger = line.__str__().count('*')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_arti_sayisi():
    print("\nsatırdaki + sayısı : ")
    deger = line.__str__().count('+')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_com_sayisi():
    print("\nsatırdaki com sayısı : ")
    deger = line.__str__().count('com')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_nokta_com_sayisi():
    print("\nsatırdaki .com sayısı : ")
    deger = line.__str__().count('.com')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_unlem_sayisi():
    print("\nsatırdaki ! sayısı : ")
    deger = line.__str__().count('!')
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki sesli harflerin toplam sayısı : ")
    alfabe = 'aeıioöuü'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_kalin_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki kalın sesli harflerin toplam sayısı : ")
    alfabe = 'aıou'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_ince_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki ince sesli harflerin toplam sayısı : ")
    alfabe = 'eiöü'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_sessiz_unsuz_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki sessiz(ünsüz) harflerin toplam sayısı : ")
    alfabe = 'bcçdfgğhjklmnprsştvyz'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_sert_unsuz_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki sert(ünsüz) harflerin toplam sayısı : ")
    alfabe = 'çfhkpsşt'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_yumusak_unsuz_sesli_harflerin_sayisi():
    global toplam
    print("\nsatırdaki yumuşak(ünsüz) harflerin toplam sayısı : ")
    alfabe = 'bcdgğjlmnrvyz'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)


def toplam_urlde_gecen_harflerin_sayisi():
    global toplam
    print("\nurl'deki harflerin toplam sayısı : ")
    alfabe = 'AaBbCdÇçDdEeFfGgĞğHhİiIıJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz'
    print(line)
    toplam = 0
    for harf in alfabe:
        if line.__str__().count(harf) != 0:
            print(harf, line.__str__().count(harf))
        toplam = (toplam + line.__str__().count(harf))
    print('Toplam : ', toplam, '\n')
    deger = toplam
    sutun.append(deger)
    sonuc = (line, deger)
    print(sonuc)
    # print(sutun)

