import random
import time
import json
from customer import Customer
from store import Store
from filter import filter_by_cake_type, filter_by_price_range, filtered_by_start_with_letter
from constans import SECONDS_IN_5_MINUTES, SECONDS_IN_A_DAY

class Simulation:
    def __init__(self, store, customers):
        self.store = store
        self.customers = customers

    def simulate_day(self):
        """Bir gunun simulyasiyasini 5 deqiqeye endirmek"""
        print("Gunun simulasiyasi baslayr...")
        for second in range(0, SECONDS_IN_5_MINUTES, 60):  # Real heyatda 1 deqiqeyə bir dovr kecir
            # Her deqiqede musterilerin mehsul almasini simulyasiya et
            self.simulate_customers_purchase()
            time.sleep(1)  # Real heyatda 1 saniye gozleyirik

    def simulate_customers_purchase(self):
        """Müsterilerin mehsul almasi simulyasiyasini heyata kecirir"""
        for customer in self.customers:
            # Her musterinin mehsul almasini tesadufi olaraq simulyasiya edirik
            if random.random() > 0.7:  # 30% ehtimal ile bir musteri mehsul alır
                product_name = random.choice(list(self.store.stock.keys()))
                count = random.randint(1, 3)  # 1 ile 3 arasinda mehsul alir
                try:
                    customer.buy_product(self.store, product_name, count)
                except Exception as e:
                    print(f"Xeta bas verdi: {e}")

        # Gundelik simulyasiya neticelerini gostermek
        self.store.show_kassa()

# Musteri melumatlarini JSON-dan yuklemek
try:
    with open("customers.json", "r", encoding="utf-8") as json_file:
        customers_data = json.load(json_file)
except FileNotFoundError:
    print("Xeta: 'customers.json' fayli tapilmadi.")
    customers_data = []  # Boş siyahı təyin edirik ki, kod davam edə bilsin
except json.JSONDecodeError:
    print("Xeta: 'customers.json' faylinda oxu xetasi bas verdi. Fayl duzgun formatda deyil.")
    customers_data = []

# Musterileri yaratmaq
customers = []
for customer_data in customers_data:
    try:
        customer = Customer(
            name=customer_data["name"],
            age=customer_data["age"]
        )
        customers.append(customer)
    except KeyError as e:
        print(f"Xeta: Mustəri melumatlarinda {e} acari tapilmadi.")
    except Exception as e:
        print(f"Xeta: Musteri yaradilarken xeta bas verdi: {e}")

# Magazani yaratmaq
try:
    my_store = Store("Sweet Treats", 2002)
except Exception as e:
    print(f"Xeta: Magaza yaradilarken xeta bas verdi: {e}")
    my_store = None

# Magazadakı tortları gostermek
if my_store:
    try:
        my_store.show_stock()
    except Exception as e:
        print(f"Xeta: Magazanin stoklari gosterilerken xeta bas verdi: {e}")
        
# Simulyasiya baslatmaq
if my_store:
    simulation = Simulation(my_store, customers)
    simulation.simulate_day()

# Musterilerin balansini və alıs tarixini gostermek
for customer in customers:
    customer.show_balance()
    customer.show_purchase_history()

# Satısları fayla yazmaq
if my_store:
    try:
        my_store.save_sales_to_file()
    except Exception as e:
        print(f"Xeta: Satislar fayla yazilarken xeta bas verdi: {e}")

# Tortları novune gore filterlemek
try:
    my_store.show_filtered_cakes(cake_type="Sokoladli")
except Exception as e:
    print(f"Xeta: Tortlar novune gore filtrlenerken xeta bas verdi: {e}")

# Qiymete gore filterlemek
try:
    my_store.show_filtered_cakes(min_price=30, max_price=60)
except Exception as e:
    print(f"Xeta: Qiymete gore tortlar filtrlenerken xeta baz verdi: {e}")

# Basladıgı herfe gore filterlemek
try:
    my_store.show_filtered_cakes(start_letter="S")
except Exception as e:
    print(f"Xeta: Tortlar bas herfe gore filtrlenerken xeta bas verdi: {e}")
    
# QR kod seklini yaratmaq ucun
if my_store:
    try:
        my_store.generate_stock_qr()
    except Exception as e:
        print(f"Xeta: QR kod yaradilarken xeta bas verdi: {e}")
        
