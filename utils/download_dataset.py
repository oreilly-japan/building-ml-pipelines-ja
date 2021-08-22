"""
Downloads the csv data
"""

import logging
import os

import pandas as pd

# Initial dataset source
DATASET_URL = "http://bit.ly/building-ml-pipelines-dataset"

# Initial local dataset location
LOCAL_FILE_NAME = "data/consumer_complaints_with_narrative.csv"


def download_dataset(url=DATASET_URL):
    """download_dataset downloads the remote dataset to a local path

    Args:
        url (str): complete url path to the csv data source (default: {DATASET_URL})
    """
    df = pd.read_csv(url, index_col=0)
    df.to_csv(LOCAL_FILE_NAME)
    logging.info("Download completed.")


def create_folder():
    """Creates a data folder if it doesn't exist."""
    directory = "data/"
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info("Data folder created.")
    else:
        logging.info("Data folder already existed.")


def check_execution_path():
    """Check if the function and all subsequent functions
        are executed from the root of the project

    Returns:
        bool: returns False if execution path isn't the root, otherwise True
    """
    file_name = "LICENSE"
    if not os.path.exists(file_name):
        logging.error(
            "Don't execute the script from a sub-directory. "
            "Switch to the root of the project folder"
        )
        return False
    return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Started download script")

    if check_execution_path():
        create_folder()
        download_dataset()

    logging.info("Finished download script")
