Link: https://harish-azka-tokofootball.pbp.cs.ui.ac.id/

---
### 1. Step by Step Implementasi Tugas 2 (Versi Saya)

1. Saya mulai dengan membuat repository baru di GitHub lewat website.
2. Setelah itu saya clone repository tersebut ke laptop biar bisa dikerjakan secara lokal.
3. Lalu mmebuat dan mengaktifkan virtual environment supaya proyek lebih rapi dan terisolasi.
4. Saya membuat file `requirements.txt`, lalu install semua dependensi dengan menjalankan:

   ```bash
   pip install -r requirements.txt
   ```
5. Saya lanjut bikin project Django baru dengan nama `toko_football` pakai perintah:

   ```bash
   django-admin startproject toko_football
   ```
6. Setelah project jadi, saya membuat aplikasi `main` dan mulai mengerjakan bagian logic-nya step by step: mulai dari `urls.py`, lanjut ke `views.py`, lalu `models.py`, dan terakhir membuat tampilan di `templates/main.html`.
7. Karena ada perubahan di `models.py`, saya menjalankan migrasi dengan:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Saya jalankan server lokal untuk mengecek apakah semuanya udah jalan dengan normal.
9. Supaya file sensitif tidak ikut ke commit, saya membuat `.gitignore` untuk skip file `.env`, `.env.prod`, dan folder `env`.
10. Saya buat file `.env` untuk development dan `.env.prod` untuk production. Di `.env.prod` saya menggunakan nama schema `tugas_individu`.
11. Saya edit `settings.py` supaya memakai environment variables, lalu saya setting konfigurasi production dan database.
12. Setelah semua selesai, saya `git add`, commit, lalu push ke GitHub.
13. Di PWS, saya bikin project baru dan menyamakan konfigurasi environment-nya dengan mengisi `.env.prod`.
14. Terakhir, saya mengikuti langkah-langkah deployment sesuai panduan sampai akhirnya aplikasi bisa diakses lewat internet. 

---

### 2. Alur Django
saya izin untuk mengambil gambar bagan ini dari Forum Diskusi Minggu Kedua - Course PBP SCELE (Discussion "Alur Django") oleh Bu Ara

**Penjelasan:**

1. HTTP Request akan diterima oleh urls.py untuk di cocokkan alamat HTTP dengan path yang telah didefinisikan di sana. Jika sesuai atau cocok, maka path akan diteruskan ke appropriate view pada views.py

2. views.py merupakan tempat dimana fungsi didefinisikan, views.py menerima request dan mengembalikan respons sesuai dengan request yang diminta,
dengan cara berinteraksi/berkomunikasi dengan models.py dengan membaca dan mengubah database yang telah didefinisikan disana.

3. views.py juga mengatur templates atau tampilan mana yang ditampilkan pada laman website sesuai request HTTP (dalam project ini yaitu main.html), mengembalikan dengan response yakni halaman yang diminta.


---

### 3. Peran `settings.py`

File `settings.py` berfungsi untuk men-konfigurasi banyak hal, hal penting yang dilakukan di file tersebut antara lain untuk konfigurasi database (menentukan engine dan kredensial database), lalu juga menyimpan daftar aplikasi yang aktif di dalam proyek (Installed Apps), mengatur alokasi file HTML, CSS, dan JS, serta menyimpan konfigurasi penting untuk deployment seperti allowed hosts, environment variable, dll.

---

### 4. Cara Kerja Migrasi Database

Migrasi database di Django adalah proses sinkronisasi antara perubahan model Python dengan struktur tabel di database. `makemigrations` membuat file instruksi perubahan, sedangkan `migrate` mengeksekusinya ke database, sehingga perubahan model dapat diterapkan tanpa harus menghapus data lama.

---

### 5. Keunggulan Django

Sejujurnya saya belum mengerti banyak tentang web development dan dengan menggunakan Django saya cukup cepat memahami cara kerjanya, sehingga mungkin itu salah satu keunggulan Django. Kalau secara teknis Django punya banyak fitur bawaan seperti autentikasi, ORM, dan admin panel sehingga akan lebih memudahkan bagi beginner. Dan juga struktur development nya yang lebih jelas dan mudah dipahami karena menerapkan MVT (Model-View-Template)

---

### 6. Feedback untuk Asisten Dosen

Sudah sangat mudah dipahami step by step nya, tetapi mungkin akan lebih paham jika offline di lab supaya bisa langsung bertanya.

---


