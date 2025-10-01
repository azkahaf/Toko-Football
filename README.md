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

<details>
<Summary><b>Tugas 4</b></Summary>

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

---

## 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
`AuthenticationForm` adalah form bawaan Django yang digunakan untuk menangani proses login pengguna. Form ini secara otomatis memvalidasi username dan password berdasarkan model User yang terdaftar.

**Kelebihan:**
- Sudah terintegrasi penuh dengan sistem autentikasi bawaan Django sehingga lebih terjamin keamanannya.
- Lebih cepat dan simple, karena tidak diperlukan untuk membuat form manual.

**Kekurangan:**
- Terbatas pada field standar yaitu username dan password, sehingga jika ingin menambahkan custom field seperti SSO, perlu dilakukan override.

---

## 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
- **Autentikasi** adalah proses memverifikasi identitas pengguna, biasanya dengan username/email dan password.

- Sedangkan **Otorisasi** adalah proses menentukan hak akses apa yang dimiliki oleh pengguna yang sudah terautentikasi.

**Implementasi di Django:**
- Autentikasi ditangani dengan sistem `django.contrib.auth`, termasuk User model, AuthenticationForm, dan fungsi untuk masuk (log in) dan keluar (logout).
- Otorisasi ditangani dengan permission (add, change, delete, view) yang terasosiasi dengan model dan diatur oleh decorator `@login_required` dan `@permission_required` untuk membatasi akses pada view.

---

## 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

**Session:**

   Kelebihan:
   - Data disimpan di server, hanya session ID yang tersimpan di browser sehingga lebih aman.
   - Oleh karena itu maka bisa menyimpan data yang lebih kompleks.

   Kekurangan:
   - Sangat membebani server karena harus menyimpan data banyak user.

**Cookies:**

   Kelebihan:
   - Disimpan di client, sehingga tidak membebani server.

   Kekurangan:
   - Rentan terhadap serangan XSS/CSRF jika tidak diamankan.
   - Ukurannya terbatas (karena disimpan di client).
   - Data sensitif tidak boleh disimpan langsung dalam cookie karena rentan.

---

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
**Penggunaan cookies tidak sepenuhnya aman secara default karena:**
- Bisa diakses lewat JavaScript (rentan XSS).
- Bisa dicuri melalui koneksi yang tidak terenkripsi (Man-in-the-Middle attack).
- Bisa dipalsukan oleh pengguna.

**Django menangani risiko ini dengan:**
- Menggunakan HttpOnly flag (mencegah akses cookie via JavaScript).
- Menggunakan Secure flag (cookie hanya dikirim melalui HTTPS).
- CSRF protection otomatis melalui middleware.
- Session cookie Django secara default disimpan dengan nama yang acak dan terenkripsi (menggunakan SECRET_KEY).

---

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. Membuat fungsi **login** dan **register** pada `views.py`.
2. Menambahkan routing untuk `login`, `register`, dan `logout` di `urls.py`.
3. Membuat template HTML khusus untuk halaman login dan register.
4. Mengimplementasikan fungsi **logout** serta menambahkan tombol logout pada `main.html`.
5. Mendaftarkan path `logout` ke dalam `urls.py`.
6. Menggunakan decorator `@login_required` untuk membatasi akses ke halaman utama dan fitur **show product**.
7. Mengelola cookies: menyimpan saat login, menghapus saat logout, serta menampilkan informasi **last login** di halaman utama.
8. Menghubungkan entitas `Product` dengan `User` agar setiap produk memiliki informasi siapa yang menambahkannya.
9. Menjalankan migrasi setelah melakukan perubahan pada `models.py`.
10. Menyesuaikan fungsi **add\_product** agar produk baru secara otomatis terkait dengan user yang membuatnya.
11. Memodifikasi halaman utama untuk menambahkan fitur **filtering** produk.
12. Menyesuaikan halaman detail produk agar menampilkan informasi user yang menambahkan produk tersebut.
13. Melakukan proses **add-commit-push** ke GitHub dan juga ke PWS.


---

</details>

<details>
<Summary><b>Tugas 4</b></Summary>

## 1. Urutan Prioritas CSS Selector
Jika sebuah elemen HTML memiliki beberapa style dari selector CSS yang berbeda, browser akan menentukan style mana yang akan diterapkan berdasarkan urutan prioritas atau yang biasa disebut spesifisitas (specificity). Berikut adalah urutannya dari prioritas tertinggi ke terendah:

1. !important Rule: Aturan CSS yang diakhiri dengan !important akan mengalahkan semua aturan lainnya. Namun, penggunaannya sangat tidak disarankan kecuali dalam keadaan terpaksa karena dapat membuat CSS sulit dikelola.

Contoh: color: blue !important;

