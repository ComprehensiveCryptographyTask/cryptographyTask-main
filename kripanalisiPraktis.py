def caesar_cipher_encrypt(plaintext, shift):
    """
    Mengenkripsi plaintext menggunakan Caesar Cipher.
    """
    ciphertext = ""
    for char in plaintext:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            ciphertext += shifted_char
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            ciphertext += shifted_char
        else:
            # Keep other characters (spaces, punctuation, etc.) as they are
            ciphertext += char
    return ciphertext

def frequency_analysis(ciphertext):
    """
    Melakukan analisis frekuensi pada ciphertext untuk menebak kunci.
    """
    # Frekuensi huruf paling umum dalam bahasa Inggris (ETAOIN SHRDLU)
    # E adalah huruf yang paling sering muncul
    english_freq_order = 'etaoinsrhdlucmfywgpbvkxqjz'
    
    # Menghitung frekuensi huruf pada ciphertext
    char_freq = {}
    total_letters = 0
    for char in ciphertext:
        if 'a' <= char.lower() <= 'z':
            total_letters += 1
            char = char.lower()
            char_freq[char] = char_freq.get(char, 0) + 1
    
    if not char_freq:
        return "Tidak ada huruf alfabet ditemukan.", None
    
    # Mencari huruf yang paling sering muncul di ciphertext
    most_common_char_in_cipher = max(char_freq, key=char_freq.get)
    
    # Mengasumsikan huruf yang paling sering muncul di cipherteks adalah 'e'
    # 'e' adalah huruf paling umum dalam bahasa Inggris
    # Tentukan pergeseran kunci
    shift_guess = (ord(most_common_char_in_cipher) - ord(english_freq_order[0]) + 26) % 26
    
    return most_common_char_in_cipher, shift_guess

def main():
    """
    Fungsi utama untuk menjalankan aplikasi.
    """
    input_filename = input("Masukkan nama file .txt (misal: plaintext.txt): ")
    output_filename = "analisa_frekuensi_hasil.txt"
    
    # 1. Membaca plaintext dari file
    try:
        with open(input_filename, 'r') as file:
            plaintext = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' tidak ditemukan.")
        return
    
    print("\nPlaintext berhasil dibaca.")

    # 2. Enkripsi plaintext
    # Gunakan pergeseran kunci acak (misal, 3) untuk demonstrasi
    encryption_shift = 3 
    ciphertext = caesar_cipher_encrypt(plaintext, encryption_shift)
    print(f"Plaintext berhasil dienkripsi menjadi ciphertext dengan pergeseran kunci {encryption_shift}.")
    
    # 3. Analisis frekuensi ciphertext
    most_common_char, guessed_shift = frequency_analysis(ciphertext)
    
    # 4. Dekripsi ciphertext dengan tebakan kunci
    if guessed_shift is not None:
        decrypted_text = caesar_cipher_encrypt(ciphertext, 26 - guessed_shift)
    else:
        decrypted_text = "Dekripsi tidak dapat dilakukan."

    # 5. Menyimpan hasil analisis ke file output
    with open(output_filename, 'w') as output_file:
        output_file.write("=== Laporan Analisis Frekuensi Cipherteks ===\n\n")
        output_file.write(f"1. Hasil Cipherteks:\n")
        output_file.write(ciphertext + "\n\n")
        output_file.write("-" * 40 + "\n\n")
        output_file.write(f"2. Hasil Analisis Frekuensi:\n")
        output_file.write(f"   Abjad paling sering digunakan (dalam cipherteks): '{most_common_char.upper()}'\n")
        output_file.write(f"   Tebakan pergeseran kunci (key): {guessed_shift}\n\n")
        output_file.write(f"   Hasil dekripsi:\n")
        output_file.write(decrypted_text + "\n")

    print(f"\nAnalisis selesai! Hasil disimpan ke file '{output_filename}'.")

if __name__ == "__main__":
    main()