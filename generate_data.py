import pandas as pd
import random

times = ["Morning", "Afternoon", "Evening", "Night"]
weathers = ["Clear", "Rain"]
traffic_levels = ["Low", "Medium", "High"]
days = ["Weekday", "Weekend"]

data = []

for _ in range(500):

    time = random.choice(times)
    weather = random.choice(weathers)
    traffic = random.choice(traffic_levels)
    day = random.choice(days)

    # Delay logic with randomness
    delay_probability = 0

    # Weather effect
    if weather == "Rain":
        delay_probability += 40

    # Traffic effect
    if traffic == "High":
        delay_probability += 40
    elif traffic == "Medium":
        delay_probability += 20

    # Peak hours
    if time in ["Morning", "Evening"]:
        delay_probability += 15

    # Weekday traffic
    if day == "Weekday":
        delay_probability += 10

    # Randomness
    delay_probability += random.randint(-15, 15)

    # Final decision
    delay = "Yes" if delay_probability >= 50 else "No"

    data.append([
        time,
        weather,
        traffic,
        day,
        delay
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Time",
    "Weather",
    "Traffic",
    "Day",
    "Delay"
])

# Save CSV
df.to_csv("transit_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())