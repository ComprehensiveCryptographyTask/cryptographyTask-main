def enkripsi_caesar(teks, shift):
    """
    Fungsi untuk mengenkripsi teks menggunakan Caesar Cipher.
    """
    hasil_enkripsi = ""
    for char in teks:
        # Hanya enkripsi huruf alfabet
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Hitung posisi baru huruf
            posisi_baru = (ord(char) - start + shift) % 26
            hasil_enkripsi += chr(start + posisi_baru)
        else:
            # Karakter selain huruf tidak diubah
            hasil_enkripsi += char
    return hasil_enkripsi

def dekripsi_caesar(teks, shift):
    """
    Fungsi untuk mendekripsi teks yang dienkripsi menggunakan Caesar Cipher.
    """
    # Dekripsi adalah enkripsi dengan shift negatif
    return enkripsi_caesar(teks, -shift)

# Contoh penggunaan
teks_asli = "halo, ini adalah teks rahasia!"
shift = 4

# Enkripsi
teks_terenkripsi = enkripsi_caesar(teks_asli, shift)
print(f"Teks asli: {teks_asli}")
print(f"Teks terenkripsi: {teks_terenkripsi}")

# Dekripsi
# teks_terdekripsi = dekripsi_caesar(teks_terenkripsi, shift)
# print(f"Teks terdekripsi: {teks_terdekripsi}")
