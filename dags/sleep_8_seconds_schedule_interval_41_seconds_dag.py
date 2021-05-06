from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

# DAG that takes longer to execute as compared to it's scheduled interval.
with DAG(
    'sleep-8-seconds-schedule-interval-41-seconds',
    description='Another sleep DAG',
    schedule_interval=timedelta(seconds=41),
    start_date=days_ago(1),
    catchup=False,
    tags=['sleep'],
    max_active_runs=1,
) as dag:
    t1 = BashOperator(
        task_id='sleep',
        bash_command='sleep 8',
    )