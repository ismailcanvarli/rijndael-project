import tkinter as tk
from Rijndael import Rijndael

# Rijndael sınıfı, key'in boyutuna göre blok boyutunu belirler.
# 16, 24 veya 32 byte key için blok boyutu sırasıyla 16, 24 veya 32 olur.
def get_block_size(key):
    length = len(key)
    if length % 16 == 0:
        return 16
    elif length % 24 == 0:
        return 24
    elif length % 32 == 0:
        return 32
    else:
        return 0

def encrypt():
    key = key_entry.get()
    block_size = get_block_size(key)
    r = Rijndael(key, block_size = block_size)
    ciphertext = r.encrypt(text_entry.get())
    result_text.insert(tk.END, "Şifreli Metin: " + ciphertext + "\n")

def decrypt():
    key = key_entry.get()
    block_size = get_block_size(key)
    r = Rijndael(key, block_size = block_size)
    plaintext = r.decrypt(text_entry.get())
    result_text.insert(tk.END, "Çözülmüş Metin: " + plaintext + "\n")

window = tk.Tk()
window.title("Rijndael Şifreleme")
window.geometry("700x700")

key_label = tk.Label(window, text="Anahtar: (Key)", font=("Times New Roman", 12))
key_label.pack(pady=5)
key_entry = tk.Entry(window, width=50, font=("Times New Roman", 12))
key_entry.pack(pady=15)

text_label = tk.Label(window, text="Metin: (Plain or Chipper text)", font=("Times New Roman", 12))
text_label.pack(pady=5)
text_entry = tk.Entry(window, width=50, font=("Times New Roman", 12))
text_entry.pack(pady=15)

encrypt_button = tk.Button(window, text="Şifrele", command=encrypt, width=10, font=("Times New Roman", 12,"bold"))
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Şifre Çöz", command=decrypt, width=10, font=("Times New Roman", 12, "bold"))
decrypt_button.pack(pady=5)

result_text = tk.Text(window)
result_text.pack(pady=10)

window.mainloop()