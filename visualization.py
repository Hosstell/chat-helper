import spacy

from nlp import nlp
from utils.data_utils import get_input_text

input_text = input("Введи предложение, которое вы хотите визуализировать:\n")

if not input_text:
    input_text = get_input_text()

doc = nlp(input_text)

print()
print("Откройте http://localhost:5000")
spacy.displacy.serve(doc, style="dep")