# 🛡️ SFAT – Steganography & Forensic Analysis Tool

*A Cybersecurity & Digital Forensics Utility*

**Language Support:** 🇬🇧 English | 🇹🇷 Turkish

---

## 🇬🇧 English

### 📌 Project Overview

SFAT (Steganography & Forensic Analysis Tool) is a Python-based cybersecurity utility designed to demonstrate **Information Hiding (Steganography)** techniques and their detection from a **Digital Forensics** perspective.

The tool simulates how covert communication channels can be created using image files and provides a **Forensic Analyst–style analysis environment** to detect and investigate these hidden manipulations.

---

### 🎯 Objective

* Simulate hidden data transmission using image carriers
* Demonstrate forensic detection of steganographic anomalies
* Provide hands-on insight into offensive (hiding) and defensive (detection) techniques

SFAT uses the **LSB (Least Significant Bit)** algorithm for data embedding and advanced **image processing techniques** for forensic analysis.

---

### 🚀 Features & Capabilities

#### 🔐 Steganography (Offensive)

* **LSB Encoding Engine** – Inject secret UTF-8 text payloads into image pixels with *no visible distortion*
* **Payload Extraction** – Recover hidden messages from suspicious images

#### 🧪 Digital Forensics (Defensive)

* **Forensic Analysis Dashboard** – Professional visualization using Matplotlib & OpenCV
* **Anomaly Detection** – Detect modified pixels via difference mapping and thresholding
* **Quality Metrics** – PSNR (Peak Signal-to-Noise Ratio) calculation to measure image integrity

#### 🌍 General

* **Multi-language Support** – Fully localized English & Turkish interface
* **UTF-8 Compatibility** – Supports special characters seamlessly

---

### 🛠️ Technical Stack

* **Core Language:** Python 3.x
* **Image Processing:** OpenCV (cv2), NumPy
* **Visualization:** Matplotlib

---

### 🔮 Future Enhancements

* **Encryption Layer** – AES-256 encryption before payload embedding
* **Web Interface** – Flask or Django-based web UI
* **Batch Analysis** – Automated scanning of multiple images
* **AI-Based Detection** – Machine learning models to detect steganography without original reference images

---

## 🇹🇷 Türkçe

### 📌 Proje Özeti

SFAT (Steganography & Forensic Analysis Tool), **Bilgi Gizleme (Steganografi)** tekniklerini ve bunların **Adli Bilişim** bakış açısıyla nasıl tespit edilebileceğini göstermek amacıyla geliştirilmiş Python tabanlı bir siber güvenlik aracıdır.

Bu araç, görüntü dosyaları üzerinden gizli iletişim kanallarının nasıl oluşturulduğunu simüle eder ve bir **Adli Bilişim Analisti** gibi analiz yapmayı mümkün kılar.

---

### 🎯 Amaç

* Görüntüler üzerinden gizli veri iletimini simüle etmek
* Steganografik anormalliklerin adli yöntemlerle tespitini göstermek
* Saldırgan (gizleme) ve savunmacı (tespit) teknikleri birlikte öğretmek

SFAT, veri enjeksiyonu için **LSB (En Anlamsız Bit)** algoritmasını ve analiz için ileri seviye **görüntü işleme** tekniklerini kullanır.

---

### 🚀 Özellikler ve Yetenekler

#### 🔐 Steganografi (Saldırgan Perspektifi)

* **LSB Kodlama Motoru** – Görsel bozulma olmadan piksellere gizli UTF-8 metin enjekte eder
* **Veri Çıkarımı** – Şüpheli görüntülerden gizli mesajları geri kurtarır

#### 🧪 Adli Bilişim (Savunmacı Perspektif)

* **Adli Analiz Paneli** – Matplotlib ve OpenCV ile geliştirilmiş profesyonel analiz arayüzü
* **Anormallik Tespiti** – Fark haritalama ve eşikleme ile değiştirilmiş pikselleri görselleştirir
* **Kalite Metrikleri** – Görüntü bütünlüğü için PSNR hesaplaması

#### 🌍 Genel

* **Çoklu Dil Desteği** – Türkçe ve İngilizce tam uyum
* **UTF-8 Uyumluluğu** – Türkçe karakter desteği

---

### 🛠️ Teknik Altyapı

* **Programlama Dili:** Python 3.x
* **Görüntü İşleme:** OpenCV (cv2), NumPy
* **Görselleştirme:** Matplotlib

---

### 🔮 Geliştirme Planları

* **Şifreleme Katmanı** – Gizleme öncesi AES-256 şifreleme
* **Web Arayüzü** – Flask / Django tabanlı arayüz
* **Toplu Analiz** – Birden fazla görselin otomatik taranması
* **Yapay Zeka Tespiti** – Referans görüntü olmadan steganografi tespiti yapan ML modelleri
