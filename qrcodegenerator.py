import qrcode #install library d cmd -> pip install qrcode
import image #install libarary di terminal -> pip install image
qr =qrcode.QRCode(
    version = 15,#versi qr code
    box_size = 10, #untuk ukuran qrcode
    border = 5#ukuran putih putih qrcode
)

data = "https://youtu.be/Vz4fB3_JkX0?si=TmiRyNl8C_kFgGZx"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color="white") #seting warna qrcode
img.save("image.jpg")