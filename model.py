import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
dataset_path = "Dataset.csv"
df = pd.read_csv(dataset_path)

# Data preprocessing
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')  # Convert date
X = df[['CodedDay', 'Zone', 'Weather', 'Temperature']]      # Features
y = df['Traffic']                                           # Target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save model
model_path="models/trained_model.pkl"
os.makedirs("models", exist_ok=True)
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print("✔ Model trained and saved successfully!")

# Feature importance visualization
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
plt.figure(figsize=(8, 6))
feature_importances.sort_values().plot(kind='barh', color='green')
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Feature Importances")
plt.grid(True)
plt.tight_layout()
plt.savefig("models/feature_importance.png")
plt.show()
