#%%
import pandas as pd
from src import api_kaggle_support as api   # import the file as a module
#%%
try:
    # 1) Download dataset folder
    print("Attempting to download dataset from Kaggle...")
    dataset_dir = api.download_credit_dataset()
    print("Dataset downloaded successfully.")

    # 2) Build data path (CSV or Excel)
    #    The function in api_kaggle_support now automatically detects
    #    if the file is .csv or .xls/.xlsx
    data_path = api.get_data_path(dataset_dir)

    # 3) Load into DataFrame
    #    If it's a CSV, use read_csv; if it's an Excel file, use read_excel.
    #    The ID column is set as the index for easier data manipulation.
    print(f"Loading data from: {data_path}")
    if data_path.endswith(".csv"):
        # The Kaggle CSV has a header on the first row and includes an 'ID' column.
        df_loyalty = pd.read_csv(data_path, index_col='ID')
    else:
        # The original UCI .xls file has headers on the second row and is missing the ID column.
        df_loyalty = pd.read_excel(data_path, header=1)
        # Add 'ID' column to be consistent with the Kaggle CSV and set it as index.
        df_loyalty.insert(0, 'ID', range(1, 1 + len(df_loyalty)))
        df_loyalty = df_loyalty.set_index('ID')

    # 4) Quick check
    print("\nData loaded successfully. Quick check:")
    print("Shape:", df_loyalty.shape)
    print(df_loyalty.head(5))

except Exception as e:
    print(f"An error occurred: {e}")
    print("\n--- Troubleshooting ---")
    print("1. Make sure you have authenticated with Kaggle. The `kagglehub` library requires a `kaggle.json` API token.")
    print("   - You can create one in your Kaggle account settings ('Create New Token').")
    print("   - Place the downloaded `kaggle.json` file in the `~/.kaggle/` directory.")
    print("2. Check your internet connection.")
    print("3. Ensure the dataset exists at 'uciml/default-of-credit-card-clients-dataset' on Kaggle.")

# %%
#%%
# 5) Data Cleaning and Preparation
# Now that the data is loaded, let's perform some initial cleaning based on the dataset's documentation.

if 'df_loyalty' in locals():
    print("\n--- Starting Data Cleaning ---")

    # Standardize column names (e.g., remove dots)
    # The original dataset from Kaggle has 'default.payment.next.month'
    if 'default.payment.next.month' in df_loyalty.columns:
        df_loyalty.rename(columns={'default.payment.next.month': 'default_payment_next_month'}, inplace=True)
        print("Renamed 'default.payment.next.month' to 'default_payment_next_month'.")

    # EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 0,5,6=unknown)
    # Grouping 5 and 6 into the 'unknown' category (0)
    df_loyalty['EDUCATION'] = df_loyalty['EDUCATION'].replace([5, 6], 0)
    print("\nCleaned 'EDUCATION' column. Value counts:")
    print(df_loyalty['EDUCATION'].value_counts())

    # MARRIAGE: (1=married, 2=single, 3=others). Some datasets include 0, which should be 'others'.
    df_loyalty['MARRIAGE'] = df_loyalty['MARRIAGE'].replace(0, 3)
    print("\nCleaned 'MARRIAGE' column. Value counts:")
    print(df_loyalty['MARRIAGE'].value_counts())

    print("\nData cleaning complete. DataFrame is ready for analysis.")
    print(df_loyalty.info())
