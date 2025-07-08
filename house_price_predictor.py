import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib
import os

# Download dataset if not present
DATA_URL = 'https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv'
DATA_PATH = 'train.csv'
if not os.path.exists(DATA_PATH):
    import urllib.request
    urllib.request.urlretrieve(DATA_URL, DATA_PATH)

# Load data
df = pd.read_csv(DATA_PATH)

# For demonstration, use 'median_house_value' as target if using California housing dataset
if 'SalePrice' in df.columns:
    target = 'SalePrice'
else:
    target = 'median_house_value'

# Drop rows with missing target
df = df.dropna(subset=[target])

# Separate features and target
X = df.drop(target, axis=1)
y = df[target]

# Select numerical and categorical columns
num_cols = X.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_cols = X.select_dtypes(include=['object']).columns.tolist()

# Preprocessing pipelines
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median'))
])
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

# Full pipeline with model
model_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model_pipeline.fit(X_train, y_train)

# Predict and evaluate
y_pred = model_pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Test MSE: {mse:.2f}")
print(f"Test R2: {r2:.2f}")

# Save model
joblib.dump(model_pipeline, 'house_price_model.joblib')
print('Model saved as house_price_model.joblib') 