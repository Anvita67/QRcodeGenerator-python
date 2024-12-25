import image;
import qrcode;

qr = qrcode.QRCode(
        version=15,  # Size of the QR code (1 = 21x21 matrix, increases with higher numbers)
        box_size=10,  # Size of each box in the QR code
        border=5,  # Thickness of the border (minimum is 4)
    )

data = "https://www.youtube.com/feed/playlists"

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill = "black", back_color = "White")
img.save("test.png")