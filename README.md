# CloudBox Backend

CloudBox Backend loyihasi - bu Dropbox'ning soddalashtirilgan versiyasi uchun backend API. Loyiha foydalanuvchilarga fayllarni yuklash, boshqarish, qidirish va tartiblash imkoniyatlarini taqdim etadi.

---

## **Loyiha haqida umumiy ma'lumot**

**Turi:** Backend API  
**Maqsad:** Fayllarni boshqarish uchun soddalashtirilgan backend tizim yaratish.  
**Asosiy funksiyalar:**

1. Autentifikatsiya va avtorizatsiya.
2. Fayl boshqaruvi (yuklash, o'chirish, qidirish, tartiblash, qayta tiklash).
3. Papkalar boshqaruvi.
4. Pagination va filtr imkoniyatlari.

---

## **Texnologiyalar**

- **Backend dasturlash tili:** Python
- **Framework:** Django / Django REST Framework
- **Ma'lumotlar bazasi:** PostgreSQL
- **Autentifikatsiya:** JWT (JSON Web Token)
- **Fayl saqlash:** Local storage yoki AWS S3 kabi bulut xizmatlari

---

## **O'rnatish va sozlash**

1. **Loyihani klonlash:**
   ```bash
   git clone https://github.com/username/cloudbox-backend.git
   cd cloudbox-backend
   ```

2. **Virtual muhitni yaratish va faollashtirish:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows uchun: venv\Scripts\activate
   ```

3. **Kerakli kutubxonalarni o'rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ma'lumotlar bazasini sozlash:**
   - `.env` faylini yaratish va quyidagi sozlamalarni qo'shish:
     ```env
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=postgres://username:password@localhost:5432/cloudbox
     ```

   - Ma'lumotlar bazasini yaratish:
     ```bash
     python manage.py migrate
     ```

5. **Serverni ishga tushirish:**
   ```bash
   python manage.py runserver
   ```

---

## **API Endpoints**

### **1. Autentifikatsiya va avtorizatsiya**

- **Ro'yxatdan o'tish:**
  - `POST /api/auth/register`
- **Kirish:**
  - `POST /api/auth/login`
- **Chiqish:**
  - `POST /api/auth/logout`

### **2. Fayl boshqaruvi**

- **Faylni yuklash:**
  - `POST /api/files/upload`
- **Fayllar ro'yxatini olish:**
  - `GET /api/files`
- **Faylni o'chirish:**
  - `DELETE /api/files/{fileId}`
- **Faylni qayta tiklash:**
  - `POST /api/files/{fileId}/restore`

### **3. Papkalar boshqaruvi**

- **Yangi papka yaratish:**
  - `POST /api/folders`
- **Papkalar ro'yxatini olish:**
  - `GET /api/folders`
- **Papkani o'chirish:**
  - `DELETE /api/folders/{folderId}`

---

## **Test qilish**

1. **Unit testlarni ishga tushirish:**
   ```bash
   python manage.py test
   ```

2. **Postman yoki Swagger yordamida API ni sinovdan o'tkazish.**


---

## **Mualliflik**

**Muallif:** Zuhra Erkayeva  


