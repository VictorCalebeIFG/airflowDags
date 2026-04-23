from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from datetime import datetime

def test_gcs():
    hook = GCSHook(gcp_conn_id="google_cloud_default")
    
    buckets = hook.list("airflow-bucket1-victor")
    print("Buckets/files:", buckets)

with DAG(
    dag_id="test_gcs_access",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="test",
        python_callable=test_gcs
    )