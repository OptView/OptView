"""
This module creates sample data for the model to train on.

The module contains a DataGenerator class
 which can be used to create sample data for the model to train on.
 The data samples are saved in a CSV file for later use.

Example usage:
    generator = DataGenerator()

    # Generate 100 samples for each category
    sample_data = generator.create_sample_data(100)
    generator.save_data()  # Saves the data to 'data_samples.csv'
"""

import random
import csv


class DataGenerator:
    """generates sample data for the model to train on."""

    print("DataGenerator Called")

    def __init__(self):
        """Initializes the DataGenerator with an empty list for data samples"""
        self.data_samples = []

    def create_sample_data(self, data_count):
        """Creates sample data for the model to train on.

        Args:
            data_count (int): The number of data samples to generate
             for each category.

        Returns:
            list: A list of data samples,
             each containing a temperature, humidity,
             IAQ Index, and window state.
        """
        print("\nCreating sample data in process...")
        self._create_comfortable_day_data(data_count)
        self._create_hot_day_data(data_count)
        self._create_polluted_day_data(data_count)
        self._create_high_humidity_day_data(data_count)
        self._create_cold_day_data(data_count)
        print("Finished creating sample data", end="\n\n")
        return self.data_samples

    def save_data(self, filename="data_samples.csv"):
        """Saves the generated data samples to a CSV file.

        Args:
            filename (str): The name of the file where to save the data.
        """
        with open(filename, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Temperature", "Humidity",
                                "IAQ Index", "Window"])
            csvwriter.writerows(self.data_samples)
        print(f"Data samples written to {filename}")

    # Private methods for generating data for different scenarios
    def _create_comfortable_day_data(self, data_count):
        for _ in range(data_count):
            self.data_samples.append([
                round(random.uniform(10.0, 30.0), 2),  # Temperature
                round(random.uniform(0.0, 70.0), 2),  # Humidity
                random.randint(0, 100),  # IAQ Index
                1  # Window Open
            ])

    def _create_hot_day_data(self, data_count):
        for _ in range(data_count):
            self.data_samples.append([
                round(random.uniform(32.0, 55.0), 2),  # Temperature
                round(random.uniform(0.0, 80.0), 2),  # Humidity
                random.randint(0, 100),  # IAQ Index
                0  # Window Closed
            ])

    def _create_polluted_day_data(self, data_count):
        for _ in range(data_count):
            self.data_samples.append([
                round(random.uniform(20.0, 35.0), 2),  # Temperature
                round(random.uniform(20.0, 80.0), 2),  # Humidity
                random.randint(151, 350),  # IAQ Index (unhealthy)
                0  # Window Closed
            ])

    def _create_high_humidity_day_data(self, data_count):
        for _ in range(data_count):
            self.data_samples.append([
                round(random.uniform(22.0, 38.0), 2),  # Temperature
                round(random.uniform(80.0, 100.0), 2),  # Humidity
                random.randint(0, 100),  # IAQ Index
                0  # Window Closed
            ])

    def _create_cold_day_data(self, data_count):
        for _ in range(data_count):
            self.data_samples.append([
                round(random.uniform(-20.0, 5.0), 2),  # Temperature
                round(random.uniform(0.0, 80.0), 2),  # Humidity
                random.randint(0, 100),  # IAQ Index
                0  # Window Closed
            ])
