# nma-gap-bot

## ⚙️ Loyihani Sozlash (Project Setup)

Loyihani ishga tushirish uchun quyidagi bosqichlarni bajaring 👇

### 1. Virtual muhit yaratish

Loyihani izolyatsiya qilish va paketlar o‘rtasida to‘qnashuvni oldini olish uchun virtual muhit yarating:

```bash
python -m venv venv
```

> `venv` — bu virtual muhit nomi, istasangiz o‘zgartirishingiz mumkin.

---

### 2. Virtual muhitni ishga tushurish

Operatsion tizimingizga qarab quyidagi buyruqlardan foydalaning:

#### 🪟 Windows:

```bash
venv\Scripts\activate
```

#### 🐧 Mac/Linux:

```bash
source venv/bin/activate
```

> Virtual muhitdan chiqish uchun:

```bash
deactivate
```

---

### 3. Kerakli kutubxonalarni o‘rnatish

Loyihaga kerakli barcha Python kutubxonalarini o‘rnating:

```bash
pip install <package_name>
```

Masalan:

```bash
pip install django
```

---

### 4. `requirements.txt` faylini yaratish

O‘rnatilgan barcha paketlar ro‘yxatini saqlab qo‘ying:

```bash
pip freeze > requirements.txt
```

---

### 5. `requirements.txt` dan paketlarni o‘rnatish

Boshqa foydalanuvchilar (yoki server) uchun kerakli kutubxonalarni bitta buyruq bilan o‘rnating:

```bash
pip install -r requirements.txt
```

---

### 6. `.env` fayl yaratish

Muhim maxfiy sozlamalar (masalan: API kalitlar, parollar, DB ma’lumotlari) uchun `.env` fayl yarating:

```bash
touch .env
```

> `.env` faylni **GitHub’ga yuklamang** — uni `.gitignore` fayliga qo‘shing.

