from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
#from airflow.operators.python import PythonOperator
from airflow.decorators import task



with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(f"Input value: {some_input}")
    
    python_task_1 = print_context("Python Decorator 실행!!!!")
    
    