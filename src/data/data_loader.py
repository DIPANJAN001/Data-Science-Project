import pandas as pd
def load_data(file_path):
    """
    Load data from a CSV file.
    
    Args:
        file_path (str): Path to the data file.

    Returns:
        pd.DataFrame: The loaded data as a DataFrame.
    """
    data = pd.read_excel(file_path)
    return data
