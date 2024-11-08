import random
import time
import json
from customer import Customer
from store import Store

# Gecikmə parametrləri: Hər bir saniyə real həyatda 1 dəqiqə simulyasiya edir.
SECONDS_IN_A_DAY = 24 * 60 * 60  # Bir gündə olan saniyələr
SECONDS_IN_5_MINUTES = 5 * 60  # 5 dəqiqəlik saniyələr

class Simulation:
    def __init__(self, store, customers):
        self.store = store
        self.customers = customers

    def simulate_day(self):
        """Bir günün simulyasiyasını 5 dəqiqəyə endirmək"""
        print("Simulation started for a day...")
        for second in range(0, SECONDS_IN_5_MINUTES, 60):  # Real həyatda 1 dəqiqəyə bir dövr keçir
            # Hər dəqiqədə müştərilərin məhsul almasını simulyasiya et
            self.simulate_customers_purchase()
            time.sleep(1)  # Real həyatda 1 saniyə gözləyirik

    def simulate_customers_purchase(self):
        """Müştərilərin məhsul alması simulyasiyasını həyata keçirir"""
        for customer in self.customers:
            # Hər müştərinin məhsul almasını təsadüfi olaraq simulyasiya edirik
            if random.random() > 0.7:  # 30% ehtimal ilə bir müştəri məhsul alır
                product_name = random.choice(list(self.store.stock.keys()))
                count = random.randint(1, 3)  # 1 ilə 3 arasında məhsul alır
                customer.buy_product(self.store, product_name, count)

        # Gündəlik simulyasiya nəticələrini göstərmək
        self.store.show_kassa()

# Müştəri məlumatlarını JSON-dan yükləmək
with open("customers.json", "r", encoding="utf-8") as json_file:
    customers_data = json.load(json_file)

# Müştəriləri yaratmaq
customers = []
for customer_data in customers_data:
    customer = Customer(
        name=customer_data["name"],
        age=customer_data["age"]
    )
    customers.append(customer)

# Mağazanı yaratmaq
my_store = Store("Sweet Treats", 2002)

# Mağazadakı tortları göstərmək
my_store.show_stock()

# Simulyasiya başlatmaq
simulation = Simulation(my_store, customers)
simulation.simulate_day()

# Müştərilərin balansını və alış tarixini göstərmək
for customer in customers:
    customer.show_balance()
    customer.show_purchase_history()

# Satışları fayla yazmaq
my_store.save_sales_to_file()

# Tortları növünə görə filterləmək
my_store.show_filtered_cakes(cake_type="Şokoladlı")

# Qiymətə görə filterləmək
my_store.show_filtered_cakes(min_price=30, max_price=60)
