from pprint import pprint
from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
#from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_python_show_templates",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1")
    def print_kwargs(**kwargs):
        pprint(kwargs)
    
    python_task_1 = print_kwargs()
    