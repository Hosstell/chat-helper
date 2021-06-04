from question_answer_generator.questions.actions import create_action_questions_for_object
from utils.data_utils import get_input_text
from spacy.lang.ru.examples import sentences

text = get_input_text()
# text = sentences[1]


question_answer_set = create_action_questions_for_object(text)


print("text:")
print(text)
print()


for question, answer in question_answer_set:
    print("question:")
    print(question)
    print()

    print("answer:")
    print(answer)
    print()
