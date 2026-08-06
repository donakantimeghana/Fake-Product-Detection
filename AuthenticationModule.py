import pandas as pd


def authenticate_product(model, product_id, brand, expiry_valid):

    brands = ["ABC", "FakeBrand", "LMN", "XYZ"]

    try:
        brand_code = int(brand)

    except ValueError:
        brand_code = brands.index(brand)

    input_data = pd.DataFrame(
        [[product_id, brand_code, expiry_valid]],
        columns=["ProductID", "Brand", "ExpiryValid"]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "Genuine Product"
    else:
        return "Fake Product"