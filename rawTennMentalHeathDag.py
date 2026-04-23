from airflow import DAG
from datetime import datetime
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

with DAG(
    dag_id = 'raw_tenn_mental_health_dag',
    start_date = datetime(2026,4,23),
    schedule_interval = '@once',
    catchup = False,
    tags = ['estudo']
) as dag:
    
    gcstobigqueryoperator = GCSToBigQueryOperator(
        task_id = 'gcstobigqueryoperator',
        bucket = 'airflow-bucket1-victor',
        source_objects = 'Teen_Mental_Health_Dataset.csv',
        destination_project_dataset_table = 'crack-cogency-355621.raw_airflow.teen_mental_health',
        skip_leading_rows=1,
        autodetect=False,
        write_disposition="WRITE_TRUNCATE",
        gcp_conn_id="google_cloud_default"
    )

    gcstobigqueryoperator