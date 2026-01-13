import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "random_forest_model.pkl"
COLS_PATH = BASE_DIR / "feature_columns.pkl"
ENCODER_PATH = BASE_DIR / "encoder.pkl"

_model = None
_feature_columns = None
_encoder = None

def load_artifacts():
    global _model, _feature_columns
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    if _feature_columns is None:
        _feature_columns = joblib.load(COLS_PATH)

def preprocess(payload: dict) -> pd.DataFrame:
    df = pd.DataFrame([payload])

    categorical_cols = ["Fuel_Type", "Seller_Type", "Transmission", "Owner", "Car_Name"]

    # Load encoder
    encoder = joblib.load(ENCODER_PATH)

    # Encode categoricals
    encoded = encoder.transform(df[categorical_cols])
    encoded_cols = encoder.get_feature_names_out(categorical_cols)
    df_encoded = pd.DataFrame(encoded, columns=encoded_cols)

    # Numeric features
    df_numeric = df.drop(categorical_cols, axis=1)

    # Combine
    X = pd.concat([df_numeric, df_encoded], axis=1)

    # Align columns
    for col in _feature_columns:
        if col not in X.columns:
            X[col] = 0

    X = X[_feature_columns]

    return X


def predict_price(payload: dict) -> float:
    load_artifacts()
    X = preprocess(payload)
    pred = _model.predict(X)[0]
    return float(pred)
