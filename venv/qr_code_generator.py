import qrcode
from qrcode.image.pil import Image, PilImage
from PIL import Image, ImageDraw


data = input("enter the text or URL: ").strip()
filename = input("enter the filename: ").strip()
if not filename:
    filename = "qr_code.png"
elif not filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
    filename += ".png"

qr = qrcode.QRCode(box_size=100, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename, format="PNG")

print(f"QR code saved as {filename}")
