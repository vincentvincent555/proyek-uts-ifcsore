# 🎨 Background Color Setter

Background Color Setter adalah fitur tambahan untuk **Rembg-Fuse** yang memungkinkan Anda mengatur warna background dari gambar yang sudah dihilangkan latar belakangnya (transparan) menjadi warna RGB yang Anda inginkan.

## ✨ Fitur

- 🎯 **Pengaturan RGB Fleksibel** - Atur nilai R, G, B secara terpisah atau gunakan color picker
- 🎨 **Preset Warna** - Warna preset yang siap pakai (White, Black, Red, Green, Blue, Cyan, Magenta, Yellow)
- 🖼️ **UI Intuitif** - Interface yang user-friendly dengan dark theme
- 📂 **Batch Processing** - Proses multiple image sekaligus
- 🚀 **Command Line Support** - Gunakan via terminal untuk automation
- 📊 **Preview Real-time** - Lihat preview warna sebelum processing

## 📋 Persyaratan

- Python 3.11 atau lebih tinggi
- PIL (Pillow)
- NumPy

Instalasi dependencies:

```bash
pip install pillow numpy
```

## 🚀 Cara Penggunaan

### 1. GUI Application (Recommended untuk User Biasa)

Jalankan aplikasi GUI:

```bash
python bg_setter_gui.py
```

**Langkah-langkah:**

1. Buka aplikasi
2. Pilih input image (PNG dengan transparent background)
3. Tentukan output location
4. Pilih warna:
   - Gunakan **Color Picker** untuk memilih warna custom
   - Atau geser sliders RGB untuk mengatur nilai manually
   - Atau klik **Preset Color** untuk warna yang sudah ditentukan
5. Klik **Apply Background Color**
6. Output akan disimpan di location yang ditentukan

### 2. Command Line Interface

Untuk automation atau scripting:

**Syntax:**

```bash
python bg_setter.py <input_image> <output_image> [R] [G] [B]
```

**Contoh:**

```bash
# White background (default)
python bg_setter.py input.png output.png

# Red background
python bg_setter.py input.png output.png 255 0 0

# Green background
python bg_setter.py input.png output.png 0 255 0

# Custom color (RGB: 100, 150, 200)
python bg_setter.py input.png output.png 100 150 200
```

### 3. Gunakan Sebagai Module dalam Python

```python
from bg_setter import BackgroundColorSetter

# Initialize
setter = BackgroundColorSetter()

# Set background color untuk single image
setter.set_background_color(
    input_path='input.png',
    output_path='output.png',
    rgb_color=(255, 0, 0)  # Red
)

# Batch process multiple images
stats = setter.batch_set_background(
    input_dir='./images',
    output_dir='./output',
    rgb_color=(0, 255, 0)  # Green
)

print(f"Processed: {stats['success']} images")
print(f"Failed: {stats['failed']} images")
```

## 📁 File Structure

```
BGSetter/
├── bg_setter.py           # Core logic untuk processing image
├── bg_setter_gui.py       # GUI application
├── README.md              # Dokumentasi (file ini)
└── requirements.txt       # Dependencies list
```

## 🎛️ RGB Color Values

RGB adalah kombinasi dari 3 warna dasar:

- **R (Red)** - Nilai 0-255 untuk intensitas merah
- **G (Green)** - Nilai 0-255 untuk intensitas hijau
- **B (Blue)** - Nilai 0-255 untuk intensitas biru

**Contoh kombinasi:**
| Warna | RGB | Hex |
|-------|-----|-----|
| White | 255, 255, 255 | #FFFFFF |
| Black | 0, 0, 0 | #000000 |
| Red | 255, 0, 0 | #FF0000 |
| Green | 0, 255, 0 | #00FF00 |
| Blue | 0, 0, 255 | #0000FF |
| Yellow | 255, 255, 0 | #FFFF00 |
| Cyan | 0, 255, 255 | #00FFFF |
| Magenta | 255, 0, 255 | #FF00FF |
| Orange | 255, 165, 0 | #FFA500 |
| Purple | 128, 0, 128 | #800080 |
| Gray | 128, 128, 128 | #808080 |

## 💡 Tips & Tricks

1. **untuk hasil terbaik**, gunakan image PNG dengan transparent background yang sudah di-process oleh Rembg
2. **Preview warna sebelum processing** menggunakan color preview di GUI
3. **Gunakan preset colors** untuk warna standar yang sering digunakan
4. **Batch processing** akan menambahkan prefix `bg_colored_` pada nama output file
5. **Quality tidak berkurang** - Proses hanya mengisi area transparent, tidak resize atau compress

## ⚠️ Troubleshooting

### Error: "Input file does not exist"

- Pastikan path input image benar
- Pastikan file ini dalam format PNG

### Error: "Invalid RGB values"

- Nilai RGB harus antara 0-255
- Tidak boleh ada karakter non-numeric

### Error: "Image not in RGBA mode"

- Aplikasi akan otomatis convert ke RGBA
- Jika error masih terjadi, konversi manual ke PNG dengan transparency terlebih dahulu

### GUI tidak bisa dibuka

- Pastikan tkinter sudah terinstall: `pip install tk`
- Pada Linux, install dengan: `sudo apt-get install python3-tk`

## 📝 Workflow Integration

Typical workflow dengan Rembg-Fuse:

1. **Rembg-Fuse** - Remove background dari image → output PNG dengan alpha channel
2. **BGSetter** - Add background color ke PNG yang sudah di-remove bg
3. Export final image dengan background yang solid

```
Original Image
    ↓
[Rembg-Fuse] → Transparent Background
    ↓
[BGSetter] → RGB Background
    ↓
Final Image dengan Solid Background
```

## 🔄 Batch Processing Example

Script untuk batch processing multiple images:

```python
from bg_setter import BackgroundColorSetter
import os

setter = BackgroundColorSetter()

# Process semua PNG di folder 'input' dengan background biru
stats = setter.batch_set_background(
    input_dir='./input',
    output_dir='./output',
    rgb_color=(0, 0, 255)  # Blue
)

print(f"Summary:")
print(f"  Total: {stats['total']}")
print(f"  Success: {stats['success']}")
print(f"  Failed: {stats['failed']}")
if stats['errors']:
    print(f"  Failed files: {', '.join(stats['errors'])}")
```

## 📄 License

MIT License - Copyright (c) 2026

## 🤝 Support

Untuk pertanyaan atau issues, silakan buat GitHub issue di repository utama Rembg-Fuse.

---

**Happy coloring! 🎨**