2. Inline Style: CSS yang ditulis langsung pada atribut style di dalam tag HTML.

Contoh: <div style="color: red;"></div>

3. ID Selector: CSS yang menargetkan elemen berdasarkan id uniknya.

Contoh: #header { color: green; }

4. Class, Attribute, dan Pseudo-class Selectors: Prioritas di level ini setara.

Class: .button { color: purple; }

Attribute: input[type="text"] { border: 1px solid gray; }

Pseudo-class: a:hover { text-decoration: underline; }

5. Element dan Pseudo-element Selectors: Menargetkan semua elemen dari jenis tag tertentu. Ini adalah prioritas terendah.

Element: div { font-size: 16px; }

Pseudo-element: p::first-line { font-weight: bold; }

Jika terdapat dua selector dengan prioritas yang sama, maka aturan yang didefinisikan paling akhir di dalam file CSS akan menjadi pemenangnya.

## 2. Pentingnya Responsive Design
Responsive design adalah konsep penting karena bertujuan untuk membuat halaman web terlihat dan berfungsi dengan baik di berbagai macam perangkat dengan ukuran layar yang berbeda, mulai dari desktop, laptop, tablet, hingga smartphone.

Mengapa ini penting?

1. Pengalaman Pengguna (User Experience): Situs yang responsif memberikan pengalaman yang nyaman bagi pengguna di perangkat apa pun. Pengguna tidak perlu melakukan zoom-in/zoom-out atau scroll ke samping untuk membaca konten.

2. Peningkatan Jangkauan Pengguna: Sebagian besar pengguna internet saat ini mengakses web melalui perangkat mobile. Tanpa desain yang responsif, Anda akan kehilangan audiens yang sangat besar.

3. SEO (Search Engine Optimization): Mesin pencari seperti Google memprioritaskan situs yang mobile-friendly dalam hasil pencariannya. Situs yang tidak responsif akan mendapatkan peringkat yang lebih rendah.

4. Efisiensi Perawatan: Anda hanya perlu mengelola satu basis kode (codebase) untuk semua perangkat, bukan membuat versi terpisah untuk desktop dan mobile.

Tentu, berikut adalah jawaban untuk soal-soal tersebut:

1. Urutan Prioritas CSS Selector
Jika sebuah elemen HTML memiliki beberapa style dari selector CSS yang berbeda, browser akan menentukan style mana yang akan diterapkan berdasarkan urutan prioritas atau yang biasa disebut spesifisitas (specificity). Berikut adalah urutannya dari prioritas tertinggi ke terendah:

!important Rule: Aturan CSS yang diakhiri dengan !important akan mengalahkan semua aturan lainnya. Namun, penggunaannya sangat tidak disarankan kecuali dalam keadaan terpaksa karena dapat membuat CSS sulit dikelola.

Contoh: color: blue !important;

Inline Style: CSS yang ditulis langsung pada atribut style di dalam tag HTML.

Contoh: <div style="color: red;"></div>

ID Selector: CSS yang menargetkan elemen berdasarkan id uniknya.

Contoh: #header { color: green; }

Class, Attribute, dan Pseudo-class Selectors: Prioritas di level ini setara.

Class: .button { color: purple; }

Attribute: input[type="text"] { border: 1px solid gray; }

Pseudo-class: a:hover { text-decoration: underline; }

Element dan Pseudo-element Selectors: Menargetkan semua elemen dari jenis tag tertentu. Ini adalah prioritas terendah.

Element: div { font-size: 16px; }

Pseudo-element: p::first-line { font-weight: bold; }

Jika terdapat dua selector dengan prioritas yang sama, maka aturan yang didefinisikan paling akhir di dalam file CSS akan menjadi pemenangnya.

2. Pentingnya Responsive Design
Responsive design adalah konsep penting karena bertujuan untuk membuat halaman web terlihat dan berfungsi dengan baik di berbagai macam perangkat dengan ukuran layar yang berbeda, mulai dari desktop, laptop, tablet, hingga smartphone.

Mengapa ini penting?

Pengalaman Pengguna (User Experience): Situs yang responsif memberikan pengalaman yang nyaman bagi pengguna di perangkat apa pun. Pengguna tidak perlu melakukan zoom-in/zoom-out atau scroll ke samping untuk membaca konten.

Peningkatan Jangkauan Pengguna: Sebagian besar pengguna internet saat ini mengakses web melalui perangkat mobile. Tanpa desain yang responsif, Anda akan kehilangan audiens yang sangat besar.

SEO (Search Engine Optimization): Mesin pencari seperti Google memprioritaskan situs yang mobile-friendly dalam hasil pencariannya. Situs yang tidak responsif akan mendapatkan peringkat yang lebih rendah.

