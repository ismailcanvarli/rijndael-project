import tkinter as tk
from Rijndael import Rijndael

def encrypt():
    r = Rijndael(key_entry.get(), block_size = 16)
    ciphertext = r.encrypt(text_entry.get())
    result_text.insert(tk.END, "Şifreli Metin: " + ciphertext + "\n")

def decrypt():
    r = Rijndael(key_entry.get(), block_size = 16)
    plaintext = r.decrypt(text_entry.get())
    result_text.insert(tk.END, "Çözülmüş Metin: " + plaintext + "\n")

window = tk.Tk()

key_label = tk.Label(window, text="Anahtar:")
key_label.pack(pady=5)
key_entry = tk.Entry(window, width=50)
key_entry.pack(pady=15)

text_label = tk.Label(window, text="Metin:")
text_label.pack(pady=5)
text_entry = tk.Entry(window, width=50)
text_entry.pack(pady=15)

encrypt_button = tk.Button(window, text="Şifrele", command=encrypt, width=10)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(window, text="Şifre Çöz", command=decrypt, width=10)
decrypt_button.pack(pady=5)

result_text = tk.Text(window)
result_text.pack(pady=10)

window.mainloop()