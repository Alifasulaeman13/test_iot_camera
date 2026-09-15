# Soal 2: IoT Camera App

Repositori ini berisi script Python sederhana untuk menjawab Soal 2 dari test Wrapstation.
Tugas utamanya adalah membuat program untuk mengakses kamera (webcam) menggunakan library OpenCV.

Script ini sudah mencakup semua requirement wajib dan bonus (nilai tambah) yang diminta di soal.

## System Specs
Sesuai dengan *Submission Guidelines*:
- OS: Windows
- CPU: Intel Core i7 Gen 14
- RAM: 16 GB
- Storage: SSD 512GB Gen4

## Fitur yang Dibuat
1. **Live Preview**: Kamera akan terbuka di pop-up window secara real-time.
2. **Camera Config (Bonus)**: Ada settingan variabel di script untuk mengatur resolusi (`RESOLUTION_WIDTH`, `RESOLUTION_HEIGHT`) dan exposure/ISO.
3. **Single Capture (Bonus)**: Bisa ambil 1 foto dengan menekan tombol `c`. Fotonya otomatis masuk ke folder `captures/`.
4. **Burst Capture (Bonus)**: Tahan tombol `b` untuk jepret foto berkali-kali secara beruntun sampai tombolnya dilepas.

## Cara Install & Run
Pastikan sudah install OpenCV:
```bash
pip install opencv-python
```

Cara jalankan aplikasinya:
```bash
python camera_app.py
```

**Tombol pintasan (saat kamera terbuka):**
- `c` = Jepret 1 foto
- `b` (tahan) = Jepret foto beruntun (burst mode)
- `q` = Keluar dari aplikasi
