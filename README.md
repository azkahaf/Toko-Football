Link: https://harish-azka-tokofootball.pbp.cs.ui.ac.id/

<details>
<Summary><b>Tugas 2</b></Summary>

---
### 1. Step by Step Implementasi Tugas 2 (Versi Saya)

1. Saya mulai dengan membuat repository baru di GitHub lewat website.
2. Setelah itu saya clone repository tersebut ke laptop biar bisa dikerjakan secara lokal.
3. Lalu mmebuat dan mengaktifkan virtual environment supaya proyek lebih rapi dan terisolasi.
4. Saya membuat file `requirements.txt`, lalu install semua dependensi dengan menjalankan:

   ```bash
   pip install -r requirements.txt
   ```
5. Saya lanjut bikin project Django baru dengan nama `toko_football` menggunakan perintah:

   ```bash
   django-admin startproject toko_football
   ```
6. Setelah project jadi, saya membuat aplikasi `main` dan mulai mengerjakan bagian logic-nya step by step mulai dari `urls.py`, lanjut ke `views.py`, lalu `models.py`, dan terakhir membuat tampilan di `templates/main.html`.
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

<img width="725" height="525" alt="AlurKerjaDjango" src="https://github.com/user-attachments/assets/4cf79a4c-78f8-4369-b9a8-e22eb307463c" />

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

</details>

<details>
<Summary><b>Tugas 3</b></Summary>

# Tugas 3: Implementasi Form dan Data Delivery pada Django

---

## 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery penting karena sebuah platform tidak pernah berdiri sendiri. Sebuah platform biasanya akan berhubungan dengan platform atau sistem lain, baik untuk bertukar informasi, mengambil data, maupun mengirimkan data. Tanpa adanya mekanisme data delivery, platform akan terisolasi dan tidak bisa berkomunikasi dengan ekosistem di sekitarnya. Dengan data delivery, proses integrasi antar-platform menjadi mungkin, sehingga layanan dapat saling melengkapi dan memberi pengalaman yang lebih kaya untuk pengguna.  

---
## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?  
Secara umum, JSON lebih praktis dibanding XML pada kebanyakan kebutuhan saat ini.

- JSON: ringkas, mudah dibaca manusia, cepat diproses mesin, serta secara alami cocok dengan JavaScript dan bahasa modern lainnya.

- XML: lebih kaya fitur (mendukung schema, namespace, validasi), tapi justru membuat strukturnya lebih rumit dan verbose.

Karena faktor kesederhanaan, performa, dan efisiensi, JSON menjadi standar de facto untuk komunikasi data terutama di API modern.

---
## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?  
Method `is_valid()` dipakai untuk memeriksa apakah data yang dikirimkan melalui form sesuai aturan yang sudah didefinisikan. Jika data memenuhi kriteria, maka menghasilkan True sehingga proses selanjutnya bisa dijalankan. Jika tidak, maka akan menghasilkan False dan Django otomatis menyediakan pesan error yang bisa ditampilkan ke pengguna. Validasi ini krusial agar hanya data yang benar dan sesuai format yang masuk ke database, sekaligus mencegah error maupun input yang berpotensi berbahaya.

---
## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?  
`csrf_token` adalah mekanisme keamanan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Tanpa token ini, seorang penyerang bisa membuat pengguna secara tidak sadar mengirimkan request berbahaya (misalnya mengganti password atau menghapus data) karena server tidak bisa membedakan mana request asli dan mana yang palsu. Dengan csrf_token, setiap form disertai kode unik yang harus cocok dengan yang ada di server. Jika token salah atau hilang, request otomatis ditolak.

---
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step  
Berikut step by step pengerjaan tugas yang saya lakukan:  

1. Menambahkan empat fungsi view di views.py, termasuk untuk daftar produk, tambah produk, dan detail produk.
2. Menghubungkan view dengan URL pattern baru lewat urls.py.
3. Membuat fungsi add_product, show_product, serta menyesuaikan main_page agar menampilkan list produk dan tombol tambah produk.
4. Mengedit index.html supaya mendukung fitur baru, seperti menampilkan daftar produk.
5. Menyediakan halaman baru di folder templates, yaitu add_product.html dan product_details.html.
6. Membuat forms.py berisi ProductForm dengan field sesuai kebutuhan input produk.
7. Menambahkan atribut id pada model Product untuk memberi identitas unik tiap produk.
8. Menambahkan CSRF trusted domains di settings.py agar form dapat berjalan aman ketika diakses via domain tertentu.
  
---
## 6. Apakah ada feedback untuk asdos di tutorial 2?  
Sudah cukup jelas smua penjelasan tutorialnya.

---
## Screenshot Postman:
1. XML

<img width="1920" height="1080" alt="Screenshot (167)" src="https://github.com/user-attachments/assets/dced570f-89e9-4f28-b769-bd7ae069906c" />


3. JSON

<img width="1920" height="1080" alt="Screenshot (169)" src="https://github.com/user-attachments/assets/9c1fd269-d023-4291-a413-562396cb4e46" />


4. XML By ID

<img width="1920" height="1080" alt="Screenshot (168)" src="https://github.com/user-attachments/assets/4ac939d8-b546-4b6a-a9b6-6f81d97e25e8" />


6. JSON By ID

<img width="1920" height="1080" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/2009412f-b181-477f-b74e-803097c31460" />


---

</details>
