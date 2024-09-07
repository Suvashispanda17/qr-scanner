import qrcode as qr

from PIL import Image as ii

QR_text= input("Enter the URL or text to generate a QR code: ")

save_file_name = input("Enter the file name to save the QR code (: image will be saved as .png:): ")

if not save_file_name.endswith('.png'):
    save_file_name += '.png'


ii = qr.make(QR_text)

ii.save(QR_text)

ii.show()

print(f"QR code generated, saved as '{QR_text}', and displayed on screen.")
