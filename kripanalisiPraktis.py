import string
import sys

# -------------------------------------------------------------------
# Data Frekuensi Huruf dalam Bahasa Indonesia 
# -------------------------------------------------------------------
FREQ_INDONESIAN = {
    'A': 0.197, 'N': 0.117, 'I': 0.088, 'T': 0.083, 'E': 0.068, 
    'R': 0.067, 'U': 0.057, 'K': 0.046, 'M': 0.043, 'S': 0.040, 
    'O': 0.039, 'D': 0.035, 'P': 0.034, 'G': 0.033, 'L': 0.029, 
    'H': 0.027, 'B': 0.024, 'C': 0.022, 'Y': 0.016, 'J': 0.010,
    'W': 0.009, 'F': 0.005, 'V': 0.004, 'Z': 0.002, 'X': 0.001,
    'Q': 0.001
}

# -------------------------------------------------------------------
# Fungsi Enkripsi/Dekripsi Caesar (Dari kode Anda, sudah baik)
# -------------------------------------------------------------------
def caesar_cipher(text, shift):
    """
    Mengenkripsi/mendekripsi teks menggunakan Caesar Cipher.
    Gunakan shift positif untuk enkripsi, shift negatif untuk dekripsi.
    """
    ciphertext = ""
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            ciphertext += shifted_char
        elif 'A' <= char <= 'Z':
            start = ord('A')
            shifted_char = chr(((ord(char) - start + shift) % 26) + start)
            ciphertext += shifted_char
        else:
            # Karakter non-alfabet (spasi, tanda baca, dll.) tidak diubah
            ciphertext += char
    return ciphertext

# -------------------------------------------------------------------
# FUNGSI BARU: Menghitung Skor Fitness (Chi-Kuadrat)
# -------------------------------------------------------------------
def calculate_fitness(text, ref_freq):
    """
    Menghitung skor Chi-Kuadrat untuk teks.
    Skor yang lebih rendah berarti kecocokan yang lebih baik.
    """
    # 1. Bersihkan teks, ubah ke uppercase, dan hitung total huruf
    text_cleaned = ''.join(filter(str.isalpha, text.upper()))
    total_len = len(text_cleaned)
    
    if total_len == 0:
        return sys.float_info.max # Skor terburuk jika tidak ada huruf

    # 2. Hitung jumlah kemunculan (counts) setiap huruf di teks
    observed_counts = {char: 0 for char in string.ascii_uppercase}
    for char in text_cleaned:
        observed_counts[char] += 1
        
    chi_squared_score = 0.0
    
    # 3. Hitung skor Chi-Kuadrat
    for char in string.ascii_uppercase:
        observed = observed_counts[char]
        
        # Frekuensi yang diharapkan (Expected)
        expected_freq = ref_freq.get(char, 0.00001) # Nilai kecil jika tidak ada
        expected = expected_freq * total_len
        
        if expected == 0:
            if observed > 0:
                chi_squared_score += 1000 # Penalti jika ada huruf yg tak terduga
        else:
            # Rumus Chi-Kuadrat: (Observed - Expected)^2 / Expected
            chi_squared_score += ((observed - expected)**2) / expected
            
    return chi_squared_score

# -------------------------------------------------------------------
# FUNGSI IMPROVEMENT: Analisis Kriptanalisis (Pengganti frequency_analysis)
# -------------------------------------------------------------------
def analyze_caesar_cipher(ciphertext):
    """
    Melakukan kriptanalisis pada ciphertext Caesar Cipher
    menggunakan analisis Chi-Kuadrat untuk menemukan kunci terbaik.
    
    Mengembalikan:
    - best_shift (int): Tebakan kunci terbaik (0-25)
    - best_plaintext_guess (str): Hasil dekripsi menggunakan kunci terbaik
    - all_scores (dict): Kamus berisi {kunci: skor} untuk semua 26 kunci
    """
    best_shift = 0
    best_score = sys.float_info.max
    best_plaintext_guess = ""
    
    # Buat dictionary untuk menyimpan semua skor
    all_scores = {}

    print("Menganalisis... Mencoba semua 26 kemungkinan kunci:")

    # 1. Brute Force: Coba semua 26 kemungkinan pergeseran
    for shift_guess in range(26):
        
        # 2. Dekripsi: Dapatkan tebakan plaintext (gunakan shift negatif)
        plaintext_guess = caesar_cipher(ciphertext, -shift_guess)
        
        # 3. Hitung Fitness: Hitung skor Chi-Kuadrat
        current_score = calculate_fitness(plaintext_guess, FREQ_INDONESIAN)
        
        # Simpan skor untuk setiap kunci
        all_scores[shift_guess] = current_score

        # 4. Pilih Kunci Terbaik: Simpan skor terendah
        if current_score < best_score:
            best_score = current_score
            best_shift = shift_guess
            best_plaintext_guess = plaintext_guess

    print(f"Analisis selesai. Skor Chi-Kuadrat terendah: {best_score:,.2f}")
    
    # Kembalikan semua hasil
    return best_shift, best_plaintext_guess, all_scores

