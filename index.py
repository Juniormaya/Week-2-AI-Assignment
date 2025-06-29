import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score

# Placeholder for the actual data loading
data = pd.read_csv('maternal_health_data_kenya.csv')  

# Example features (X) and target variable (y)
# Features might include: 'age', 'number of antenatal visits', 'parity', 'previous complications',
# 'anemia', 'hypertension status', 'diabetes', 'education level', 'distance to health facility'
# target variable could be 'high risk pregnancy' (binary: 0 for low risk or 1 for high risk)
X = data[['age', 'antenatal_visits', 'parity', 'previous_complications',
          'anemia', 'hypertension', 'diabetes', 'education_level', 'distance_to_health_facility']]
y = data['high_risk_pregnancy']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Training the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))
print(f1_score(y_test, y_pred, average='binary'))

# To integrate with a referral system, the model's predictions would trigger alerts for high-risk pregnancies.
