import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the data
df = pd.read_csv("Credit rating.csv")

# Define features and target
X = df[['age', 'ed', 'employ', 'address', 'income', 
        'Debt to Income Ratio', 'Credit to Debt Ratio', 'othdebt']]
y = df['BAD']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "credit_model.pkl")
print("✅ Model saved as 'credit_model.pkl'")