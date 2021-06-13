import os

from nlp import nlp


def get_input_text():
    input_file = "../input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return open(os.path.join(current_dir, input_file), "r", encoding="utf8").read()


def get_input_sentences():
    doc = nlp(get_input_text())
    return [sent.text.strip() for sent in doc.sents]


if __name__ == '__main__':
    data = get_input_sentences()

    for item in data:
        print(item)
