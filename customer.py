import random
from datetime import datetime

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = random.randint(100, 250)
        self.purchase_history = []
        self.reviews = {} 

    def __repr__(self):
        return f"Musteri(name = {self.name}, age = {self.age}, balance = {self.balance})"
    
    def buy_product(self, store, product_name, count=1):
        """Musteri mehsul alir"""
        try:
            if product_name not in store.stock:
                raise ValueError(f"{product_name} mağazada mövcud deyil.")  # Mehsul mövcud deyil
            
            product_price = store.stock[product_name]
            total_price = product_price * count
            
            # Balans yoxlanmasi
            if self.balance >= total_price:
                self.balance -= total_price
                store.kassa += total_price
                store.sales.append(f"{self.name} {count} dene {product_name} aldi, total: {total_price} AZN")
                print(f"{self.name} {count}dene {product_name} aldi. Ödenilen məbləğ: {total_price} AZN")
                purchase_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.purchase_history.append(f"{product_name} - {total_price} AZN --> {purchase_time}")
            else:
                raise ValueError(f"{self.name}, kifayət qədər balansınız yoxdur.")  # Balansın kifayət etməməsi

        except ValueError as e:
            print(f"Xeta: {e}")  # Xetanı ekranda gosteririk
        except Exception as e:
            print(f"Xeta bas verdi: {e}")  # umumi səhv halı

    def show_balance(self):
        """Musterinin balansini gosterir"""
        try:
            if self.balance < 0:
                raise ValueError(f"{self.name} nin balansi azdir!")
            print(f"{self.name} nin balansi: {self.balance} AZN")
        except ValueError as e:
            print(f"Xeta: {e}")

    def show_purchase_history(self):
        """Musterinin alis tarixini gosterir"""
        try:
            if not self.purchase_history:
                raise ValueError(f"{self.name} heç bir məhsul almayıb.")
            print(f"{self.name} nin alis tarixi: ")
            for purchase in self.purchase_history:
                print(purchase)
        except ValueError as e:
            print(f"Xeta: {e}")
        except Exception as e:
            print(f"Xeta bas verdi: {e}")

    def add_review(self, store, product_name, rating, review_text):
        """Musterinin mehsul ucun rey ve ulduz deyerlendirmesi"""
        try:
            if product_name not in store.stock:
                raise ValueError(f"{product_name} magazada movcud deyil!")
            
            if not (1 <= rating <= 5):
                raise ValueError("Deyerlendirme 1-den 5-e qeder olmalidir.")
            
            # Rey ve qiymetlendirme elave olunur
            self.reviews[product_name] = {"rating": rating, "review": review_text}
            store.add_review(product_name, rating, review_text)
            print(f"{self.name} mehsul ucun reyi ve deyerlendirmesini elave etdi.")
        
        except ValueError as e:
            print(f"Xeta: {e}")  # Deyer sehvlerini idare edir
        except Exception as e:
            print(f"Xeta bas verdi: {e}") 

    def show_reviews(self):
        """Musterinin verdiyi reyleri gosterir"""
        try:
            if not self.reviews:
                raise ValueError(f"{self.name} hec bir məhsul ucun rey yazmayib.")
            print(f"{self.name} nin yazdigi reyler: ")
            for product, review in self.reviews.items():
                print(f"{product} - Rating: {review['rating']} | Review: {review['review']}")
        except ValueError as e:
            print(f"Xeta: {e}")
        except Exception as e:
            print(f"Xeta bas verdi: {e}")
