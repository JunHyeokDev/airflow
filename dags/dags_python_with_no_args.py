from airflow import DAG
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator
#from airflow.operators.python import PythonOperator
from airflow.decorators import task
from common.common_func import regist


with DAG(
    dag_id="dags_python_with_no_args",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2023, 1, 1, tz="Europe/Warsaw"),
    catchup=False,
) as dag:
    
    regist_t1 = PythonOperator(
        task_id="regist_t1",
        python_callable=regist,
        op_args=["홍길동", "남자", "옵션1", "옵션2"],
    )
    
    regist_t2 = PythonOperator(
        task_id="regist_t2",
        python_callable=regist,
        op_kwargs={
            "name": "김영희",
            "gender": "여자",
            "option1": "옵션3",
            "option2": "옵션4"
        }
    )
    regist_t2
    