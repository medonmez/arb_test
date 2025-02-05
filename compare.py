from bitci_api import BitciAPI, PAR_1, PAR_2
from binance_api import BinanceAPI
from typing import Tuple, Optional, Dict

def get_prices() -> Tuple[Optional[float], Optional[float]]:
    """
    Her iki borsadan fiyatları çeker
    
    Returns:
        Tuple[Optional[float], Optional[float]]: (Bitci fiyatı, Binance fiyatı)
    """
    bitci = BitciAPI()
    binance = BinanceAPI()
    
    bitci_price = bitci.get_price()
    binance_price = binance.get_price()
    
    return bitci_price, binance_price

def calculate_difference(price1: float, price2: float) -> float:
    """
    İki fiyat arasındaki yüzdelik farkı hesaplar
    
    Args:
        price1: İlk fiyat
        price2: İkinci fiyat
    
    Returns:
        float: Yüzdelik fark
    """
    return ((price1 - price2) / price2) * 100

def get_comparison_data() -> Dict:
    """
    Karşılaştırma verilerini hazırlar
    
    Returns:
        Dict: Karşılaştırma sonuçlarını içeren sözlük
    """
    bitci_price, binance_price = get_prices()
    
    if bitci_price is None or binance_price is None:
        return {
            "success": False,
            "message": "❌ Fiyatlar alınamadı"
        }
    
    diff = calculate_difference(bitci_price, binance_price)
    
    return {
        "success": True,
        "bitci_price": bitci_price,
        "binance_price": binance_price,
        "difference": diff,
        "higher_exchange": "Bitci" if diff > 0 else "Binance" if diff < 0 else None
    }

if __name__ == "__main__":
    print(f"\n{PAR_1}/{PAR_2} Fiyat Karşılaştırması")
    print("-" * 30)
    
    data = get_comparison_data()
    
    if not data["success"]:
        print(data["message"])
    else:
        print(f"Bitci   : {data['bitci_price']:.4f}")
        print(f"Binance : {data['binance_price']:.4f}")
        
        if data["higher_exchange"]:
            print(f"Fark    : +%{abs(data['difference']):.2f} ({data['higher_exchange']})")
        else:
            print("Fark    : %0.00") 