#%%
import kagglehub
import os
from pathlib import Path

def download_credit_dataset():
    """
    Download the dataset and return the folder path.
    """
    path = kagglehub.dataset_download("uciml/default-of-credit-card-clients-dataset")
    print("Path to dataset files:", path)
    return path

def get_data_path(dataset_dir):
    """
    Return the full path to the data file inside the dataset directory.
    It will detect whether the file is CSV or Excel.
    """
    dataset_dir = Path(dataset_dir)
    # Search for CSV files
    csv_files = list(dataset_dir.glob("*.csv"))
    if csv_files:
        return str(csv_files[0])

    # Search for Excel files
    excel_files = list(dataset_dir.glob("*.xls*"))
    if excel_files:
        return str(excel_files[0])

    raise FileNotFoundError("No CSV/XLS file found in the dataset directory")

# %%
