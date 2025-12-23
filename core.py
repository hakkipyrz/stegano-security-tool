import cv2
import numpy as np

import cv2
import numpy as np

def veri_binary_cevir(veri):
    """
    Veriyi bilgisayarın dili olan 0 ve 1'lere (Binary) çevirir.
    Hoca Sorarsa: "Steganografi bit seviyesinde yapıldığı için veriyi önce binary formata dönüştürmem şart."
    """
    if isinstance(veri, str):
        return ''.join([format(b, "08b") for b in veri.encode('utf-8')])
    elif isinstance(veri, bytes) or isinstance(veri, np.ndarray):
        return [format(i, "08b") for i in veri]
    elif isinstance(veri, int) or isinstance(veri, np.uint8):
        return format(veri, "08b")
    else:
        raise TypeError("Girdi tipi desteklenmiyor.")


def veri_gizle(resim, gizli_mesaj):
    gizli_mesaj += "==SON=="

    binary_veri = veri_binary_cevir(gizli_mesaj)
    veri_uzunlugu = len(binary_veri)
    
    veri_indeksi = 0
    

    islenmis_resim = resim.copy()

    for values in islenmis_resim:
        for pixel in values:
            r, g, b = veri_binary_cevir(pixel)
            
            
            if veri_indeksi < veri_uzunlugu:
                pixel[0] = int(r[:-1] + binary_veri[veri_indeksi], 2)
                veri_indeksi += 1
                
            if veri_indeksi < veri_uzunlugu:
                pixel[1] = int(g[:-1] + binary_veri[veri_indeksi], 2)
                veri_indeksi += 1
                
            if veri_indeksi < veri_uzunlugu:
                pixel[2] = int(b[:-1] + binary_veri[veri_indeksi], 2)
                veri_indeksi += 1

            if veri_indeksi >= veri_uzunlugu:
                break
        if veri_indeksi >= veri_uzunlugu:
            break
            
    return islenmis_resim


def veri_coz(resim):
    binary_veri = ""

    for values in resim:
        for pixel in values:
            r, g, b = veri_binary_cevir(pixel)

            binary_veri += r[-1]
            binary_veri += g[-1]
            binary_veri += b[-1]

    all_bytes = [binary_veri[i: i+8] for i in range(0, len(binary_veri), 8)]
    
    cozulmus_byte_dizisi = bytearray()
    
    for byte in all_bytes:
        cozulmus_byte_dizisi.append(int(byte, 2))

        try:
            son_kisim = cozulmus_byte_dizisi[-7:].decode("utf-8")
            
            if "==SON==" in son_kisim:
                tam_mesaj_bytes = cozulmus_byte_dizisi[:-7]
                return tam_mesaj_bytes.decode("utf-8")
        except:

            continue
            
    return "Gizli mesaj bulunamadı."