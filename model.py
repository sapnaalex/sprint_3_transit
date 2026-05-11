import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

print("Running model training...")

# Load dataset
data = pd.read_csv("transit_data.csv")

# Encoders
le_time = LabelEncoder()
le_weather = LabelEncoder()
le_traffic = LabelEncoder()
le_day = LabelEncoder()
le_delay = LabelEncoder()

# Encode
data['Time'] = le_time.fit_transform(data['Time'])
data['Weather'] = le_weather.fit_transform(data['Weather'])
data['Traffic'] = le_traffic.fit_transform(data['Traffic'])
data['Day'] = le_day.fit_transform(data['Day'])
data['Delay'] = le_delay.fit_transform(data['Delay'])

# Features & target
X = data[['Time', 'Weather', 'Traffic', 'Day']]
y = data['Delay']

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model (better than Decision Tree)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save model & encoders
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le_time, open("time_encoder.pkl", "wb"))
pickle.dump(le_weather, open("weather_encoder.pkl", "wb"))
pickle.dump(le_traffic, open("traffic_encoder.pkl", "wb"))
pickle.dump(le_day, open("day_encoder.pkl", "wb"))
pickle.dump(le_delay, open("delay_encoder.pkl", "wb"))

print("Model trained and saved successfully!")

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
})

print("\nFeature Importance:")
print(feature_importance.sort_values(by='Importance', ascending=False))