from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
    tags=["example", "example2", "example3"],
) as dag:
        bash_t1 = BashOperator(
            task_id="bash_t1",
            bash_command="echo whoami", # 
        )
        
        bash_t2 = BashOperator(
            task_id="bash_t2",
            bash_command="echo $HOST", #
        )
        
        bash_t1 >> bash_t2

