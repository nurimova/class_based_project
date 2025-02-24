
# Foydalanuvchilarni CSV fayldan o'qish va tahlil qilish

Ushbu loyiha CSV faylidan foydalanuvchilar haqidagi ma'lumotlarni o'qish va tahlil qilish uchun Python dasturini o'z ichiga oladi. Dastur `Users` klassini taqdim etadi, u orqali foydalanuvchilar haqidagi turli ma'lumotlarni olish mumkin.

## Foydalanish

1. **CSV fayl yo'lini ko'rsatib `Users` obyektini yaratish:**
   ```python
   users = Users("foydalanuvchilar.csv")
   ```

2. **Barcha foydalanuvchilarning ismlarini olish:**
   ```python
   first_names = users.first_name_all()
   print(first_names)
   ```

3. **Barcha foydalanuvchilarning familiyalarini olish:**
   ```python
   last_names = users.last_name_all()
   print(last_names)
   ```

4. **Erkak foydalanuvchilar sonini olish:**
   ```python
   male_count = users.gender_male_count()
   print(male_count)
   ```

5. **Ayol foydalanuvchilar sonini olish:**
   ```python
   female_count = users.gender_female_count()
   print(female_count)
   ```

6. **Barcha noyob domen nomlarini olish:**
   ```python
   domains = users.get_all_domen_name()
   print(domains)
   ```

7. **Barcha noyob kasblarni olish:**
   ```python
   jobs = users.get_job()
   print(jobs)
   ```

8. **Ma'lum bir foydalanuvchi haqida ma'lumot olish (ID bo'yicha):**
   ```python
   user_data = users.get_one_user(3)  # ID 3 bo'lgan foydalanuvchi
   print(user_data)
   ```

## Funksiyalar tavsifi

- `first_name_all()`: Barcha foydalanuvchilarning ismlarini ro'yxat shaklida qaytaradi.
- `last_name_all()`: Barcha foydalanuvchilarning familiyalarini ro'yxat shaklida qaytaradi.
- `gender_male_count()`: Erkak foydalanuvchilar sonini qaytaradi.
- `gender_female_count()`: Ayol foydalanuvchilar sonini qaytaradi.
- `get_all_domen_name()`: Elektron pochta manzillaridan domen nomlarini ajratib, noyob ro'yxat shaklida qaytaradi.
- `get_job()`: Barcha noyob kasblarni ro'yxat shaklida qaytaradi.
- `get_one_user(id)`: Berilgan ID bo'yicha foydalanuvchi ma'lumotlarini qaytaradi.
