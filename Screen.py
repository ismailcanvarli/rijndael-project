import tkinter as tk
from Rijndael import Rijndael

# Rijndael sınıfı, key'in boyutuna göre blok boyutunu belirler.
# 16, 24 veya 32 byte key için blok boyutu sırasıyla 16, 24 veya 32 olur.
def get_block_size(block_size):
    if block_size not in [16, 24, 32]:
        raise ValueError("Invalid block size. Block size must be 16, 24, or 32.")
    return block_size

def encrypt():
    key = key_entry.get()
    block_size = get_block_size(len(key))  # Anahtar uzunluğuna göre blok boyutunu belirle
    r = Rijndael(key, block_size=block_size)
    
    plaintext = text_entry.get()
    # Giriş metnini blok boyutuna uygun hale getir
    if len(plaintext) % block_size != 0:
        # Eğer giriş metni blok boyutuna eşit değilse, dolgu ekle
        plaintext = pad_data(plaintext, block_size)

    ciphertext = r.encrypt(plaintext)
    result_text.insert(tk.END, "Anahtar: " + key + "\n")
    result_text.insert(tk.END, "Metin: " + plaintext + "\n")
    result_text.insert(tk.END, "Şifreli Metin: " + ciphertext + "\n")
    result_text.insert(tk.END, "\n")  # Boş satır ekle

def decrypt():
    key = key_entry.get()
    block_size = get_block_size(len(key))  # Anahtar uzunluğuna göre blok boyutunu belirle
    r = Rijndael(key, block_size=block_size)
    
    ciphertext = text_entry.get()
    plaintext = r.decrypt(ciphertext)
    result_text.insert(tk.END, "Anahtar: " + key + "\n")
    result_text.insert(tk.END, "Şifreli Metin: " + ciphertext + "\n")
    result_text.insert(tk.END, "Çözülmüş Metin: " + plaintext + "\n")
    result_text.insert(tk.END, "\n")  # Boş satır ekle

def pad_data(data, block_size):
    # Dolgu yapılacak bayt sayısı hesaplanır
    padding_size = block_size - len(data) % block_size
    # Her dolgu baytı, dolgu yapılacak bayt sayısına eşit olacak şekilde olur
    padding = chr(padding_size) * padding_size
    # Veriye dolgu eklenir
    padded_data = data + padding
    return padded_data

window = tk.Tk()
window.title("Rijndael Şifreleme (Rijndael Encryption)")
window.geometry("700x700")

# Anahtar giriş alanı
key_label = tk.Label(window, text="Anahtar (Key) 16, 24 veya 32 karakter olmalıdır", font=("Times New Roman", 12))
key_label.pack(pady=5)

# Anahtar girişi için bir Entry oluştur
key_entry = tk.Entry(window, width=50, font=("Times New Roman", 12))
key_entry.pack(pady=15)

# Metin uzunluğunu tutacak bir StringVar oluştur
text_length = tk.StringVar()
text_length.set("Anahtar uzunluğu (Key Size): "+'0')

# Metin uzunluğunu gösterecek bir Label oluştur
length_label = tk.Label(window, textvariable=text_length, font=("Times New Roman", 12))
length_label.pack(pady=5)

# Her tuşa basıldığında metin uzunluğunu güncelle
def update_length(event):
    text_length.set("Anahtar uzunluğu (Key Size): " + str(len(key_entry.get())))

key_entry.bind('<KeyRelease>', update_length)

# Metin giriş alanı
text_label = tk.Label(window, text="Metin (Plain or Chipper text)", font=("Times New Roman", 12))
text_label.pack(pady=5)
text_entry = tk.Entry(window, width=50, font=("Times New Roman", 12))
text_entry.pack(pady=15)

#Encrypt ve Decrypt butonları
encrypt_button = tk.Button(window, text="Şifrele (Encrypt)", command=encrypt, width=20, font=("Times New Roman", 12,"bold"))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Şifre Çöz (Decrypt) ", command=decrypt, width=20, font=("Times New Roman", 12, "bold"))
decrypt_button.pack(pady=5)

result_text = tk.Text(window)
result_text.pack(pady=10)

window.mainloop()