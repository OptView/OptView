import random
import csv


data_samples = []
data_count = 10000000

# Adjusted sample boundaries for smart window model

print("Creating Comfortable Day Data in Process...")
# Comfortable Day
# Temperatures are capped at 28.0°C to avoid the upper uncomfortable range.
for _ in range(data_count):
    data_samples.append([round(random.uniform(10.0, 30.0), 2),  # Temperature
                         round(random.uniform(00.0, 70.0), 2),  # Humidity
                         random.randint(0, 100),                 # IAQ Index (good to moderate air quality)
                         1])                                    # Window Open
print("Finished Creating Comfortable Day Data")

print()

print("Creating Hot Day Data in Process...")
# Hot Day
# Reduced upper temperature limit to reflect more common high temperatures.
for _ in range(data_count):
    data_samples.append([round(random.uniform(32.0, 55.0), 2),  # Temperature
                         round(random.uniform(00.0, 80.0), 2),  # Humidity
                         random.randint(0, 100),                # IAQ Index
                         0])                                    # Window Closed
print("Finished Creating Hot Day Data")

print()

print("Creating Polluted Day Data in Process...")
# Polluted Day
# IAQ Index values adjusted to reflect a more common range for poor air quality.
for _ in range(data_count):
    data_samples.append([round(random.uniform(20.0, 35.0), 2),  # Temperature
                         round(random.uniform(20.0, 80.0), 2),  # Humidity
                         random.randint(151, 350),              # IAQ Index (unhealthy)
                         0])                                    # Window Closed
print("Finished Creating Polluted Day Data")

print()

print("Creating High Humidity Day Data in Process...")
# High Humidity Day
# The temperature range is adjusted to not overlap with the comfortable range.
for _ in range(data_count):
    data_samples.append([round(random.uniform(22.0, 38.0), 2),  # Temperature
                         round(random.uniform(80.0, 100.0), 2), # Humidity
                         random.randint(0, 100),                # IAQ Index
                         0])                                    # Window Closed
print("Finished Creating High Humidity Day Data")

print()

print("Creating Cold Day Data in Process...")
# Cold Day
# The lower limit for temperature is adjusted to a more common cold temperature.
for _ in range(data_count):
    data_samples.append([round(random.uniform(-20.0, 5.0), 2),  # Temperature
                         round(random.uniform(00.0, 80.0), 2),   # Humidity
                         random.randint(0, 100),                  # IAQ Index (good to moderate air quality)
                         0])                                     # Window Closed
print("Finished Creating Cold Day Data")

print()

# Write the generated samples to a new CSV
with open("data_samples.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    # Writing the header
    csvwriter.writerow(["Temperature", "Humidity", "IAQ Index", "Window"])
    # Writing the data samples
    csvwriter.writerows(data_samples)

print("Data samples written to data_samples.csv")
