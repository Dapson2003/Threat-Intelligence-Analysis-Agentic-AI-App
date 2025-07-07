import pandas as pd
import pickle
import os

# Load the model only once (on import)
model_path = os.getenv("MODEL_PATH", "model/Proto76.pkl")
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Expected columns
expected_columns = [
    'severity', 'alert_status', 'log_source', 'tags', 'objectMarking',
    'alert_name', 'sla_mttv', 'hostname', 'endpoint_type', 'os', 'src_ip'
]

def predict_label(input_data: dict) -> str:
    """
    Takes a dictionary with alert data and returns the predicted label.
    
    Args:
        input_data (dict): A dictionary with keys matching expected_columns.

    Returns:
        str: Predicted label
    """
    # Validate input
    for col in expected_columns:
        if col not in input_data:
            raise ValueError(f"Missing required field: {col}")

    # Prepare DataFrame
    df = pd.DataFrame([input_data])[expected_columns].astype(str)
    
    # Predict
    prediction = model.predict(df)
    
    return prediction[0]
