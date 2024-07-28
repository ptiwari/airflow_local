from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
import os

class ConsoleWriterOperator(BaseOperator):
    """
    Custom Operator to write a predefined message to the console.
    """
    @apply_defaults
    def __init__(self, message: str, *args, **kwargs) -> None:
        super(ConsoleWriterOperator, self).__init__(*args, **kwargs)
        self.message = message

    def execute(self, context: dict) -> None:
        self.log.info("Writing message to console:")
        self.log.info(self.message)
