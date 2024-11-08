import random

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.balance = random.randint(100, 250)
        self.purchase_history = []

    # Musterinin temsil olumasi
    def __repr__(self):
        return f"Customer(name = {self.name}, age = {self.age}, balance = {self.balance})"

    def buy_product(self, store, product_name, count=1):
        """Musteri mehsul alir"""
        if product_name not in store.stock:
            print(f"{product_name} movcud deyil.")
            return
        
        product_price = store.stock[product_name]
        total_price = product_price * count
        
        # Balans yoxlanması
        if self.balance >= total_price:
            self.balance -= total_price
            store.kassa += total_price
            store.sales.append(f"{self.name} bought {count} {product_name}, total: {total_price} AZN")
            print(f"{self.name} {count} {product_name} aldi. Ödenilen məbləğ: {total_price} AZN")
            self.purchase_history.append(f"{product_name} - {total_price} AZN")
        else:
            print(f"{self.name}, kifayət qədər balansiniz yoxdur.")

    def show_balance(self):
        """Musterinin balansini gosterir"""
        print(f"{self.name}'s balance: {self.balance} AZN")

    def show_purchase_history(self):
        """Musterinin alis tarixini gosterir"""
        if not self.purchase_history:
            print(f"{self.name} hec bir mehsul almayib.")
        else:
            print(f"{self.name}nin alis tarixi:")
            for purchase in self.purchase_history:
                print(purchase)
