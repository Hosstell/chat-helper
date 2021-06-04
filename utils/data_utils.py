import os


def get_input_text():
    input_file = "../input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(current_dir, input_file), "r", encoding="utf8").read()
