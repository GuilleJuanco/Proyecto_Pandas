Proyecto_Pandas
This project uses the Pandas library in Python to clean and transform a dataset on shark attacks, which can be found in a CSV file named "attacks.csv" in the src folder.

Requirements
To run the code in this project, you will need the following Python libraries:

pandas
numpy
Installation
To install the required libraries, run the following command in your terminal:
pip install pandas numpy

Usage
To run the code in this project, follow these steps:

Download or clone this repository to your computer.
Open the Python file containing the code in your preferred Python IDE.
Run the Python file.
The Python file will read the CSV file "attacks.csv" located in the src folder and clean and transform the data using the Pandas library.

The results of the data cleaning and transformation will be saved in a new CSV file named "attacks_clean.csv" in the src folder.

Features
The Python file containing the code performs the following tasks:

Removes unnecessary columns from the dataset.
Renames the remaining columns to be more descriptive.
Removes rows with missing or null values.
Adds a column called "timeofday" that classifies the attacks based on the time of day they occurred.
Adds a column called "ocean_sea" that classifies the attacks based on the oceanic region where they occurred.
Adds a column called "size" that classifies the sharks based on their size.
Adds a column called "region" that classifies the attacks based on the geographic region where they occurred.
Adds a column called "injury_outcome" that classifies the attacks based on the severity of the injuries they caused.
Saves the results of the data cleaning and transformation in a new CSV file named "attacks_clean.csv" in the src folder.

Data Analysis
Data analysis will be performed in a future update of this project.

Contributing
Contributions and suggestions to improve this project are welcome.
