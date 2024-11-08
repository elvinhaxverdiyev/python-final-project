# filter.py

def filter_by_cake_type(stock, cake_type):
    """tortlari nove gore filerlemek"""
    filtered = {}
    for cake, price in stock.items():
        if cake_type.lower() in cake.lower():
            filtered[cake] = price
    return filtered

def filter_by_price_range(stock, min_price, max_price):
    """qiymete gore filterlemek"""
    filtered = {}
    for cake, price in stock.items():
        if min_price <= price <= max_price:
            filtered[cake] = price
    return filtered
