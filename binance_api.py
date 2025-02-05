import os
from dotenv import load_dotenv
import requests
from typing import Optional

# .env dosyasından değişkenleri yükle
load_dotenv()
load_dotenv(override=True)  # Force reload

# Global parametreler
PAR_1 = os.getenv('PAR_1')    # Varsayılan değer kaldırıldı
PAR_2 = os.getenv('PAR_2')    # Varsayılan değer kaldırıldı

class BinanceAPI:
    def __init__(self, coin_code: str = PAR_1, currency_code: str = PAR_2):
        if not coin_code or not currency_code:
            raise ValueError("PAR_1 ve PAR_2 değerleri .env dosyasında tanımlanmalıdır")
        
        self.base_url = "https://api.binance.com/api/v3/ticker/price"
        self.coin_code = coin_code.upper()
        self.currency_code = currency_code.upper()

    def get_price(self) -> Optional[float]:
        """
        Binance borsasından belirtilen coin/currency paritesinin fiyatını çeker
        
        Returns:
            float: Paritenin fiyatı
            None: Hata durumunda None döner
        """
        try:
            # Binance için symbol formatını oluştur (örn: USDTTRY)
            symbol = f"{self.coin_code}{self.currency_code}"
            
            # API'den veriyi çek
            response = requests.get(self.base_url, params={"symbol": symbol})
            response.raise_for_status()  # HTTP hataları için kontrol
            data = response.json()

            # Fiyatı döndür
            return float(data["price"])

        except requests.RequestException as e:
            print(f"Binance API hatası: {e}")
            return None
        except (KeyError, ValueError) as e:
            print(f"Veri işleme hatası: {e}")
            return None

# Test için kullanım örneği
if __name__ == "__main__":
    # Sadece PAR_1/PAR_2 paritesi için test
    binance = BinanceAPI()
    price = binance.get_price()
    if price:
        print(f"Binance {binance.coin_code}/{binance.currency_code} fiyatı: {price} {binance.currency_code}") 