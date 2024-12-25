import qrcode


def generate_qr_code():
    # Input the data for the QR code
    data = input("Enter the data or URL to encode in the QR code: ")

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Size of the QR code (1 = 21x21 matrix, increases with higher numbers)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Thickness of the border (minimum is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image of the QR code
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code to a file
    img.save("qrcode.png")
    print("QR code generated and saved as 'qrcode.png'!")

generate_qr_code()
