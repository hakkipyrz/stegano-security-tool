import cv2
import numpy as np
import matplotlib.pyplot as plt
from core import veri_coz  

import cv2
import numpy as np
import matplotlib.pyplot as plt
from core import veri_coz  

def create_forensic_report(original_path, suspicious_path):
    """
    Dijital adli bilişim raporu oluşturur. 
    Orijinal ve şüpheli görseli karşılaştırarak LSB (Least Significant Bit) manipülasyonlarını görselleştirir.
    """
    
    print("Initializing forensic analysis...")
    
    img_org = cv2.imread(original_path)
    img_susp = cv2.imread(suspicious_path)
    
    if img_org is None or img_susp is None:
        print("ERROR: Could not read image files.")
        return

    img_org_rgb = cv2.cvtColor(img_org, cv2.COLOR_BGR2RGB)
    img_susp_rgb = cv2.cvtColor(img_susp, cv2.COLOR_BGR2RGB)

    diff = cv2.absdiff(img_org_rgb, img_susp_rgb)
    
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    
    _, mask = cv2.threshold(diff_gray, 0, 255, cv2.THRESH_BINARY)

    detection_map = np.zeros_like(img_org_rgb)
    
    detection_map[mask > 0] = [0, 255, 0] 

    try:
        hidden_data = veri_coz(img_susp)
        status_msg = "CRITICAL DATA DETECTED / KRİTİK VERİ TESPİTİ"
    except:
        hidden_data = "No readable data found / Veri Okunamadı."
        status_msg = "CLEAN / TEMİZ"

    plt.style.use('dark_background') 
    
    fig = plt.figure(figsize=(14, 8))
    fig.suptitle('DIGITAL FORENSICS & STEGANALYSIS REPORT', fontsize=16, fontweight='bold', color='cyan')

    ax1 = fig.add_subplot(2, 2, 1)
    ax1.imshow(img_susp_rgb)
    ax1.set_title("EVIDENCE A: Suspicious Image", color='white', fontsize=11)
    ax1.axis('off') 


    ax2 = fig.add_subplot(2, 2, 2)
    ax2.imshow(detection_map)
    ax2.set_title("TECHNICAL ANALYSIS: LSB Modification Map", color='lime', fontsize=11)
    ax2.set_xlabel("Green pixels indicate modified bits.")
    ax2.set_xticks([])
    ax2.set_yticks([])

    ax3 = fig.add_subplot(2, 1, 2)
    ax3.axis('off')
    
    report_text = (
        f"--- FORENSIC REPORT SUMMARY ---\n"
        f"STATUS: {status_msg}\n"
        f"SOURCE FILE: {suspicious_path}\n"
        f"METHOD: LSB (Least Significant Bit) Injection Analysis\n"
        f"--------------------------------------------------\n"
        f">> EXTRACTED PAYLOAD (ÇÖZÜLEN VERİ):\n\n"
        f"{hidden_data}\n\n"
        f"--------------------------------------------------"
    )
    
    props = dict(boxstyle='round', facecolor='black', alpha=0.6, edgecolor='cyan')
    
    ax3.text(0.05, 0.5, report_text, fontsize=12, fontfamily='monospace', 
             color='white', verticalalignment='center', bbox=props)

    print("Report generated. Displaying dashboard...")
    plt.tight_layout() 
    plt.show()

def calculate_psnr(org_path, susp_path):
    img1 = cv2.imread(org_path)
    img2 = cv2.imread(susp_path)
    
    mse = np.mean((img1 - img2) ** 2)
    
    if mse == 0: return 100
    
    return 20 * np.log10(255.0 / np.sqrt(mse))

def compare_histogram(org_path, susp_path):
    create_forensic_report(org_path, susp_path)