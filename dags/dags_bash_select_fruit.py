from airflow import DAG
import pendulum
import datetime
from airflow.providers.standard.operators.bash import BashOperator


with DAG (
    dag_id = "dags_bash_select_fruit",
    schedule= "10 0 * * 6#1",
    start_date=pendulum.datetime(2021, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command = "/opt/airflow/plugins/shell/select_fruit.sh ORANGE",
    )
    
    t2_avokado = BashOperator(
        task_id="t2_avokado",
        bash_command = "/opt/airflow/plugins/shell/select_fruit.sh AVOKADO",
    )
    
    t1_orange >> t2_avokado
    