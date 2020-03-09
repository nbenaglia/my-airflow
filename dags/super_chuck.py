from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_chuck():
    return 'Super Chuck!'

dag = DAG('super_chuck', description='A simple DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2020, 3, 9), catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task', retries=3, dag=dag)

chuck_operator = PythonOperator(task_id='super_chuck', python_callable=print_chuck, dag=dag)

dummy_operator >> chuck_operator
