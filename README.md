# 🎂 Sweet Treats Mağaza Simulyasiyası

Bu layihə, **Sweet Treats** adlı bir mağaza üçün sadə bir simulyasiya sistemidir. 🏪 Simulyasiya müştərilərin alışlarını təsadüfi şəkildə həyata keçirir və müxtəlif filtr, balans, tarixçə, satış kimi funksionallıqları əhatə edir. Layihə **Python** dili ilə yazılmışdır. 🐍

## 🚀 Layihənin Funksionallığı
- 🛍 **Müştərilərin Alış Simulyasiyası**: Müştərilər 30% ehtimal ilə məhsul alır.
- ⭐ **Məhsul Rəyləri**: Alınan məhsullara 50% ehtimal ilə rəy əlavə edilir.
- 📦 **Mağazanın Anbar Göstəricisi**: Mövcud məhsullar göstərilir.
- 💾 **Satışları Fayla Yazmaq**: Günlük satışlar fayla yazılır.
- 🔍 **Məhsulları Filtrləmək**:
  - 🍰 Tort növünə görə
  - 💰 Qiymət aralığına görə
  - 🔠 Başlanğıc hərfinə görə
- 💳 **Müştəri Balansı və Alış Tarixçəsi**: Hər müştərinin balansı və alış tarixi göstərilir.
- 📲 **QR Kod Yaratmaq**: Mağazanın stokunda olan məhsulların QR kodu yaradılır.

---
## ⚙️ Quraşdırma və İşə Salma
### 1️⃣ Layihəni klonlayın:
```bash
git clone https://github.com/sizin-repo/sweet-treats-simulation.git
cd sweet-treats-simulation
```

### 2️⃣ Virtual Mühiti Aktivləşdirin:
```bash
pipenv shell
```

### 3️⃣ Lazımi kitabxanaları quraşdırın:
```bash
pipenv install
```

### 4️⃣ Simulyasiyanı İşə Salın:
```bash
python simulation.py
```

---
## 📁 Fayl Strukturu
- 📜 **simulation.py** - Simulyasiya prosesi
- 🧑‍💻 **customer.py** - Müştəri ilə bağlı funksiyalar
- 🏪 **store.py** - Mağaza ilə bağlı funksiyalar
- 🛠 **filter.py** - Filtr funksiyaları
- ⚙️ **constants.py** - Sabitlər
- 📄 **customers.json** - Müştəri məlumatlarını saxlayan JSON faylı
- 📖 **README.md** - Layihənin izahı

---
## 📝 İstifadə Qaydaları
Simulyasiya başladıqdan sonra mağazanın anbarı göstəriləcək və müştərilər təsadüfi şəkildə məhsul alacaq. Hər dəqiqədə bir müştərinin məhsul alma ehtimalı var. Alışlar, müştəri balansı və digər funksiyalar avtomatik işləyəcəkdir.

---
## 🛠 Xətalar və Həllər
- ❌ **`customers.json` tapılmırsa**, müştəri siyahısı boş təyin olunacaq.
- ❌ **Satışlar fayla yazılmırsa**, mağaza faylını yoxlayın.
- ❌ **Filtrləmə xətası baş verərsə**, filtr modullarını yoxlayın.
- ❌ **QR kod generasiya olunmazsa**, `qrcode` kitabxanasının quraşdırıldığından əmin olun:
```bash
pipenv install qrcode[pil]
```

---
## 👤 Müəllif
Bu layihə **Sweet Treats Simulyasiya** üçün hazırlanmışdır. Əgər hər hansı sualınız varsa, bizimlə əlaqə saxlayın! 📩

---
## 📜 Lisenziya
Bu layihə açıq mənbə lisenziyası altında paylanır. İstifadə edərkən müəllif hüquqlarına hörmət edin. 📝

