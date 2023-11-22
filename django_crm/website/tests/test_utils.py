import pathlib
import json
import os
from csv import reader


def load_data(file):
    file = pathlib.Path(f"{os.getcwd()}/website/tests/test_data/{file}")
    with open(file) as f:
        data = json.load(f)

    return data


def csv_to_list_of_tuples(file):
    file = pathlib.Path(f"{os.getcwd()}/website/tests/test_data/{file}")
    with open(file, "r") as csv_file:
        csv_reader = reader(csv_file)
        list_of_tuples = list(map(tuple, csv_reader))

    return list_of_tuples


