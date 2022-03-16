# Tutorial Instalasi

1. Siapkan virtual environment python. Silahkan install python terlebih dahulu jika belum terdapat pyton pada local environment.

    > python -m venv env

2. Install semua requirements yang diperlukan pada requirements.txt yang terletak di root folder
    > pip install -r requirements.txt

3. Jalankan program dengan command runserver
    > python manage.py runserver

---
**NOTE**

Untuk tahap ketiga,perlu dilakukan migrasi terhadap model sebelum menjalankan program.Migrasi telah saya lakukan pada project ini, Namun,jika ingin memastikan kembali apakah migrasi sudah dijalankan, bisa menjalankan program:

    > python manage.py makemigrations
    > python manage.py migrate



---