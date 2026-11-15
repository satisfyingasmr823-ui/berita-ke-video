# Berita ke Video Vertikal

Ubah link berita menjadi video vertikal 9:16 untuk Facebook Reels dan YouTube Shorts.
Teks dan gambar diambil dari artikel, naskah dibacakan dengan suara bahasa Indonesia,
dan musik latar dibuat langsung oleh browser sehingga bebas hak cipta.

## Fitur

- Ambil judul, paragraf, dan gambar dari link berita (tombol **Ambil Isi dari Link**)
- Kotak teks terisi otomatis dan bisa diedit sebelum video dibuat
- Tambah gambar dari Wikimedia Commons jika artikel kurang gambar
- Ganti atau hapus gambar tiap slide (dari file atau link)
- Dua format: **bebas** (jumlah poin fleksibel) atau **40 detik** (Hook, Inti, Fakta, Dampak, Penutup)
- Narasi dengan teks yang menyorot kata yang sedang dibacakan
- Pilihan musik latar: Energik, Berita (serius), Santai (ambient), atau tanpa musik
- Rekam dan unduh video 1080×1920 (MP4 jika didukung, jika tidak WebM)

## Cara pakai

### Mode 1: Buka langsung (GitHub Pages)

Halaman bisa dibuka dari `https://USERNAME.github.io/NAMA-REPO/`.
Pengambilan isi link memakai layanan proxy publik, yang kadang gagal.
Jika gagal, tempel teks berita secara manual di kotak "Teks berita".

### Mode 2: Jalankan lokal (disarankan)

Mode ini paling andal karena pengambilan link berjalan dari komputermu sendiri.

1. Pastikan Python 3 terpasang.
2. Di folder ini, jalankan `python server.py` (Windows: `py server.py`).
3. Buka http://127.0.0.1:8000 di Chrome atau Edge.

## Merekam video

1. Pilih format dan gaya musik, lalu klik **Buat Video Otomatis**.
2. Klik **Rekam & Unduh**.
3. Pada jendela berbagi, pilih tab ini dan centang **Bagikan audio tab**.
   Suara narasi dan musik ikut terekam.
4. Jangan pindah tab selama rekaman berlangsung.

Rekaman hanya bisa dibuat di Chrome atau Edge.

## Catatan hak cipta

- Musik latar dibuat oleh kode di halaman ini, tidak memakai file audio pihak lain.
- Gambar dari Wikimedia Commons punya lisensi masing-masing. Cek syaratnya, terutama atribusi.
- Teks berita tetap milik sumbernya. Tulis ulang dengan kata-katamu sendiri dan cantumkan sumber.

## Struktur

- `index.html`: aplikasi lengkap (satu file, tanpa instalasi)
- `server.py`: server lokal opsional untuk mengambil isi link tanpa batasan CORS
- `.nojekyll`: memberi tahu GitHub Pages agar file dibaca apa adanya
