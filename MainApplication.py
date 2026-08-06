import os

from QRCodeScanningAndDecoding import scan_qr
from RandomForestClassification import train_model
from AuthenticationModule import authenticate_product


# Train Random Forest model
model = train_model()


# Ask user for Product ID
product_id = input("Enter ProductID to check: ")


# QR Code file location
filename = os.path.join("qrcodes", f"qr_product_{product_id}.png")


# Scan QR Code
scanned_data = scan_qr(filename)


if scanned_data:

    print("QR Code Data:", scanned_data)

    # Split QR data
    parts = scanned_data.split(";")

    product_id = int(parts[0].split(":")[1])
    brand = parts[1].split(":")[1]
    expiry_str = parts[2].split(":")[1]


    # Check expiry
    expiry_year = int(expiry_str.split("-")[0])

    if expiry_year >= 2025:
        expiry_valid = 1
    else:
        expiry_valid = 0


    # Authenticate product
    result = authenticate_product(
        model,
        product_id,
        brand,
        expiry_valid
    )


    print(
        f"Authentication Result for Product {product_id}: {result}"
    )