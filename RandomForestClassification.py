from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from dataset import load_dataset


def train_model():

    df = load_dataset()

    X = df[["ProductID", "Brand", "ExpiryValid"]]
    y = df["Authentic"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Model Accuracy:", accuracy_score(y_test, y_pred))

    return model


if __name__ == "__main__":
    train_model()