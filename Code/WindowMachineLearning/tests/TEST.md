# Code Coverage Instructions

Follow these steps to measure the code coverage of the Python programs in this project:


## Installation

1. **Install Required Packages**:
   Ensure that all required packages are installed by running:


```shell
pip install -r requirements.txt
```


## Running Coverage

2. **Navigate to Project Root**:
Change to the root directory of the project:

```shell
cd path/to/WindowMachineLearning
```


3. **Run Coverage**:
Execute the following command to start the coverage measurement:
```shell
coverage run -m unittest discover -s tests

# coverage run -m unittest tests.data_training.test_model_prediction

# python -m unittest tests.data_training.test_model_prediction
```


## Reporting

4. **Generate Coverage Report**:
To generate a coverage report in the terminal, run:

```shell
coverage report
```


5. **Generate HTML Report**:
For a more detailed report that includes highlighted source files, generate an HTML report using:

```shell
coverage html
```

This will create an `htmlcov` directory containing the report.
