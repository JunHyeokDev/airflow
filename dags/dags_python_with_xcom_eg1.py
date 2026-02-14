from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.providers.standard.operators.bash import BashOperator
from datetime import timedelta

with DAG (
    dag_id = 'dags_python_with_xcom_eg1',
    schedule= '0 2 * * *',
    start_date=pendulum.datetime(2023, 1, 1, tz='Europe/Warsaw'),
    catchup=False,
) as dag:
    
    @task(task_id='push_xcom_task1')
    def push_xcom_1(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key = 'key1', value = 'value1')
        ti.xcom_push(key = 'key2', value = 'value2')
        print("XCom pushed from push_xcom_task1")
    
    @task(task_id='push_xcom_task2')
    def push_xcom_2(**kwargs):
        ti = kwargs['ti']
        ti.xcom_push(key = 'key3', value = 'value3')
        print("XCom pushed from push_xcom_task2")
        
    @task(task_id='pull_xcom_task')
    def pull_xcom(**kwargs):
        ti = kwargs['ti']
        value1 = ti.xcom_pull(key = 'key1')
        value2 = ti.xcom_pull(key = 'key2')
        value3 = ti.xcom_pull(key = 'key3')
        print(f"XCom pulled values: {value1}, {value2}, {value3}")
        
    push_xcom_1() >> push_xcom_2() >> pull_xcom()