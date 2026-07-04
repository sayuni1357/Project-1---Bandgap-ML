import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("combined_bandgap_dataset.csv")
print(df.head())

# Convert boolean/categorical columns to numeric if needed
df['magnetic_state'] = df['magnetic_state'].astype(int)

# Define features (X) and target (y)
X = df[['atomic_density', 'fermi energy', 'magnetic_state']]
y = df['band_gap']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² Score:", r2)
print("Mean Squared Error:", mse)

coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print(coefficients)

import matplotlib.pyplot as plt
import numpy as np

# --- Plot 1: Actual vs Predicted Band Gaps ---
plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred, color='royalblue', alpha=0.7, edgecolor='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)  # Ideal line
plt.xlabel("Actual Band Gap (eV)")
plt.ylabel("Predicted Band Gap (eV)")
plt.title("Actual vs Predicted Band Gap")
plt.grid(True)
plt.show()

# --- Plot 2: Residual Plot (Error Analysis) ---
residuals = y_test - y_pred
plt.figure(figsize=(7, 5))
plt.scatter(y_pred, residuals, color='orange', alpha=0.7, edgecolor='k')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel("Predicted Band Gap (eV)")
plt.ylabel("Residuals (Actual - Predicted)")
plt.title("Residual Plot")
plt.grid(True)
plt.show()

# Example: Predict bandgap for a new compound
# Replace the feature values below with real data from your dataset

new_data = {
    'atomic_density': [0.8],
    'fermi energy': [1.2],
    'magnetic_state': [False],
    # ... include all features used in training
}

# Convert to DataFrame (same columns as X)
new_df = pd.DataFrame(new_data)

# Predict using the trained model
predicted_bandgap = model.predict(new_df)

print(f"Predicted Band Gap: {predicted_bandgap[0]:.3f} eV")

