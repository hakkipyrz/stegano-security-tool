import cv2
import os
from core import veri_gizle, veri_coz 

# --- DİL PAKETİ (SADELEŞTİRİLMİŞ) ---
DIL_SOZLUGU = {
    'tr': {
        'menu_title': "🕵️  STEGANOGRAFI SIBER GÜVENLIK ARACI",
        'opt1': "1. Resim İçine Mesaj Gizle (Encode)",
        'opt2': "2. Resimden Mesaj Oku (Decode)",
        'opt3': "3. Çıkış", # Artık 3 numara Çıkış oldu
        'choice': "\nSeçiminiz (1-3): ",
        'mode_encode': "\n--- MESAJ GİZLEME MODU ---",
        'mode_decode': "\n--- MESAJ ÇÖZME MODU ---",
        'ask_img': "Assets klasöründeki resim adı (uzantısıyla, örn: test.png): ",
        'err_img': "HATA: Resim bulunamadı! İsmi doğru yazdığınızdan emin olun.",
        'info_alpha': "Bilgi: Resim şeffaf (Alpha) kanala sahip, RGB'ye dönüştürülüyor...",
        'ask_msg': "Gizlenecek gizli mesajı yazın: ",
        'wait': "\nİşlem yapılıyor, lütfen bekleyin...",
        'success': "✅ BAŞARILI! Mesaj gizlendi.",
        'saved_at': "Yeni resim şuraya kaydedildi: ",
        'err_gen': "HATA OLUŞTU: ",
        'ask_out_img': "Output klasöründeki okunacak resim adı (genelde: gizli_resim.png): ",
        'scanning': "\nResim taranıyor...",
        'result_title': "🔓 GİZLİ MESAJ: ",
        'bye': "Program kapatılıyor...",
        'invalid': "Geçersiz seçim, tekrar deneyin."
    },
    'en': {
        'menu_title': "🕵️  STEGANOGRAPHY CYBER SECURITY TOOL",
        'opt1': "1. Hide Message in Image (Encode)",
        'opt2': "2. Read Message from Image (Decode)",
        'opt3': "3. Exit",
        'choice': "\nYour Choice (1-3): ",
        'mode_encode': "\n--- ENCODE MODE ---",
        'mode_decode': "\n--- DECODE MODE ---",
        'ask_img': "Image name in Assets folder (with extension, e.g., test.png): ",
        'err_img': "ERROR: Image not found! Check the filename.",
        'info_alpha': "Info: Image has Alpha channel, converting to RGB...",
        'ask_msg': "Enter the secret message to hide: ",
        'wait': "\nProcessing, please wait...",
        'success': "✅ SUCCESS! Message hidden.",
        'saved_at': "New image saved at: ",
        'err_gen': "ERROR OCCURRED: ",
        'ask_out_img': "Image name in Output folder (usually: gizli_resim.png): ",
        'scanning': "\nScanning image...",
        'result_title': "🔓 HIDDEN MESSAGE: ",
        'bye': "Exiting...",
        'invalid': "Invalid choice, try again."
    }
}

SECILEN_DIL = 'tr' 

def dil_secimi_yap():
    global SECILEN_DIL
    print("\n" + "="*30)
    print("LANGUAGE SELECTION / DİL SEÇİMİ")
    print("="*30)
    print("1. Türkçe")
    print("2. English")
    secim = input("Seçim / Choice (1-2): ")
    if secim == '2':
        SECILEN_DIL = 'en'
        print("Language set to English.")
    else:
        SECILEN_DIL = 'tr'
        print("Dil Türkçe olarak ayarlandı.")

def metin_getir(anahtar):
    return DIL_SOZLUGU[SECILEN_DIL][anahtar]

def ana_menu():
    print("\n" + "="*45)
    print(" " + metin_getir('menu_title'))
    print("="*45)
    print(metin_getir('opt1'))
    print(metin_getir('opt2'))
    print(metin_getir('opt3'))
    secim = input(metin_getir('choice'))
    return secim

def islem_gizle():
    print(metin_getir('mode_encode'))
    dosya_adi = input(metin_getir('ask_img'))
    girdi_yolu = f"assets/{dosya_adi}"
    
    resim = cv2.imread(girdi_yolu, cv2.IMREAD_UNCHANGED)
    
    if resim is None:
        print(metin_getir('err_img'))
        return

    if resim.shape[2] == 4:
        print(metin_getir('info_alpha'))
        resim = cv2.cvtColor(resim, cv2.COLOR_BGRA2BGR)

    mesaj = input(metin_getir('ask_msg'))
    print(metin_getir('wait'))
    
    try:
        sifreli_resim = veri_gizle(resim, mesaj)
        cikti_yolu = "output/gizli_resim.png"
        cv2.imwrite(cikti_yolu, sifreli_resim, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        print(metin_getir('success'))
        print(f"{metin_getir('saved_at')} {cikti_yolu}")
    except Exception as e:
        print(f"{metin_getir('err_gen')} {e}")

def islem_coz():
    print(metin_getir('mode_decode'))
    dosya_adi = input(metin_getir('ask_out_img'))
    dosya_yolu = f"output/{dosya_adi}"
    resim = cv2.imread(dosya_yolu, cv2.IMREAD_UNCHANGED)
    
    if resim is None:
        print(metin_getir('err_img'))
        return
        
    print(metin_getir('scanning'))
    try:
        cozulen_mesaj = veri_coz(resim)
        print("-" * 30)
        print(f"{metin_getir('result_title')} {cozulen_mesaj}")
        print("-" * 30)
    except Exception as e:
         print(f"{metin_getir('err_gen')} {e}")

if __name__ == "__main__":
    if not os.path.exists("output"):
        os.makedirs("output")
        
    dil_secimi_yap()

    while True:
        secim = ana_menu()
        if secim == '1':
            islem_gizle()
        elif secim == '2':
            islem_coz()
        elif secim == '3':
            print(metin_getir('bye'))
            break
        else:
            print(metin_getir('invalid'))