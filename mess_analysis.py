# mess_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# STEP 1: Load the dataset
df = pd.read_csv("dataset.csv")

# STEP 2: Data preprocessing
# Clean column names in case they have extra spaces
df.columns = df.columns.str.strip()

# Handle mixed date formats in the Date column
df['Date'] = pd.to_datetime(df['Date'], format='mixed', dayfirst=True)

# STEP 3: Basic Exploration
print("\nData Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# STEP 4: Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("graphs/correlation_heatmap.png")

# STEP 5: Crowd vs Time
plt.figure(figsize=(10,4))
sns.lineplot(x='Date', y='Weekly_Crowd', data=df)
plt.title("Weekly Crowd Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/crowd_over_time.png")

# STEP 6: EDA - Individual Factors
sns.boxplot(x='Is_Holiday', y='Weekly_Crowd', data=df)
plt.title("Crowd on Holidays vs Non-Holidays")
plt.savefig("graphs/holiday_vs_crowd.png")

# STEP 7: Prepare data for ML
features = ['Is_Holiday', 'Temperature', 'Menu_Score', 'Event_Intensity_Index', 'Stress_Level']
target = 'Weekly_Crowd'

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# STEP 8: Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print("\nModel MSE:", mse)

# STEP 9: Show model coefficients
coeffs = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
})
print("\nModel Coefficients:\n", coeffs)


