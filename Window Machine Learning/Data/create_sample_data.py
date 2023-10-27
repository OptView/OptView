import random
import csv


data_samples = []

# Comfortable Day (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(20.0, 25.0), 2),  # Temperature
                         round(random.uniform(45.0, 60.0), 2),  # Humidity
                         round(random.uniform(5.0, 10.0), 2),   # UV Light
                         random.randint(20, 50),                 # IAQ Index
                         0,                                      # Fire Sensor
                         1])                                     # Window

# Hot Day (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(28.0, 35.0), 2),  # Temperature
                         round(random.uniform(65.0, 85.0), 2),  # Humidity
                         round(random.uniform(15.0, 20.0), 2),  # UV Light
                         random.randint(50, 100),                # IAQ Index
                         0,                                      # Fire Sensor
                         0])                                     # Window

# Polluted Day (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(20.0, 28.0), 2),  # Temperature
                         round(random.uniform(50.0, 70.0), 2),  # Humidity
                         round(random.uniform(10.0, 15.0), 2),  # UV Light
                         random.randint(100, 150),               # IAQ Index
                         0,                                      # Fire Sensor
                         0])                                     # Window

# Fire Alert (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(20.0, 30.0), 2),  # Temperature
                         round(random.uniform(50.0, 70.0), 2),  # Humidity
                         round(random.uniform(10.0, 15.0), 2),  # UV Light
                         random.randint(200, 250),               # IAQ Index
                         1,                                      # Fire Sensor
                         1])                                     # Window

# Cold Day (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(15.0, 20.0), 2),  # Temperature
                         round(random.uniform(30.0, 45.0), 2),  # Humidity
                         round(random.uniform(5.0, 10.0), 2),   # UV Light
                         random.randint(20, 50),                 # IAQ Index
                         0,                                      # Fire Sensor
                         1])                                     # Window

# Industrial Activity Nearby (20 samples)
for _ in range(20):
    data_samples.append([round(random.uniform(20.0, 28.0), 2),  # Temperature
                         round(random.uniform(50.0, 70.0), 2),  # Humidity
                         round(random.uniform(10.0, 15.0), 2),  # UV Light
                         random.randint(100, 150),               # IAQ Index
                         0,                                      # Fire Sensor
                         0])                                     # Window

# Print the generated samples
for sample in data_samples:
    print(sample)


# Write the generated samples to CSV
with open("data_samples.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Writing the header
    csvwriter.writerow(["Temperature", "Humidity", "UV Light", "IAQ Index", "Fire Sensor", "Window"])
    # Writing the data samples
    csvwriter.writerows(data_samples)

print("Data samples written to data_samples.csv")