# -------------------------------------------------------------------
# FUNGSI MAIN: Disesuaikan untuk laporan detail
# -------------------------------------------------------------------
def main():
    """
    Fungsi utama untuk menjalankan aplikasi.
    """
    try:
        input_filename = input("Masukkan nama file .txt (misal: plaintext.txt): ")
        # 1. Membaca plaintext dari file
        # Menambahkan encoding='utf-8' untuk keamanan
        with open(input_filename, 'r', encoding='utf-8') as file:
            plaintext = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' tidak ditemukan.")
        return
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")
        return
        
    print(f"\nPlaintext berhasil dibaca dari '{input_filename}'.")
    
    if len(plaintext.split()) < 500:
        print(f"PERINGATAN: Teks Anda hanya {len(plaintext.split())} kata.")
        print("Analisis Chi-Kuadrat paling akurat dengan 500+ kata.")

    # 2. Enkripsi plaintext
    try:
        secret_key = int(input("Masukkan Kunci Rahasia untuk enkripsi (angka 1-25): "))
        if not (1 <= secret_key <= 25):
            print("Kunci tidak valid. Menggunakan kunci 7.")
            secret_key = 7
    except ValueError:
        print("Input salah. Menggunakan kunci 7.")
        secret_key = 7

    ciphertext = caesar_cipher(plaintext, secret_key)
    print(f"Plaintext berhasil dienkripsi dengan pergeseran kunci {secret_key}.")
    
    # 3. Analisis frekuensi ciphertext (menggunakan fungsi baru)
    # Fungsi ini tidak tahu 'secret_key'
    # Terima 'all_scores' dari fungsi analisis
    guessed_shift, decrypted_text, all_scores = analyze_caesar_cipher(ciphertext)
    
    # 4. Menghitung akurasi (Laporan untuk Tugas 5)
    clean_original = ''.join(filter(str.isalpha, plaintext.upper()))
    clean_guessed = ''.join(filter(str.isalpha, decrypted_text.upper()))
    
    correct_chars = 0
    total_chars = len(clean_original)
    accuracy = 0.0
    
    if total_chars > 0:
        # Bandingkan karakter per karakter
        for i in range(min(total_chars, len(clean_guessed))):
            if clean_original[i] == clean_guessed[i]:
                correct_chars += 1
        accuracy = (correct_chars / total_chars) * 100

    # 5. Menyimpan hasil analisis ke file output
    output_filename = "analisa_frekuensi_hasil.txt"
    try:
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write("=== Laporan Analisis Frekuensi Cipherteks ===\n\n")
            
            output_file.write("--- Ringkasan Hasil ---\n")
            output_file.write(f"1. Kunci Rahasia Asli     : {secret_key}\n")
            output_file.write(f"2. Tebakan Kunci          : {guessed_shift}\n")
            
            if secret_key == guessed_shift:
                output_file.write("   Hasil Tebakan Kunci: BENAR 🥳\n")
            else:
                output_file.write("   Hasil Tebakan Kunci: SALAH 😥\n")

            output_file.write(f"3. Akurasi Teks Ditebak   : {accuracy:.2f}%\n")
            output_file.write(f"   ({correct_chars} dari {total_chars} karakter alfabet berhasil dikembalikan)\n")
            
            # --- BAGIAN LAPORAN BARU YANG DETAIL ---
            output_file.write("\n\n--- Detail Proses Analisis Chi-Kuadrat (χ²) ---\n")
            output_file.write("Algoritma mencoba semua 26 kemungkinan kunci dekripsi.\n")
            output_file.write("Skor χ² mengukur seberapa 'mirip' hasil dekripsi dengan Bahasa Indonesia.\n")
            output_file.write("SKOR LEBIH RENDAH = LEBIH MIRIP.\n\n")

            # Urutkan skor dari yang terbaik (terendah) ke terburuk (tertinggi)
            sorted_scores = sorted(all_scores.items(), key=lambda item: item[1])

            for shift, score in sorted_scores:
                # Format angka: :2d (lebar 2 digit), :15,.2f (lebar 15, koma, 2 desimal)
                line = f"  - Kunci {shift:2d}: Skor χ² = {score:15,.2f}"
                if shift == guessed_shift:
                    line += "  <-- SKOR TERENDAH (TEBAKAN KUNCI)"
                output_file.write(line + "\n")
            # -----------------------------------------

            output_file.write("\n\n" + ("-" * 40) + "\n\n")
            output_file.write(f"--- Data Teks ---\n\n")
            
            # Hanya tampilkan 1000 karakter pertama agar laporan tidak terlalu besar
            output_file.write(f"1. Cipherteks (Potongan):\n")
            output_file.write(ciphertext[:1000] + "...\n\n")
            
            output_file.write(f"2. Hasil Dekripsi (Tebakan Plaintext):\n")
            output_file.write(decrypted_text + "\n")

        print(f"\nAnalisis selesai! Laporan detail disimpan ke file '{output_filename}'.")
    
    except Exception as e:
        print(f"Terjadi error saat menulis file: {e}")

# Menjalankan fungsi utama jika file ini dieksekusi sebagai script
if __name__ == "__main__":
    main()