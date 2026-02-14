from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
#from airflow.operators.python import PythonOperator
from airflow.decorators import task

with DAG(
    dag_id="dags_python_templates",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    
    
    def python_function1(start_date, end_date, **kwargs):
        print(start_date)
        print(end_date)
    
    python_t1 = PythonOperator(
        task_id = 'python_t1',
        python_callable= python_function1,
        op_kwargs={
            'start_date': '{{ data_interval_start }}',
            'end_date': '{{ data_interval_end }}'
        }
    )
    
    
    
    @task(task_id = 'python_t2')
    def python_function2(**kwargs):
        print(kwargs)
        print(kwargs['data_interval_start'])
        print(kwargs['data_interval_end'])
        
        
    python_function2()