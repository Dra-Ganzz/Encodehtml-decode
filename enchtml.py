import urllib.parse
import os

def escape_html_like_api(text):
    # URL encode (tanpa quote_plus, supaya %20 bukan +)
    encoded = urllib.parse.quote(text, safe='')  
    js_wrapper = (
        "<script language='javascript'>"
        f"document.write(unescape('{encoded}'));"
        "</script>"
    )
    return js_wrapper

def main():
    input_file = input(" Input File html > ").strip()

    if not os.path.isfile(input_file):
        print(f"File '{input_file}' tidak ditemukan.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    print("[•] Memproses secara lokal...")
    escaped_js_html = escape_html_like_api(html_content)

    output_file = "hasil_encrypt.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(escaped_js_html)

    print(f"✅ Hasil dibungkus ke JavaScript dan disimpan ke: {output_file}")

if __name__ == "__main__":
    main()
