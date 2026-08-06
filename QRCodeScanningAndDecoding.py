import cv2

def scan_qr(filename="product_qr.png"):
    img = cv2.imread(filename)

    detector = cv2.QRCodeDetector()

    data, bbox, _ = detector.detectAndDecode(img)

    if data:
        print("QR Code Data:", data)
        return data
    else:
        print("No QR Code detected")
        return None


if __name__ == "__main__":
    scan_qr("product_qr.png")