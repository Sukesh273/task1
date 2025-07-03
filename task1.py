# import pandas as pd
# import numpy as np
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.impute import SimpleImputer
# from sklearn.pipeline import Pipeline

# # 1. Load the Iris dataset directly from sklearn
# def load_iris_data():
#     """Load Iris dataset from sklearn"""
#     iris = load_iris()
#     df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
#                      columns=iris['feature_names'] + ['target'])
#     return df

# # 2. Data Exploration
# def explore_data(df):
#     """Perform initial data exploration"""
#     print("=== Data Exploration ===")
#     print("\nData Shape:", df.shape)
#     print("\nFirst 5 rows:\n", df.head())
#     print("\nData Types:\n", df.dtypes)
#     print("\nMissing Values:\n", df.isnull().sum())
#     print("\nTarget Distribution:\n", df['target'].value_counts())
#     print("\nSummary Statistics:\n", df.describe())

# # 3. Data Cleaning (Iris dataset is already clean, but we'll include the function)
# def clean_data(df):
#     """Basic data cleaning"""
#     print("\n=== Data Cleaning ===")
#     # Check for duplicates
#     duplicates = df.duplicated().sum()
#     print(f"Number of duplicates found: {duplicates}")
    
#     # Remove duplicates if any
#     if duplicates > 0:
#         df = df.drop_duplicates()
#         print(f"Removed {duplicates} duplicates")
    
#     return df

# # 4. Data Splitting
# def split_data(df, test_size=0.2, random_state=42):
#     """Split data into features and target, then into train and test sets"""
#     X = df.drop('target', axis=1)
#     y = df['target']
    
#     return train_test_split(X, y, test_size=test_size, random_state=random_state)

# # 5. Create Preprocessing Pipeline
# def create_preprocessing_pipeline():
#     """Create preprocessing pipeline for numerical features"""
#     pipeline = Pipeline([
#         ('imputer', SimpleImputer(strategy='mean')),  # Though Iris has no missing values
#         ('scaler', StandardScaler())
#     ])
#     return pipeline

# # 6. Main Pipeline Execution
# def run_iris_pipeline():
#     """Execute the complete Iris data processing pipeline"""
#     # 1. Load data
#     df = load_iris_data()
    
#     # 2. Explore data
#     explore_data(df)
    
#     # 3. Clean data
#     df = clean_data(df)
    
#     # 4. Split data
#     X_train, X_test, y_train, y_test = split_data(df)
    
#     # 5. Create and fit preprocessing pipeline
#     preprocessor = create_preprocessing_pipeline()
#     preprocessor.fit(X_train)
    
#     # 6. Transform data
#     X_train_processed = preprocessor.transform(X_train)
#     X_test_processed = preprocessor.transform(X_test)
    
#     # Print results
#     print("\n=== Processing Results ===")
#     print("\nOriginal Training Data Shape:", X_train.shape)
#     print("Processed Training Data Shape:", X_train_processed.shape)
#     print("\nSample of Processed Data (first row):", X_train_processed[0])
    
#     return X_train_processed, X_test_processed, y_train, y_test, preprocessor

# # Run the pipeline
# if __name__ == "__main__":
#     X_train, X_test, y_train, y_test, pipeline = run_iris_pipeline()