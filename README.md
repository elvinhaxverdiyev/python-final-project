# 🎂 Sweet Treats Store Simulation

This project is a simple simulation system for a store called **Sweet Treats**. 🏪 The simulation randomly processes customer purchases and includes functionalities such as filtering, balance tracking, purchase history, and sales recording. The project is written in **Python**. 🐍

## 🚀 Features
- 🛍 **Customer Purchase Simulation**: Customers have a 30% chance of purchasing a product.
- ⭐ **Product Reviews**: Purchased products have a 50% chance of receiving a review.
- 📦 **Store Inventory Display**: Shows available products.
- 💾 **Sales Recording**: Daily sales are saved to a file.
- 🔍 **Product Filtering**:
  - 🍰 By cake type
  - 💰 By price range
  - 🔠 By starting letter
- 💳 **Customer Balance & Purchase History**: Displays each customer's balance and purchase records.
- 📲 **QR Code Generation**: Generates QR codes for the store's inventory.

---
## ⚙️ Installation & Running the Simulation
### 1️⃣ Clone the Repository:
```
git clone https://github.com/your-repo/sweet-treats-simulation.git
cd sweet-treats-simulation
```

### 2️⃣ Activate Virtual Environment:
```
pipenv shell
```

### 3️⃣ Install Dependencies:
```
pipenv install
```

### 4️⃣ Run the Simulation:
```
python simulation.py
```

---
## 📁 Project Structure
- 📜 **simulation.py** - Runs the simulation
- 🧑‍💻 **customer.py** - Customer-related functions
- 🏪 **store.py** - Store-related functions
- 🛠 **filter.py** - Filtering functions
- ⚙️ **constants.py** - Constants
- 📄 **customers.json** - Stores customer data in JSON format
- 📖 **README.md** - Project documentation

---
## 📝 How It Works
Once the simulation starts, the store's inventory is displayed, and customers will randomly make purchases. Each minute, a customer has a chance to buy a product. Purchases, customer balances, and other functions operate automatically.

---
## 🛠 Errors & Solutions
- ❌ **`customers.json` not found**: The customer list will be set to empty.
- ❌ **Sales not being recorded**: Check the store file.
- ❌ **Filtering errors**: Verify the filter modules.
- ❌ **QR code generation fails**: Ensure the `qrcode` library is installed:
```
pipenv install qrcode[pil]
```

---
## 👤 Author
This project was developed for **Sweet Treats Simulation**. If you have any questions, feel free to contact us! 📩

---
## 📜 License
This project is distributed under an open-source license. Please respect copyright laws when using it. 📝
