🛡️ Steganography & Forensic Analysis Tool (SFAT)
Cybersecurity & Digital Forensics Utility / Siber Güvenlik ve Adli Bilişim Aracı 

Language: English | Turkish

🇬🇧 English 📝 Project Overview
This tool is a specialized cybersecurity utility designed to demonstrate Information Hiding (Steganography) and Digital Forensic Detection techniques.

Objective: The primary goal is to simulate how covert channels are established using image carriers and to provide a "Forensic Analyst" dashboard to detect such anomalies. This Python-based tool utilizes the LSB (Least Significant Bit) algorithm for data injection and advanced Image Processing techniques for detection.

Features and Capabilities:

LSB Encoding Engine: Inject secret text payloads into image pixels with zero visual distortion.

Forensic Dashboard: A professional analysis interface using Matplotlib & OpenCV.

Anomaly Detection: Instantly visualize modified bits using difference mapping and thresholding.

Payload Extraction: Recover hidden messages from suspicious images.

Quality Metrics: Calculate PSNR (Peak Signal-to-Noise Ratio) to assess image integrity.

Multi-Language Support: Fully localized for English and Turkish.

UTF-8 Compatibility: Full support for special characters.

Technical Stack:

Core: Python 3.x

Image Processing: OpenCV (cv2), NumPy

Visualization: Matplotlib

Future Enhancements (Development Plans):

Encryption Layer: AES-256 encryption for payloads before hiding.

Web Interface: Migration to a Flask/Django-based UI.

Batch Analysis: Automated scanning for multiple images.

AI Detection: Machine Learning models to detect steganography without original reference.


🇹🇷 Turkish 📝 Proje Özeti
Bu araç, Bilgi Gizleme (Steganografi) ve Adli Bilişim Tespiti (Digital Forensics) tekniklerini uygulamalı olarak göstermek amacıyla geliştirilmiş bir siber güvenlik yazılımıdır.

Amaç: Temel amaç, görüntü dosyaları üzerinde gizli iletişim kanallarının nasıl oluşturulduğunu simüle etmek ve bir "Adli Bilişim Analisti" gözüyle bu anormalliklerin nasıl tespit edileceğini sağlayan bir analiz ortamı sunmaktır. Python tabanlı bu araç, veri enjeksiyonu için LSB (En Anlamsız Bit) algoritmasını ve tespit için ileri seviye Görüntü İşleme tekniklerini kullanır.

Özellikler ve Yetenekler:

LSB Kodlama Motoru: Görüntüde görsel bozulma yaratmadan piksellere gizli metin enjekte eder.

Adli Analiz Paneli: Matplotlib ve OpenCV tabanlı profesyonel analiz arayüzü.

Anormallik Tespiti: Fark haritalama ve eşikleme yöntemleriyle değiştirilmiş bitleri anında görselleştirir.

Veri Çıkarımı: Şüpheli görüntülerden gizli mesajları geri kurtarır.

Kalite Metrikleri: Görüntü bütünlüğünü ölçmek için PSNR hesaplaması yapar.

Çoklu Dil Desteği: Türkçe ve İngilizce tam uyumlu arayüz.

UTF-8 Uyumluluğu: Türkçe karakterleri sorunsuz işler.

Teknik Altyapı:

Çekirdek: Python 3.x

Görüntü İşleme: OpenCV (cv2), NumPy

Görselleştirme: Matplotlib

Geliştirme Planları (Future Enhancements):

Şifreleme Katmanı: Veriyi gizlemeden önce AES-256 ile şifreleme.

Web Arayüzü: Flask/Django tabanlı web arayüzüne geçiş.

Toplu Analiz: Birden fazla görseli otomatik tarama.

Yapay Zeka Tespiti: Orijinal referans olmadan steganografiyi tespit eden ML modelleri.
