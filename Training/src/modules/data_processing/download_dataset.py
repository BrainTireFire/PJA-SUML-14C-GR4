"""
Ten moduł pobiera dataset.
"""

import opendatasets as od

def download_dataset(url: str, destination: str) -> None:
    """
    Loads dataset from specified URL and saves it in specified folder.
    """
    od.download(url, destination)
    print('Dataset downloaded and extracted successfully')
