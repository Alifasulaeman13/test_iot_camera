import cv2
import time
import os

# ==========================================
# Parameter Kamera [OPSIONAL - Poin Tambahan]
# ==========================================

# Mode koneksi kamera:
# - Jika menggunakan webcam fisik/USB, isi CAMERA_ID (biasanya 0) dan kosongkan DROIDCAM_IP
# - Jika menggunakan DroidCam via WiFi, isi DROIDCAM_IP dengan IP dari aplikasi DroidCam di HP
#   Contoh: DROIDCAM_IP = "192.168.1.5"  -> akan connect ke http://192.168.1.5:4747/video
CAMERA_ID = 0  # Ubah ke 1 jika menggunakan OBS Virtual Camera
DROIDCAM_IP = ""  # Isi dengan IP HP jika menggunakan DroidCam via WiFi (contoh: "192.168.1.5")

# a. Resolusi
RESOLUTION_WIDTH = 640
RESOLUTION_HEIGHT = 480
# b. Shutter Speed (Exposure) & c. ISO (Gain)
# Nilai-nilai ini bergantung pada dukungan hardware kamera Anda.
# Di OpenCV V4L2/DSHOW, exposure biasanya bernilai negatif (cth: -4, -5)
EXPOSURE_VALUE = -4 
ISO_VALUE = 100 

def setup_camera():
    # Jika DROIDCAM_IP diisi, gunakan HTTP video stream langsung (lebih stabil dari virtual driver)
    if DROIDCAM_IP:
        stream_url = f"http://{DROIDCAM_IP}:4747/video"
        print(f"Mencoba koneksi ke DroidCam via IP: {stream_url}")
        cap = cv2.VideoCapture(stream_url)
    else:
        cap = cv2.VideoCapture(CAMERA_ID)
    
    if not cap.isOpened():
        print("Error: Tidak dapat mengakses kamera.")
        return None
    
    # Paksa format video MJPEG agar virtual camera (OBS/DroidCam) terbaca dengan benar
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

    # Warmup: Baca beberapa frame pertama agar kamera selesai inisialisasi
    for _ in range(10):
        cap.read()

    # Terapkan konfigurasi resolusi
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION_HEIGHT)
    
    # Matikan konfigurasi hardware spesifik (Exposure & ISO) 
    # karena virtual camera (seperti DroidCam) sering tidak mendukung fitur ini
    # cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    # cap.set(cv2.CAP_PROP_EXPOSURE, EXPOSURE_VALUE)
    # cap.set(cv2.CAP_PROP_GAIN, ISO_VALUE)
    
    return cap

def main():
    cap = setup_camera()
    if cap is None:
        return
        
    print("========================================")
    print("Live Preview Kamera Berjalan")
    print("- Tekan 'c' untuk Capture (Foto Tunggal)")
    print("- Tahan 'b' untuk Burst Capture (Foto Beruntun)")
    print("- Tekan 'q' untuk Keluar")
    print("========================================")

    # Buat direktori untuk menyimpan hasil foto
    output_dir = "captures"
    os.makedirs(output_dir, exist_ok=True)
    burst_count = 0

    # 1. Live Preview
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal mengambil frame dari kamera.")
            break

        cv2.imshow("IoT & Embedded Systems - Camera", frame)

        # 3. Key Mapping
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'): 
            break
        elif key == ord('c'):
            # Menangkap foto tunggal
            filename = os.path.join(output_dir, f"capture_{int(time.time())}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Foto disimpan: {filename}")
        elif key == ord('b'):
            # 4. Burst Capture [OPSIONAL]
            # OS akan mengirimkan sinyal key 'b' secara terus-menerus saat tombol ditahan
            burst_count += 1
            filename = os.path.join(output_dir, f"burst_{int(time.time()*1000)}_{burst_count}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Burst foto disimpan: {filename}")
        else:
            # Reset hitungan burst jika tombol dilepas
            burst_count = 0 
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
