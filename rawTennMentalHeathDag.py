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
        gcp_conn_id="google_cloud_default",
        schema_fields = [
            {"name": "age", "type": "INTEGER"},
            {"name": "gender", "type": "STRING"},
            {"name": "daily_social_media_hours", "type": "FLOAT"},
            {"name": "platform_usage", "type": "STRING"},
            {"name": "sleep_hours", "type": "FLOAT"},
            {"name": "screen_time_before_sleep", "type": "FLOAT"},
            {"name": "academic_performance", "type": "FLOAT"},
            {"name": "physical_activity", "type": "FLOAT"},
            {"name": "social_interaction_level", "type": "STRING"},
            {"name": "stress_level", "type": "INTEGER"},
            {"name": "anxiety_level", "type": "INTEGER"},
            {"name": "addiction_level", "type": "INTEGER"},
            {"name": "depression_label", "type": "INTEGER"},]
    )

    gcstobigqueryoperator