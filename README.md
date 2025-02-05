# Kripto Arbitraj Telegram Botu PRD

## Proje Özeti
Bu bot, Bitci ve Binance borsaları arasındaki fiyat farklarını takip ederek arbitraj fırsatlarını tespit eder ve Telegram kanalı üzerinden kullanıcıları bilgilendirir.

## Temel Özellikler

### 1. Veri Toplama
- Bitci API'sinden kripto para çiftlerinin fiyat verilerini çekme
- Binance API'sinden aynı kripto para çiftlerinin fiyat verilerini çekme
- Her iki borsadan veri çekme işlemi belirli aralıklarla (örn: 1 dakika) tekrarlanacak

### 2. Veri İşleme
- İki borsa arasındaki fiyat farklarının hesaplanması
- Belirli bir yüzdenin (örn: %1.5) üzerindeki farkların tespit edilmesi
- İşlem hacmi kontrolü

### 3. Telegram Entegrasyonu
- Tespit edilen arbitraj fırsatlarının Telegram kanalına otomatik mesaj olarak gönderilmesi
- Mesaj formatı:
  ```
  🔄 Arbitraj Fırsatı
  Çift: BTC/USDT
  Bitci: 65,000 USDT
  Binance: 64,000 USDT
  Fark: %1.56 ⬆️
  Tarih: 12.03.2024 14:30
  ```

## Teknik Gereksinimler
- Python programlama dili
- python-telegram-bot kütüphanesi
- requests kütüphanesi (API istekleri için)
- Sürekli çalışan bir sunucu veya host

## Güvenlik
- API anahtarları ve token'lar environment variables olarak saklanacak
- Rate limiting kurallarına uyulacak
- Hata yönetimi ve loglama sistemi

## Gelecek Geliştirmeler
- Daha fazla borsa eklenmesi
- Minimum fark yüzdesinin ayarlanabilmesi
- Özel kripto para çiftlerinin takibi
- Anlık fiyat sorgulama komutları

## Kurulum

### 1. Virtual Environment Oluşturma
```bash
# Virtual environment oluştur
python -m venv venv

# Windows'ta aktive etme
venv\Scripts\activate

# Linux/Mac'te aktive etme
source venv/bin/activate
```

### 2. Gerekli Paketlerin Kurulumu
```bash
pip install -r requirements.txt
```

### 3. Environment Variables Ayarlama
- `.env.example` dosyasını `.env` olarak kopyalayın
- `.env` dosyasındaki değişkenleri kendi değerlerinizle güncelleyin

### 4. Botu Çalıştırma
```bash
python main.py
```

### 5. Sunucuda Sürekli Çalıştırma (Linux)
```bash
nohup python main.py &
``` 