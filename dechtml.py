import urllib.parse
import re


def decrypt_html_from_script(js_html):
    match = re.search(r"unescape\('([^']+)'\)", js_html)
    if match:
        encoded_part = match.group(1)
        decoded_html = urllib.parse.unquote(encoded_part)
        return decoded_html
    else:
        return "❌ Tidak ditemukan unescape() di dalam input."

mande = input("File enc html: ")

# Baca dari file
with open(mande, "r", encoding="utf-8") as f:
    js_html = f.read()

# Dekripsi
decrypted = decrypt_html_from_script(js_html)
print("✅ Hasil Decrypt:\n")
print(decrypted)

# Simpan ke file hasil.html (opsional)
with open("hasil.html", "w", encoding="utf-8") as f:
    f.write(decrypted)

print("hasil decrypt simpan hasil.html")
