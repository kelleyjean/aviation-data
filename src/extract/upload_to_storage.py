import os
import configparser
from datetime import datetime

from google.cloud import storage
from load.GCSLoader import CloudStorageLoader


config_file_path = os.path.join("credentials", "config.ini")
config = configparser.ConfigParser()
config.read(config_file_path)
project_id = config["GCS"]["project_id"]
bucket_name = config["GCS"]["bucket_name"]


def upload_csv_to_storage(project_id, bucket_name):

    """
    This script uploads all CSV files from a specified folder to a Google Cloud Storage bucket,
    adding a date stamp to each uploaded filename.

    Requirements:
      - Google Cloud SDK with project configured
      - Service account key file with appropriate permissions
      - `google-cloud-storage` library installed

    Instructions:
      1. Edit the `src/config/config.ini` file with your GCS project ID and bucket name.
      2. Place your CSV files in the `src/data` folder.
      3. Run the script.

    """

    # Create a CloudStorageLoader instance
    loader = CloudStorageLoader(project_id, bucket_name)

    data_folder_path = os.path.join("src", "data")
    for filename in os.listdir(data_folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(data_folder_path, filename)

            # Get current date and format it for filename
            date_stamp = datetime.today().strftime("%Y-%m-%d")

            # Construct new filename with date stamp
            new_filename = f"{filename[:-4]}_{date_stamp}.csv"

            # Upload the file with the new filename
            loader.upload_file(file_path, new_filename)
            print(f"File {filename} uploaded as {new_filename} to Google Cloud Storage!")

    print("All CSV files in src/data folder have been uploaded successfully!")