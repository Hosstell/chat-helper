from nlp import nlp
from preprocessing.preprocessing import Preprocessor
from question_answer_generator.QuestionAnswerGenerator import QuestionAnswerGenerator
from utils.data_utils import get_input_text

text = get_input_text()

print("Input text:")
for sent in nlp(text).sents:
    print(sent)
print()

sentences = Preprocessor.generate(text)
print("After preprocessing(разделение сложных предложений на более простые):")
for sent in sentences:
    print(sent)
print()


output_file = open("output.txt", "w", encoding="utf8")
for sentence in sentences:
    print('/// ' + sentence)
    question_answer_set = QuestionAnswerGenerator.generate([sentence])
    for i, (question, answer) in enumerate(question_answer_set):
        output_file.write(question + "\n")
        output_file.write(answer + "\n")
        output_file.write("\n")

        print(f"{i+1}.\t{question}")
        print(f"\t{answer}")
        print()

output_file.close()
