# Rembg-Fuse: Background Removal & Color Customizer

## 🎬 Complete Solution untuk Background Removal & Color Setting

Paket terintegrasi yang menggabungkan:

- **Rembg**: AI-powered background removal untuk DaVinci Resolve Fusion
- **BGSetter**: GUI aplikasi untuk mengatur background color dengan preview real-time

<img width="1918" height="752" alt="Screenshot 2025-08-16 172203" src="https://github.com/user-attachments/assets/bc2019c4-3a2c-426f-a128-e8de8b60f209" />

---

## 📋 Daftar Isi

- [Fitur Rembg](#-fitur-rembg)
- [Fitur BGSetter](#-fitur-bgsetter)
- [Instalasi & Setup](#-instalasi--setup)
- [Cara Menjalankan](#-cara-menjalankan)
- [Workflow Lengkap](#-workflow-rembg--bgsetter)

---

## 🔧 Fitur Rembg

### Fitur Utama

- ✅ **AI-Powered Background Removal** - Menggunakan teknologi U-2-Net dan model AI terbaru untuk menghilangkan background dengan presisi tinggi
- 🎞️ **DaVinci Resolve Fusion Integration** - Plugin native terintegrasi langsung di DaVinci Resolve editor
- 🛠️ **Lightweight Implementation** - Script-based Python + Fuse, mudah diinstal tanpa perlu software tambahan
- 🧩 **Kompatibel** - Bekerja di Free version maupun Studio version DaVinci Resolve 18+
- 🆓 **100% Open Source** - Free dan dapat dimodifikasi sesuai kebutuhan
- 📊 **Real-time Workflow** - Lihat hasil removal langsung di Fusion editor
- 🎯 **Multiple AI Models** - Pilih dari 12+ model AI untuk berbagai keperluan

### Fitur Pendukung

- 🔄 **Automatic Model Download** - Download dan cache model secara otomatis saat pertama kali digunakan
- ⚙️ **Rembg Manager GUI** - Setup wizard yang memandu instalasi tanpa perlu command line
- 💾 **Model Selection** - Pilih model AI sesuai kebutuhan task Anda (u2net, u2netp, isnet, birefnet, dll)
- 🖥️ **GPU Support** - CUDA untuk NVIDIA dan ROCM untuk AMD untuk processing lebih cepat
- 🔧 **Manual Setup Option** - Opsi instalasi manual jika diperlukan troubleshooting
- 📝 **Logging & Debugging** - Console logging di DaVinci Resolve untuk tracking progress dan error
- 🎥 **Batch Processing Ready** - Architecture yang support multiple clips processing
- 🔄 **Model Reloading** - Switch antar model tanpa perlu restart DaVinci Resolve
- 📚 **Comprehensive Documentation** - Wiki dengan troubleshooting guide lengkap
- 🌐 **Community Support** - Repository terbuka untuk kontribusi dan Q&A

---

## 🎨 Fitur BGSetter

### Fitur Utama

- 🖼️ **Real-time Image Preview** - Lihat gambar input (original) dan output (processed) berdampingan secara live
- 🎯 **RGB Color Adjustment** - Atur warna background dengan slider RGB (0-255) dengan kontrol penuh
- 🎨 **Instant Preview Update** - Preview gambar output berubah seketika saat menggeser slider warna tanpa delay
- 💾 **Direct Output Save** - Simpan gambar hasil langsung ke file explorer dengan satu klik tombol
- 🖱️ **Multiple Color Input Methods** - Pilih warna melalui slider RGB, color picker dialog, atau preset buttons

### Fitur Pendukung

- 🎯 **Preset Color Buttons** - 6 warna siap pakai: White, Black, Red, Green, Blue, Yellow untuk quick selection
- 🌈 **Windows Color Picker** - Dialog native untuk memilih warna custom dari unlimited color palette
- 📐 **RGB Value Display** - Real-time display nilai RGB saat ini (0-255) dan format Hex color (#RRGGBB)
- 🏷️ **Image Information** - Tampilkan dimensi gambar (width x height pixels) dan info file
- 📊 **Status Logging** - Log lengkap semua operasi, processing time, dan error messages untuk debugging
- 🔄 **Live Preview Update** - Setiap gerakan slider langsung update preview tanpa wait/refresh
- 💡 **User-Friendly UI** - Interface modern dengan dark theme yang nyaman untuk mata
- ⚡ **Fast Processing** - Processing cepat dengan hasil berkualitas tinggi tanpa kompresi
- 📦 **PNG Support** - Full support PNG format dengan alpha channel (transparency/transparan)
- 🧹 **Clear All** - Reset semua input, preview, dan kembali ke state awal dengan satu tombol
- 🔒 **Prevent Errors** - Validasi input untuk mencegah file mismatch atau invalid operations
- 🎞️ **Batch Processing Ready** - Core logic support multiple images, GUI dapat diperluas untuk batch

---

## 📦 AI Models yang Tersedia di Rembg

| Model                 | Tipe         | Ukuran | Kegunaan                                                      |
| --------------------- | ------------ | ------ | ------------------------------------------------------------- |
| **u2net**             | General      | 168 MB | Segmentasi umum berkualitas tinggi, semua jenis background    |
| **u2netp**            | Lightweight  | 4 MB   | Fast processing dengan resource rendah, ideal untuk real-time |
| **u2net_human_seg**   | Specialized  | 168 MB | Background removal khusus foto manusia/portrait               |
| **u2net_cloth_seg**   | Specialized  | 168 MB | Segmentasi pakaian dan cloth areas                            |
| **isnet-general-use** | General      | 170 MB | Segmentasi general purpose dengan akurasi bagus               |
| **isnet-anime**       | Anime        | 168 MB | Optimized untuk anime-style images dan illustrations          |
| **silueta**           | Silhouette   | 43 MB  | Untuk silhouette, outline, dan shadow effects                 |
| **sam**               | Advanced     | 400 MB | Segment Anything Model - versatile untuk berbagai objek       |
| **birefnet-general**  | High-Quality | 928 MB | Hasil maksimal untuk general use dengan akurasi tertinggi     |
| **birefnet-portrait** | Portrait     | 928 MB | Specialized untuk portrait/wajah dengan detail halus          |
| **ben2-base**         | Efficient    | 213 MB | Background removal yang balance antara speed dan quality      |

---

## ⚙️ Instalasi & Setup

### Prerequisites

- **Python**: 3.8 atau lebih tinggi (recommended: 3.11+)
- **pip**: Package manager (biasanya sudah terinstall dengan Python)
- **OS**: Windows 7+, Linux, atau macOS
- **RAM**: 4GB minimum (8GB recommended untuk model besar)
- **Storage**: 500MB+ untuk model downloads

### Step 1: Download & Setup Project

```bash
# Clone atau download repository
git clone https://github.com/Akascape/Rembg-Fuse.git
cd Rembg-Fuse
```

### Step 2: Install Rembg Dependencies

```bash
# Masuk ke folder Rembg
cd Rembg

# Install rembg package
pip install rembg
```

**Optional - GPU Support:**

- NVIDIA CUDA: `pip install rembg[gpu]`
- AMD ROCM: `pip install rembg[rocm]`

### Step 3: Install BGSetter Dependencies

```bash
# Masuk ke folder BGSetter
cd ../BGSetter

# Install dependencies
pip install -r requirements.txt
```

**Packages yang diinstall:**

- `Pillow >= 10.0.0` - Image processing library
- `NumPy >= 1.24.0` - Numerical computing

### Step 4: (Optional) Setup Rembg untuk DaVinci Resolve

Jika ingin gunakan plugin di DaVinci Resolve:

1. Copy folder `Rembg` ke plugin directory DaVinci Resolve:
   - Windows: `C:\Program Files\DaVinci Resolve\Fusion\Plugins\`
   - Linux: `/opt/DaVinci/Fusion/Plugins/`
   - macOS: `/Applications/DaVinci Resolve/Fusion/Plugins/`

2. Restart DaVinci Resolve

3. Buka Fusion page, cari "Rembg" di node menu (Shift+Spacebar)

---

## 🚀 Cara Menjalankan

### REMBG - 3 Pilihan Setup

#### Pilihan 1️⃣: Automatic Setup (RECOMMENDED - Paling Mudah)

```bash
cd Rembg
python rembg_manager.py
```

**Apa yang terjadi:**

- GUI wizard akan membuka
- Follow step-by-step instructions
- Download model otomatis
- Setup selesai dalam beberapa klik

#### Pilihan 2️⃣: Manual Setup (Untuk Advanced User)

```bash
# Di Python atau Jupyter
import rembg

# Download model u2net
rembg.new_session("u2net")

# Ulangi untuk model lain jika perlu
rembg.new_session("u2netp")
rembg.new_session("birefnet-general")
```

Kemudian tambahkan model names ke `Rembg/models.txt` (satu per line)

#### Pilihan 3️⃣: Direct Use dalam Script Python

```python
from rembg import remove
from PIL import Image

# Buka gambar original
input_img = Image.open("photo.jpg")

# Remove background menggunakan model u2net_human_seg
output_img = remove(input_img, model_name="u2net_human_seg")

# Simpan hasil (dengan alpha channel)
output_img.save("photo_no_background.png")
print("✅ Background removed successfully!")
```

---

### BGSETTER - Jalankan Aplikasi GUI

```bash
cd BGSetter
python bg_setter_gui.py
```

Atau **double-click** file `bg_setter_gui.py`

**GUI akan terbuka dengan:**

- Panel kiri: Control untuk RGB adjustment
- Panel kanan: Preview original image + processed image
- Status log untuk tracking operasi

---

## 🎯 Workflow Rembg → BGSetter

### Workflow Lengkap: Hapus Background & Atur Warna Custom

#### Scenario: Foto Produk → Remove BG → Set Custom Color

**Step 1: Persiapkan Gambar Input**

- Siapkan foto/gambar asli (JPG, PNG, atau format lain)
- Simpan di folder mudah diakses

**Step 2: Remove Background dengan Rembg**

```python
from rembg import remove
from PIL import Image

# Buka gambar original
print("Opening image...")
img = Image.open("product_photo.jpg")

# Hilangkan background
print("Removing background...")
img_no_bg = remove(img, model_name="u2net")

# Simpan hasil (HARUS PNG untuk preserve transparency!)
img_no_bg.save("product_no_bg.png")
print("✅ Step 1 Done: photo_no_bg.png")
```

**Output**: File `product_no_bg.png` dengan background transparan

**Step 3: Jalankan BGSetter**

```bash
cd BGSetter
python bg_setter_gui.py
```

**Step 4: Gunakan BGSetter untuk Set Warna**

1. **Buka Gambar**
   - Klik tombol "Select Input Image"
   - Pilih file `product_no_bg.png`
   - Gambar muncul di panel preview sebelah kiri

2. **Pilih Warna Background**
   - Option A: Geser **RGB Sliders** untuk custom color dengan preview real-time
   - Option B: Klik **"Choose Color"** untuk buka Windows color picker
   - Option C: Klik salah satu **Preset Button** (White, Black, Red, dll)

3. **Lihat Preview Real-time**
   - Panel sebelah kanan akan menampilkan hasil dengan warna yang dipilih
   - Update instantly saat Anda menggeser slider!

4. **Simpan Hasil**
   - Klik **"Save Output Image"**
   - Pilih lokasi penyimpanan
   - Gambar final tersimpan dengan background color custom

**Output**: File PNG final dengan background color sesuai keinginan

**Step 5: Gunakan Gambar Final**

- Import ke DaVinci Resolve untuk video editing
- Atau gunakan di aplikasi lain (Photoshop, web, dll)

---

## 💡 Tips & Tricks

### Rembg Tips:

- ✅ Gunakan `u2net` untuk hasil terbaik (168 MB, processing lebih lama)
- ✅ Gunakan `u2netp` untuk kecepatan (4 MB, lightweight)
- ✅ Gunakan `u2net_human_seg` untuk foto manusia
- ✅ Gunakan GPU support untuk processing 5-10x lebih cepat
- ✅ Try multiple models untuk mendapat hasil terbaik

### BGSetter Tips:

- ✅ Selalu gunakan **PNG input** (dengan transparency/alpha channel)
- ✅ RGB Value: 0 = min, 255 = max brightness
  - 255,255,255 = White
  - 0,0,0 = Black
  - 255,0,0 = Pure Red
- ✅ Gunakan **Preset buttons** untuk quick color selection
- ✅ Gunakan **RGB Sliders** untuk fine-tuning warna
- ✅ Preview update real-time → lihat perubahan langsung tanpa delay!
- ✅ Check RGB display untuk nilai pasti dari warna yang dipilih

### Workflow Best Practices:

1. Rembg untuk remove background → output PNG
2. BGSetter untuk set warna custom → output PNG final
3. Import ke DaVinci Resolve / aplikasi editing lain
4. Atau gunakan multiple BGSetter output dengan warna berbeda untuk variations

---

## 🎞️ Video Demo

[<img src="https://img.youtube.com/vi/Lv8DGq7qbx4/0.jpg" width=40% height=40%>](https://youtu.be/Lv8DGq7qbx4)

---

## 🌱 Project Info

| Aspek                  | Keterangan                                           |
| ---------------------- | ---------------------------------------------------- |
| **Rembg Version**      | 0.3                                                  |
| **BGSetter Version**   | 2.0                                                  |
| **DaVinci Resolve**    | Free or Studio: 18+                                  |
| **Python Requirement** | 3.8 - 3.13                                           |
| **License**            | MIT                                                  |
| **Copyright**          | 2026                                                 |
| **Rembg Author**       | Akash Bora                                           |
| **Rembg Library**      | [Daniel Gatis](https://github.com/danielgatis/rembg) |

---

## 🐞 Troubleshooting

### ModuleNotFoundError: No module named 'rembg'

```bash
pip install rembg
```

### No module named 'PIL' atau 'pillow'

```bash
pip install pillow
```

### Tkinter error (GUI tidak muncul)

- **Windows**: Usually built-in
- **Linux**: `sudo apt-get install python3-tk`
- **macOS**: `brew install python-tk`

### BGSetter preview tidak update

- Pastikan file PNG sudah ter-load dengan benar
- Check input label menunjukkan filename
- Resize window jika canvas terlalu kecil

### Rembg processing sangat lambat

- Install GPU support: `pip install rembg[gpu]`
- Atau gunakan model lebih ringan: `u2netp`

### Memory error saat processing

- Gunakan model lebih ringan/lightweight
- Kurangi ukuran/resolusi gambar input sebelumnya

### DaVinci Resolve tidak menemukan Rembg plugin

- Pastikan folder `Rembg` di lokasi plugin yang benar
- Restart DaVinci Resolve
- Check console untuk error messages

---

## 📂 Struktur Folder Project

```
Rembg-Fuse/
├── README.md                     ← Dokumentasi lengkap (file ini)
├── LICENSE                       ← MIT License
│
├── Rembg/                        ← Background Removal Modul
│   ├── bg_remover.py            ← Core removal logic
│   ├── rembg_manager.py         ← Setup wizard GUI
│   ├── models.txt               ← List model terdownload
│   └── Rembg.fuse               ← Plugin untuk DaVinci Resolve
│
└── BGSetter/                     ← Background Color Setter Modul
    ├── bg_setter_gui.py         ← Main GUI aplikasi (RUN THIS!)
    ├── bg_setter.py             ← Core color setting logic
    ├── requirements.txt         ← Python dependencies
    └── README.md                ← BGSetter documentation
```

---

## 🚀 Quick Start

**Untuk user yang terburu-buru:**

```bash
# 1. Setup BGSetter (3 minutes)
cd BGSetter
pip install -r requirements.txt

# 2. Run aplikasi
python bg_setter_gui.py

# 3. Load image → Atur warna → Save hasil ✅
```

---

## 📚 Full Documentation

- 📖 [BGSetter README](./BGSetter/README.md) - Dokumentasi BGSetter
- 🎬 [Rembg Official Repo](https://github.com/danielgatis/rembg) - Dokumentasi Rembg Library
- 🔧 [Troubleshooting Wiki](https://github.com/Akascape/Rembg-Fuse/wiki/Troubleshooting-Guide) - Panduan troubleshooting

---

## 🤝 Contributing

Kontribusi welcome! Anda dapat:

- 🐛 Report bugs
- 💡 Suggest features
- 📝 Submit pull requests
- 📚 Improve documentation

---

## ❤️ Credits & Support

- **Rembg Plugin**: Akash Bora
- **Rembg Library**: [Daniel Gatis](https://github.com/danielgatis/rembg)
- **BGSetter**: Custom development

**Get more Resolve plugins at [www.akascape.com](https://www.akascape.com) 👈**

---

## 📄 License

MIT License - Lihat file [LICENSE](./LICENSE) untuk detailnya

---

## 🎉 Selesai!

Anda sudah siap menggunakan **Rembg-Fuse**! 🚀

**Next Step**: Buka terminal dan jalankan:

```bash
cd BGSetter
python bg_setter_gui.py
```

**Questions?** Cek troubleshooting section atau baca dokumentasi di folder masing-masing.

---

**Last Updated**: April 2026  
**Status**: Production Ready ✅
