import json
from pprint import pprint

def load_data(filepath):
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data

def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    data = load_data("my_json.json")
    pretty_print_json(data)

