import qrcode

def generate_qr(data, filename="product_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    )

    img.save(filename)

    print(f"QR Code saved as {filename}")


if __name__ == "__main__":
    generate_qr("ProductID:12345;Brand:XYZ;Expiry:2026-12-31")