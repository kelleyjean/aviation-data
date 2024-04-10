from google.cloud import bigquery
from BuildTables import BigQueryTableCreator

def build_table(project_id, dataset_id):
    creator = BigQueryTableCreator(project_id, dataset_id)
    creator.create_tables_from_directory("schemas") 
