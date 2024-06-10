"""
Ten moduł pobiera dataset.
"""

import opendatasets as od
 
def download_dataset(url: str, destination: str) -> None:
    """
    Ta funkcja pobiera dataset.
    """
    try:
        od.download(url, destination)
        print('Dataset downloaded and extracted successfully')
    except Exception as e:
        print(f"Error occurred while downloading the dataset: {str(e)}")
