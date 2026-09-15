# IoT & Embedded Systems (Camera App) - Wrapstation Test Task 2

This repository contains the solution for Task 2 of the Wrapstation Fullstack Developer technical test. It is a Python script that accesses the computer's camera (webcam) using OpenCV.

## Features Included
This script successfully implements **all mandatory requirements** and **all optional bonus features (Nilai Tambah)**:
1. **Live Preview**: Accesses the camera and displays a real-time feed in a pop-up window. (Press `q` to quit).
2. **Camera Configuration (Bonus)**: Easily adjustable variables at the top of the script for `RESOLUTION_WIDTH`, `RESOLUTION_HEIGHT`, `EXPOSURE_VALUE`, and `ISO_VALUE`.
3. **Key Mapping / Single Capture (Bonus)**: Press the `c` key to take a single photo. The image will be saved automatically in the `captures/` directory.
4. **Burst Capture (Bonus)**: Hold down the `b` key to take continuous burst photos until the key is released.

## Requirements
- Python >= 3.8
- `opencv-python`

## 💻 Spesifikasi Sistem (Environment)
Sesuai dengan *Submission Guidelines*, berikut adalah spesifikasi sistem yang digunakan selama pengerjaan tugas ini:
- **OS:** Windows
- **Prosesor:** Intel Core i7 Gen 14
- **RAM:** 16 GB
- **Storage:** SSD 512GB Gen4

## Setup & Installation
Install the required OpenCV library:
```bash
pip install opencv-python
```

## How to Run
Run the main script from your terminal:
```bash
python camera_app.py
```
*(If you are on Windows, you may need to use `py camera_app.py`)*

Once the window opens:
- Press **`c`** to capture a photo.
- Hold **`b`** for burst capture.
- Press **`q`** to close the camera and exit the application.
