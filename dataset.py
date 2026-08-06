import pandas as pd

def load_dataset():
    data = {
        "ProductID": [12345, 12346, 12347, 12348],
        "Brand": [1, 1, 0, 1],
        "ExpiryValid": [1, 1, 0, 1],
        "Authentic": [1, 1, 0, 1]
    }

    df = pd.DataFrame(data)

    return df