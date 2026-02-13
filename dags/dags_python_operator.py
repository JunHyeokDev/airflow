from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
#from airflow.operators.python import PythonOperator
import random


with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    def select_fruit():
        fruits = ["apple", "banana", "orange", "avocado"]
        rand_init = random.randint(0,3)
        print(fruits[rand_init])
    
    py_t1 = PythonOperator(
        task_id="py_t1",
        python_callable=select_fruit
    )        
    
    py_t1