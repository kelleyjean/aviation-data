from google.cloud import bigquery
import configparser
import json
import os

class BigQueryTableCreator:
    def __init__(self, config_file_path, schema_file_path):
        # Read project_id from config.ini
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self.project_id = config["GCS"]["project_id"]

        # Load dataset_id from JSON schema file
        with open(schema_file_path, "r") as f:
            schema_data = json.load(f)
        self.dataset_id = schema_data["dataset_id"]  # Assuming dataset_id exists in JSON file

        # Continue with other initialization steps
        self.client = bigquery.Client(project=self.project_id)
        self.dataset_ref = self.client.dataset(self.dataset_id)

    def load_schema_from_file(self, schema_file_path):
        with open(schema_file_path, "r") as f:
            schema_data = json.load(f)
        return [bigquery.SchemaField(field["name"], field["type"]) for field in schema_data]
    
    def create_tables_from_directory(self, schema_directory):
        for filename in os.listdir(schema_directory):
            if filename.endswith(".json"):  # Assuming JSON schema files
                schema_file_path = os.path.join(schema_directory, filename)
                table_name = os.path.splitext(filename)[0]  # Extract table name from filename
                self.create_table(table_name, schema_file_path)

    def create_table(self, table_name, schema_file_path):
        schema = self.load_schema_from_file(schema_file_path)
        table_ref = self.dataset_ref.table(table_name)
        table = bigquery.Table(table_ref, schema=schema)
        try:
            table = self.client.create_table(table)  # Create the table
            print(f"Table created: {table.full_table_id}")
        except Exception as e:
            print(f"Error creating table: {e}")

