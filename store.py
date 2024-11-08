import json
from filter import filter_by_cake_type, filter_by_price_range 

class Store:
    def __init__(self, name, since):
        self.name = name
        self.since = since
        with open("cakes.json", "r", encoding="utf-8") as json_file:
            self.stock = json.load(json_file) 
        self.kassa = 0
        self.sales = []

    def show_stock(self):
        """Stock-u ekrana yazir"""
        print("Products in stock:")
        print("-" * 30)
        for cake, price in self.stock.items():
            print(f"{cake}: {price} AZN")
        print("-" * 30)

    def sell_item(self, customer, item_name, count=1):
        """Satilan məhsulu kassa və muştəri balansini yeniləyir"""
        if item_name in self.stock:
            price = self.stock[item_name]
            total_price = price * count
            if customer.balance >= total_price:
                # Musteri balansi yeterince varsa
                customer.balance -= total_price
                self.kassa += total_price
                self.sales.append(f"{customer.name} bought {count} {item_name}, total: {total_price} AZN")
                customer.purchase_history.append(f"{item_name} - {total_price} AZN")
                print(f"{customer.name} bought {count} {item_name}. Total: {total_price} AZN")
            else:
                print(f"{customer.name}, yertersiz balans.")
        else:
            print(f"{item_name} stockda yoxdur.")

    def show_kassa(self):
        """Kassa meblegini ekranda gosterir"""
        print(f"Kassadaki total gelir: {self.kassa} AZN")

    def save_sales_to_file(self):
        """Satislari fileye yazir"""
        with open("sales_report.txt", "w", encoding="utf-8") as file:
            file.write("Sales Report:\n")
            file.write("-" * 40 + "\n")
            for sale in self.sales:
                file.write(sale + "\n")
            file.write("-" * 40 + "\n")
            file.write(f"Kassaya gelen total gelir: {self.kassa} AZN\n")
            print("Sales data saved to 'sales_report.txt'.")

    def show_filtered_cakes(self, cake_type=None, min_price=None, max_price=None):
        """Tortlari filterleyen func"""
        filtered_cakes = self.stock

        if cake_type:
            # Tort novu ilə filtrleme
            filtered_cakes = filter_by_cake_type(filtered_cakes, cake_type)
            print(f"\n{cake_type.capitalize()} Cakes:")

        if min_price is not None and max_price is not None:
            # Qiymete gore filterlemek
            filtered_cakes = filter_by_price_range(filtered_cakes, min_price, max_price)
            print(f"\nBu araliqdaki tortlar {min_price} ve {max_price} AZN:")

        if not filtered_cakes:
            print("Ugun tort tapilmadi.")
            return

        for cake, price in filtered_cakes.items():
            print(f"{cake}: {price} AZN")