Efisiensi Perawatan: Anda hanya perlu mengelola satu basis kode (codebase) untuk semua perangkat, bukan membuat versi terpisah untuk desktop dan mobile.

Contoh Aplikasi:

   - Sudah Menerapkan (Responsif): YouTube.

      - Alasan: Jika Anda membuka YouTube di desktop, Anda akan melihat video utama dengan daftar video rekomendasi di sampingnya dalam beberapa kolom. Namun, saat dibuka di smartphone, tata letaknya berubah menjadi satu kolom vertikal, dengan komentar dan rekomendasi di bawah video. Ini membuat navigasi dan menonton menjadi mudah di layar kecil.

   - Belum Menerapkan (Tidak Responsif): Situs web akademik atau pemerintah yang sudah tua.

      - Alasan: Seringkali situs-situs lama ini dibuat hanya untuk tampilan desktop. Saat dibuka di smartphone, seluruh halaman akan "menyusut" agar muat di layar. Akibatnya, teks menjadi sangat kecil dan tidak terbaca, dan tombol atau link menjadi sulit untuk ditekan. Pengguna dipaksa untuk terus-menerus memperbesar dan menggeser layar, memberikan pengalaman yang sangat buruk.

## 3. Perbedaan Margin, Border, dan Padding
Ketiganya adalah komponen dari CSS Box Model, yang merupakan kotak yang membungkus setiap elemen HTML.

1. Padding (Bantalan):
Definisi: Ruang transparan yang berada di dalam border, yaitu antara border dan konten elemen (teks/gambar). Fungsinya adalah memberikan ruang bernapas untuk konten di dalam kotaknya.

Implementasi: padding: 20px; atau padding-top: 10px;

2. Border (Garis Tepi):
Definisi: Garis yang mengelilingi padding dan konten. Border bisa memiliki ketebalan, gaya (misalnya solid, dotted), dan warna.

Implementasi: border: 2px solid black;

3. Margin (Jarak):
Definisi: Ruang transparan yang berada di luar border. Fungsinya adalah untuk menciptakan jarak antara elemen tersebut dengan elemen lainnya di sekitarnya.

Implementasi: margin: 15px; atau margin-bottom: 25px;

## 4. Konsep dan Kegunaan Flexbox dan Grid Layout
Keduanya adalah sistem layout modern di CSS untuk mengatur posisi dan tata letak elemen, namun dengan tujuan yang berbeda.

1. Flexbox (Flexible Box Layout)

   - Konsep: Sistem layout satu dimensi. Artinya, Flexbox dirancang untuk mengatur elemen-elemen dalam satu baris (row) atau satu kolom (column). Ia sangat "fleksibel" dalam mendistribusikan ruang dan meratakan item di dalam sebuah kontainer.
   - Kegunaan:
      - Sangat ideal untuk komponen aplikasi skala kecil, seperti membuat navbar, meratakan item di dalam sebuah tombol atau kartu.
      - Memusatkan elemen secara vertikal dan horizontal dengan mudah.
      - Mendistribusikan ruang secara merata di antara beberapa item.

2. Grid Layout

   - Konsep: Sistem layout dua dimensi. Grid memungkinkan kita mengatur    tata letak dalam bentuk baris dan kolom secara bersamaan, seperti sebuah tabel atau spreadsheet. Kita bisa mendefinisikan sebuah "kisi-kisi" dan menempatkan elemen secara presisi di dalamnya.

   - Kegunaan:
      - Sangat cocok untuk tata letak halaman secara keseluruhan (contoh: header, sidebar, konten utama, footer).
      - Membuat layout yang kompleks dan asimetris, seperti galeri foto atau dashboard aplikasi.
      - Mengatur elemen yang perlu sejajar baik secara horizontal maupun vertikal.

---

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

1. Saya memulai dengan membuat fungsi untuk mengedit dan menghapus produk dari etalase.
2. Tak lupa saya juga menampilkan fitur edit dan delete pada cardproduct.
3. Membuat beberapa tampilan html untuk membuat tampilan yang bisa dikostumisasi menggunakan Tailwind.
4. Sebetulnya saya pertama-tama menerapkan semua yang diberikan di tutorial, tetapi saya mengubah beberapa hal.
5. Menambah animasi ketika cursor digerakkan ke arah card.
6. Mengubah seluruh tampilan warna website menjadi darkmode dan menggunakan warna spotlight berupa warna biru.
7. Menambah harga barang pada card.
8. Menambahkan kondisi ketika tidak ada thumbnail maka akan menampilkan no-thumbnail image, begitupun krtika tidak ada produk.
9. Menambahkan navbar untuk keperluan navigasi web dan untuk merapikan susunan web.


</details>