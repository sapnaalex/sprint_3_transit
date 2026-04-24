import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import pickle

print("Running model training...")

# Load dataset
data = pd.read_csv("transit_data.csv")

# Encode categorical data
le_time = LabelEncoder()
le_weather = LabelEncoder()
le_delay = LabelEncoder()

data['Time'] = le_time.fit_transform(data['Time'])
data['Weather'] = le_weather.fit_transform(data['Weather'])
data['Delay'] = le_delay.fit_transform(data['Delay'])

# Features and target
X = data[['Time', 'Weather']]
y = data['Delay']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save model and encoders
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(le_time, open("time_encoder.pkl", "wb"))
pickle.dump(le_weather, open("weather_encoder.pkl", "wb"))
pickle.dump(le_delay, open("delay_encoder.pkl", "wb"))

print("Model trained and saved successfully!")