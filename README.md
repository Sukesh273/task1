# task1
# README - Iris Dataset Processing Pipeline

## Overview
This project demonstrates a complete data processing pipeline for the Iris dataset using Python and scikit-learn. The pipeline includes data loading, exploration, cleaning, splitting, and preprocessing steps.

## Features
- **Data Loading**: Loads the Iris dataset directly from scikit-learn
- **Data Exploration**: Provides comprehensive statistics and information about the dataset
- **Data Cleaning**: Handles duplicates (though Iris dataset is typically clean)
- **Data Splitting**: Splits data into training and test sets
- **Preprocessing Pipeline**: Standardizes features and handles potential missing values

## Dependencies
- Python 3.x
- pandas
- numpy
- scikit-learn

## Installation
1. Clone this repository
2. Install required packages:
   ```bash
   pip install pandas numpy scikit-learn
   ```

## Usage
Run the main script:
```bash
python task1.py
```

## Functions
1. `load_iris_data()`: Loads the Iris dataset into a pandas DataFrame
2. `explore_data(df)`: Performs initial data exploration and prints statistics
3. `clean_data(df)`: Checks for and removes duplicates
4. `split_data(df)`: Splits data into features (X) and target (y), then into train/test sets
5. `create_preprocessing_pipeline()`: Creates a preprocessing pipeline with imputation and scaling
6. `run_iris_pipeline()`: Executes the complete pipeline and returns processed data

## Output
The script will print:
- Dataset shape and sample rows
- Data types and missing values
- Target distribution
- Summary statistics
- Duplicate information
- Processing results including transformed data shape

## Notes
- The Iris dataset is already clean, so the cleaning functions are included as an example
- The preprocessing pipeline includes steps that would be useful for other datasets with missing values
- Random state is fixed for reproducible results

## Future Enhancements
- Add visualization capabilities
- Extend to handle other datasets
- Include model training and evaluation
