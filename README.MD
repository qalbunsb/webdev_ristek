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

Setelah ketiga tahapan tersebut dilakukan, program bisa dijalankan. Dalam project, sudah terdapat akun superuser dengan username *admin* dan password *password*. Jika ingin membuat akun superuser baru, dapat menjalankan perintah

    > python manage.py createsuperuser

Akun superuser dapat menggunakan seluruh fitur yang ada dalam projek ini. Artikel/Post dapat dibuat dengan akun superuser atau akun yang sudah terakui sebagai staff.

