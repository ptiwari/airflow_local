"""This module provides the example of creating a dag and tasks."""
from airflow import DAG
from airflow.utils.dates import days_ago
from operators.console_writer import ConsoleWriterOperator
from airflow.operators.python_operator import PythonOperator
from demo_project.demo_task import print_dict_function

from datetime import timedelta
import os

def create_demo_dag():
    """
    Creates a DAG to download a CSV file and print a dictionary.
    
    Returns:
        DAG: The created DAG object.
    """
    airflow_home = os.environ.get("AIRFLOW_HOME")
    
    # Define DAG arguments
    dag_args = {
        'owner': 'airflow',
        'start_date': days_ago(1),
    }
    my_dict = {"key1": "value1", "key2": "value2"}    
    # Create the DAG
    dag = DAG('Demo_dag', default_args=dag_args, schedule_interval=timedelta(days=1))
    
    # Define the task to download the CSV file
    console_operator = ConsoleWriterOperator(
        task_id='console_writer',
        message = "I am a console writer",
        dag=dag,
    )
    
    print_dict_task = PythonOperator(
        task_id='print_dictionary_task',
        python_callable=print_dict_function,
        provide_context=True,
        templates_dict={'my_dict': my_dict},
        dag=dag,
    )

    # Set the task dependencies
    console_operator >> print_dict_task
    
    return dag

# Create the DAG instance
demo_dag = create_demo_dag()
