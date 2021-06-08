from question_answer_generator.QuestionAnswerGenerator import QuestionAnswerGenerator
from question_answer_generator.questions.actions import create_action_questions_for_object, \
    create_adjective_questions_for_object
from utils.data_utils import get_input_text
from spacy.lang.ru.examples import sentences

# sentences = [ get_input_text() ]
sentences = sentences
# sentences = [sentences[0]]
# print(sentences)


for sentence in sentences:
    print('/// ' + sentence)
    question_answer_set = QuestionAnswerGenerator.generate([sentence])
    for i, (question, answer) in enumerate(question_answer_set):
        print(f"{i+1}.\t{question}")
        print(f"\t{answer}")
        print()