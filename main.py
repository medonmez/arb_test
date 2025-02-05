import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from compare import get_comparison_data, PAR_1, PAR_2

# .env dosyasından değişkenleri yükle
load_dotenv()
load_dotenv(override=True)  # Force reload

# Telegram bot token'ı
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

# Bot ayarları
raw_value = os.getenv('MIN_ARBITRAGE_PERCENTAGE')
print(f"Raw value from .env: '{raw_value}'")
MIN_DIFFERENCE = float(raw_value)
CHECK_INTERVAL = int(os.getenv('CHECK_INTERVAL'))

def send_telegram_message(message: str) -> bool:
    """
    Telegram'a mesaj gönderir
    
    Args:
        message: Gönderilecek mesaj
    
    Returns:
        bool: Mesaj başarıyla gönderildiyse True
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": str(CHANNEL_ID),
        "text": message,
        "parse_mode": "MarkdownV2",  # Markdown formatını kullan
        "disable_web_page_preview": True,  # Link önizlemesini kapat
        "disable_notification": False  # Bildirim sesi açık
    }
    
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return True
        else:
            print(f"Telegram API Hatası: {response.text}")
            return False
    except Exception as e:
        print(f"Telegram mesaj hatası: {e}")
        return False

def check_prices():
    """Fiyatları kontrol eder ve arbitraj fırsatı varsa kanal'a mesaj gönderir"""
    data = get_comparison_data()
    
    if data["success"]:
        abs_diff = abs(data["difference"])
        
        # Fark minimum değerin üzerindeyse bildir
        if abs_diff >= MIN_DIFFERENCE:
            # Markdown için özel karakterleri escape et
            message = (
                "🔔 *Arbitraj Fırsatı* 💰\n\n"
                f"💱 Çift: `{PAR_1}/{PAR_2}`\n"
                f"🟢 Bitci: `{data['bitci_price']:.4f} {PAR_2}`\n"
                f"🔵 Binance: `{data['binance_price']:.4f} {PAR_2}`\n"
                f"📊 Fark: `%{abs_diff:.2f}` {'📈' if data['higher_exchange'] == 'Bitci' else '📉'}\n"
                f"⏰ Tarih: `{datetime.now().strftime('%d.%m.%Y %H:%M')}`"
            )
            
            # Markdown için özel karakterleri escape et
            message = message.replace('.', '\\.').replace('-', '\\-').replace('_', '\\_')
            
            if send_telegram_message(message):
                print(f"✅ Mesaj gönderildi - Fark: %{abs_diff:.2f}")
            else:
                print("❌ Mesaj gönderilemedi")

def test_telegram_connection():
    """Telegram bağlantısını test eder"""
    message = "🔔 *Test Mesajı* 🚀\n\n🔄 Bot bağlantısı test ediliyor\\."
    
    print(f"🤖 Bot Token: {TOKEN}")
    print(f"📱 Channel ID: {CHANNEL_ID}")
    
    if send_telegram_message(message):
        print("✅ Test mesajı başarıyla gönderildi")
    else:
        print("❌ Test mesajı gönderilemedi")

def main():
    # Gerekli çevre değişkenlerini kontrol et
    required_vars = ['TELEGRAM_BOT_TOKEN', 'TELEGRAM_CHANNEL_ID', 
                    'PAR_1', 'PAR_2', 
                    'MIN_ARBITRAGE_PERCENTAGE', 'CHECK_INTERVAL']
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        print("❌ Eksik çevre değişkenleri:")
        for var in missing_vars:
            print(f"   - {var}")
        return
    
    print("🤖 Bot başlatılıyor...")
    print(f"📊 Minimum fark: %{MIN_DIFFERENCE}")
    print(f"⏱️ Kontrol aralığı: {CHECK_INTERVAL} saniye")
    
    while True:
        try:
            check_prices()
            time.sleep(CHECK_INTERVAL)  # .env'den gelen süre kadar bekle
        except KeyboardInterrupt:
            print("\n👋 Bot durduruluyor...")
            break
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")
            time.sleep(5)  # Hata durumunda 5 saniye bekle

if __name__ == '__main__':
    test_telegram_connection()  # Önce testi çalıştır
    main()  # Test başarılıysa ana programı başlat 