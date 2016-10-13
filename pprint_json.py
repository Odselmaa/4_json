import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    else:
        with open(filepath) as data_file:
            return json.load(data_file)


def pretty_print_json(data):
    return json.dumps(
                    data,
                    indent=4,
                    separators=(',', ': '),
                    ensure_ascii=False
                    )


if __name__ == '__main__':
    try:
        file_path = input("Enter file path: ")
    except ValueError:
        file_path = None

    if file_path is not None:
        data = load_data(file_path)
        pretty_data = pretty_print_json(data)
        print(pretty_data)
