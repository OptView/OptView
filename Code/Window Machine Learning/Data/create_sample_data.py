import random
import csv


data_samples = []
data_count = 10000000

# Comfortable Day
for _ in range(data_count):
    data_samples.append([round(random.uniform(20.0, 25.0), 2),  # Temperature
                         round(random.uniform(45.0, 60.0), 2),  # Humidity
                         random.randint(20, 50),                 # IAQ Index
                         1])                                     # Window

# Hot Day
for _ in range(data_count):
    data_samples.append([round(random.uniform(30.0, 60.0), 2),  # Temperature
                         round(random.uniform(50.0, 85.0), 2),  # Humidity
                         random.randint(50, 100),                # IAQ Index
                         0])                                     # Window

# Polluted Day
for _ in range(data_count):
    data_samples.append([round(random.uniform(20.0, 28.0), 2),  # Temperature
                         round(random.uniform(50.0, 70.0), 2),  # Humidity
                         random.randint(100, 500),               # IAQ Index
                         0])                                     # Window

# High Humidity Day
for _ in range(20):
    data_samples.append([round(random.uniform(20.0, 30.0), 2),  # Temperature
                         round(random.uniform(80.0, 95.0), 2),  # Humidity
                         random.randint(50, 100),                # IAQ Index
                         1])                                     # Window


# Cold Day (10000 samples)
for _ in range(data_count):
    data_samples.append([round(random.uniform(-50.0, 0.0), 2),  # Temperature
                         round(random.uniform(30.0, 45.0), 2),  # Humidity
                         random.randint(20, 50),                 # IAQ Index
                         1])                                     # Window


# Print the generated samples
for sample in data_samples:
    print(sample)


# Write the generated samples to CSV
with open("data_samples.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Writing the header
    csvwriter.writerow(["Temperature", "Humidity", "IAQ Index", "Window"])
    # Writing the data samples
    csvwriter.writerows(data_samples)

print("Data samples written to data_samples.csv")
