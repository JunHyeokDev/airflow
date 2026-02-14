
from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator

with DAG (
    dag_id = "dags_bash_with_macro_eg2",
    schedule= "10 0 * * 6#2", # 매월 2번째 토요일 00:10에 실행
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    # Start_Date : 2주전 월요일 / End_Date : 2주전 토요일
    bash_task1 = BashOperator(
        task_id = "bash_task1",
        env = {
            'START_DATE' : '{{ data_interval_start.in_timezone("Europe/Warsaw") - macros.timedelta(days=19) | ds }}',
            'END_DATE' : '{{ data_interval_end.in_timezone("Europe/Warsaw") - macros.timedelta(days=14) | ds }}'
        },
        bash_command = 'echo "Start Date: $START_DATE" && echo "End Date: $END_DATE"'
    )