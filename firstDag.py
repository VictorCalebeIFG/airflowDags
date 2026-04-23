from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def firstTask():
    print('hello world !')

with DAG (
    dag_id = 'firstDag',
    start_date = datetime(2026,4,23),
    schedule_interval = '@once',
    catchup = False,
    tags = ['estudo']
) as dag:

    firstTask = PythonOperator(
        task_id = 'firstTask',
        python_callable = firstTask
    )

    firstTask