import os
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_process_data():
    # Load data from a specified location or path
    data = pd.read_csv("path_to_your_dataset.csv")
    
    # Extract relevant features (e.g., X)
    X = data.drop(["target_column_name"], axis=1)
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, data["target_column_name"], test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

# Example usage:
X_train, X_test, y_train, y_test = load_and_process_data()
