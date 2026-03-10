import json
import os


def load_test_data(file_name):
    file_path = os.path.join("testdata", file_name)

    with open(file_path) as f:
        data = json.load(f)

    return data