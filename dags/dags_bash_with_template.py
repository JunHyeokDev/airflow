from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator


with DAG (
    dag_id = "dags_bash_with_template",
    schedule= "10 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag: 
    
    bash_t1 = BashOperator(
        task_id = "bash_t1",
        bash_command = "echo 'This is Jinja Template : data Interval start : {{ data_interval_start }}'",
        params = {"my_param": "Airflow Template Test"}
    )
    
    bash_t2 = BashOperator(
        task_id = "bash_t2",
        env= {
            'START_DATE': '{{ data_interval_start | ds }}',
            'END_DATE': '{{ data_interval_end | ds }}',
        },
        bash_command= "echo 'Start Date: $START_DATE, End Date: $END_DATE'"
    )
    
    bash_t1 >> bash_t2
    