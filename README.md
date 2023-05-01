Sure, here's the readme again:

# Proyecto_Pandas

This project uses the Pandas library in Python to clean and transform a dataset on shark attacks, which can be found in a CSV file named "attacks.csv" in the src folder.

## Requirements

To run the code in this project, you will need the following Python libraries:

- pandas
- numpy

## Installation

To install the required libraries, run the following command in your terminal:

```bash
pip install pandas numpy
```

## Usage

To run the code in this project, follow these steps:

1. Download or clone this repository to your computer.
2. Open the Python file containing the code in your preferred Python IDE.
3. Run the Python file.

The Python file will read the CSV file "attacks.csv" located in the src folder and clean and transform the data using the Pandas library. The results of the data cleaning and transformation will be saved in a new CSV file named "attacks_clean.csv" in the src folder.

## Features

The Python file containing the code performs the following tasks:

1. Removes unnecessary columns from the dataset.
2. Renames the remaining columns to be more descriptive.
3. Removes rows with missing or null values.
4. Adds a column called "timeofday" that classifies the attacks based on the time of day they occurred.
5. Adds a column called "ocean_sea" that classifies the attacks based on the oceanic region where they occurred.
6. Adds a column called "size" that classifies the sharks based on their size.
7. Adds a column called "region" that classifies the attacks based on the geographic region where they occurred.
8. Adds a column called "injury_outcome" that classifies the attacks based on the severity of the injuries they caused.
9. Saves the results of the data cleaning and transformation in a new CSV file named "attacks_clean.csv" in the src folder.

## Data Analysis

Data analysis will be performed in a future update of this project.

## Contributing

Contributions and suggestions to improve this project are welcome.
