import pyshorteners
import qrcode

def shorten_url(url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    return short_url

def generate_qr_code(url, filename='qrcode.png'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    print(f"QR Code generated for shortened URL: {url}")
    img.show()

if __name__ == "__main__":
    original_url = input("Enter the URL to shorten: ")
    
    short_url = shorten_url(original_url)
    print(f"Shortened URL: {short_url}")

    generate_qr_code(short_url)
