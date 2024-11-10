def filter_by_cake_type(stock, cake_type):
    """Tortlari novune gore filterlemek"""
    filtered = {}
    try:
        for cake, price in stock.items():
            if cake_type.lower() in cake.lower():
                filtered[cake] = price
    except AttributeError as e:
        print(f"Xeta: 'cake' ve ya 'cake_type' deyiseni duzgun formatda deyil. {e}")
    except Exception as e:
        print(f"Qeyri-mueyyen xeta bas verdi filter_by_cake_type funksiyasinda: {e}")
    return filtered

def filter_by_price_range(stock, min_price, max_price):
    """Qiymete gore filterlemek"""
    filtered = {}
    try:
        for cake, price in stock.items():
            if min_price <= price <= max_price:
                filtered[cake] = price
    except TypeError as e:
        print(f"Xeta: Qiymet deyerleri arasinda uygunluq yoxlanilarken sehv bas verdi: {e}")
    except Exception as e:
        print(f"Qeyri-mueyyən xeta bas verdi filter_by_price_range funksiyasinda: {e}")
    return filtered

def filtered_by_start_with_letter(stock, letter):
    """Basladigi herfe gore filterlemek"""
    filtered = {}
    try:
        if not isinstance(letter, str) or len(letter) != 1:
            raise ValueError("Verilen 'letter' parametri duzgun bir herf olmalidir.")
        for cake, price in stock.items():
            if cake[0].lower() == letter.lower():
                filtered[cake] = price
    except ValueError as e:
        print(f"Xeta: {e}")
    except KeyError as e:
        print(f"Xeta: Stockda {e} adli tort tapilmadi.")
    except Exception as e:
        print(f"Qeyri-mueyyen xeta bas verdi filtered_by_start_with_letter funksiyasinda: {e}")
    return filtered

