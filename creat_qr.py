import qrcode
import json

def create_stock_qr_code(stock_data, filename="stock_qr.png"):
    """Stock melumatlarini QR kod olaraq yaradir və fayla saxlayir"""
    try:
        # Stock melumatlarini JSON formatinda cevirmek
        json_stock = json.dumps(stock_data, ensure_ascii=False) 
        qr = qrcode.make(json_stock)
        qr.save(filename)
        print(f"Stock melumatlari '{filename}' faylina QR kod olaraq yadda saxlanildi.")
        qr.show()  # QR kodu birbasa gosterir
    except Exception as e:
        print(f"Xeta bas verdi: {e}")
