# import string

# def analyze_caesar_cipher():
#     """Melakukan analisis frekuensi untuk memecahkan sandi Caesar."""
    
#     # Frekuensi huruf di Bahasa Indonesia (berdasarkan data umum)
#     # A, N, I, T, E, R, U, K, M, S adalah yang paling sering
#     freq_indonesian = {
#         'A': 0.197, 'N': 0.117, 'I': 0.088, 'T': 0.083, 'E': 0.068, 
#         'R': 0.067, 'U': 0.057, 'K': 0.046, 'M': 0.043, 'S': 0.040, 
#         'O': 0.039, 'D': 0.035, 'P': 0.034, 'G': 0.033, 'L': 0.029, 
#         'H': 0.027, 'B': 0.024, 'C': 0.022, 'Y': 0.016, 'J': 0.010,
#         'W': 0.009, 'F': 0.005, 'V': 0.004, 'Z': 0.002, 'X': 0.001,
#         'Q': 0.001
#     }

#     # Meminta input dari pengguna
#     ciphertext = input("Masukkan teks tersandi (Caesar): ")
    
#     # Membersihkan teks dari karakter non-alfabetik dan mengubah ke huruf kapital
#     text = ''.join(filter(str.isalpha, ciphertext.upper()))
#     if not text:
#         print("Teks tersandi tidak valid.")
#         return

#     # Menghitung frekuensi huruf pada ciphertext
#     freq_cipher = {char: text.count(char) / len(text) for char in string.ascii_uppercase}
    
#     # Menemukan huruf paling sering di ciphertext
#     most_common_cipher = max(freq_cipher, key=freq_cipher.get)
    
#     # Huruf yang paling sering di Bahasa Indonesia (yaitu 'A')
#     most_common_indonesian = 'A'

#     # Menghitung tebakan pergeseran
#     shift_guess = (ord(most_common_cipher) - ord(most_common_indonesian)) % 26
    
#     print(f"\n--- Hasil Analisis ---")
#     print(f"Huruf paling sering di teks tersandi: {most_common_cipher}")
#     print(f"Tebakan pergeseran kunci: {shift_guess}")
    
#     # Mendekripsi teks dengan tebakan pergeseran
    
#     plaintext = ""
#     for char in ciphertext:
#         if char.isalpha():
#             start = ord('A') if char.isupper() else ord('a')
#             shifted = (ord(char) - start - shift_guess) % 26
#             plaintext += chr(start + shifted)
#         else:
#             plaintext += char
            
#     print(f"Hasil dekripsi: {plaintext}")

# # Menjalankan fungsi
# analyze_caesar_cipher()


import string

# -------------------------------------------------------------------
# Data Frekuensi Huruf dalam Bahasa Indonesia
# Berdasarkan data umum
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
# Fungsi Enkripsi Caesar Cipher
# -------------------------------------------------------------------
def caesar_encrypt(text, shift):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher.
    """
    result = ""
    for char in text:
        # Hanya enkripsi huruf alfabet
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Hitung posisi baru huruf
            shifted_pos = (ord(char) - start + shift) % 26
            result += chr(start + shifted_pos)
        else:
            # Karakter selain huruf tidak diubah
            result += char
    return result

# -------------------------------------------------------------------
# Fungsi Analisis Frekuensi dan Dekripsi Caesar
# -------------------------------------------------------------------
def analyze_caesar_cipher(ciphertext):
    """
    Melakukan analisis frekuensi untuk memecahkan sandi Caesar.
    """
    # Membersihkan teks dari karakter non-alfabetik dan mengubah ke huruf kapital
    text_cleaned = ''.join(filter(str.isalpha, ciphertext.upper()))
    if not text_cleaned:
        return "Teks tersandi tidak valid."

    # Menghitung frekuensi huruf pada ciphertext
    freq_cipher = {char: text_cleaned.count(char) / len(text_cleaned) for char in string.ascii_uppercase}
    
    # Menemukan huruf paling sering di ciphertext
    most_common_cipher = max(freq_cipher, key=freq_cipher.get)
    
    # Asumsi huruf paling sering di Bahasa Indonesia adalah 'A'
    most_common_indonesian = 'A'

    # Menghitung tebakan pergeseran
    shift_guess = (ord(most_common_cipher) - ord(most_common_indonesian)) % 26
    
    print("\n--- Hasil Analisis Frekuensi ---")
    print(f"Huruf paling sering di teks tersandi: {most_common_cipher}")
    print(f"Tebakan pergeseran kunci: {shift_guess}")
    
    # Dekripsi teks dengan tebakan pergeseran
    plaintext_guess = caesar_encrypt(ciphertext, -shift_guess)
    
    print(f"Hasil dekripsi: {plaintext_guess}")
    
    return plaintext_guess

# -------------------------------------------------------------------
# Bagian Utama Program
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("Selamat datang di program demonstrasi Caesar Cipher.")
    print("Program ini akan mengenkripsi teks Anda, lalu memecahkannya.")
    
    # Langkah 1: Pengguna menginput plaintext
    plaintext = input("\nMasukkan teks yang ingin dienkripsi: ")
    
    # Langkah 2: Enkripsi teks dengan pergeseran tertentu
    # Kita gunakan pergeseran 3 sebagai contoh
    shift_value = 3
    ciphertext = caesar_encrypt(plaintext, shift_value)
    
    print(f"\n--- Proses Enkripsi ---")
    print(f"Teks Asli: {plaintext}")
    print(f"Nilai Pergeseran: {shift_value}")
    print(f"Teks Terenkripsi: {ciphertext}")
    
    # Langkah 3: Menganalisis dan mendekripsi ciphertext
    # Fungsi analyze_caesar_cipher akan bekerja tanpa perlu tahu nilai pergeseran
    analyze_caesar_cipher(ciphertext)