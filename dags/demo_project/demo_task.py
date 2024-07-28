def print_dict_function(**kwargs):
    """The Python function that can be used in Airflow task."""
    my_dict = kwargs['templates_dict']['my_dict']
    print(my_dict)