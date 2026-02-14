
from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator
from datetime import timedelta


with DAG (
    dag_id = "dags_bash_with_macro_eg1",
    schedule= "10 0 L * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
    user_defined_macros={'timedelta': timedelta}  # 여기에 등록!
) as dag:
    
    # Start_Date : 전월 말일 / End_Date : 1일전
    bash_task1 = BashOperator(
        task_id = "bash_task1",
        env = {
            'START_DATE' : '{{ data_interval_start.in_timezone("Europe/Warsaw") | ds }}',
            'END_DATE' : '{{ (data_interval_end.in_timezone("Europe/Warsaw") - timedelta(days=1) )| ds}}'
        },
        bash_command = 'echo "Start Date: $START_DATE" && echo "End Date: $END_DATE"'
    )