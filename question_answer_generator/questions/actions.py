from morphy.utils import change_form
from nlp import nlp
from utils.data_utils import get_input_text
from utils.spacy_utils import get_all_lefts_and_rights, get_which_word


def create_action_questions_for_object(text):
    doc = nlp(text)
    output_data = []

    for token in doc:
        conditions = all([
            any([
                token.pos_ == "NOUN",
                token.pos_ == "PROPN",
                token.pos_ == "PRON",
            ]),
            any([
                token.dep_ == "nsubj",
                token.dep_ == "nsubj:pass",
            ]),
            token.head.pos_ == "VERB"
        ])
        if conditions:

            def stop(token_):
                condition = any([
                    token_.pos_ == "VERB" and token_.dep_ != "ROOT",
                    any([
                        token_.dep_ == "nsubj",
                        token_.dep_ == "nsubj:pass",
                    ])
                ])
                return condition

            answer = get_all_lefts_and_rights(token.head, [], stop)
            answer = list(filter(lambda x: x != token, answer))
            answer = list(filter(lambda x: x.pos_ != "PUNCT", answer))
            answer = list(filter(lambda x: x.pos_ != "SCONJ", answer))
            answer = list(map(get_which_word, answer))
            answer = list(map(lambda x: x.text, answer))
            answer = " ".join(answer)

            token_name = get_all_lefts_and_rights(token, [])
            token_name = list(map(get_which_word, token_name))
            token_name = list(map(lambda x: x.text, token_name))
            token_name = " ".join(token_name)

            question_do = change_form("делать", token.head.text)
            output_data.append([
                f"Что {question_do} {token_name.lower()}?",
                answer.capitalize()
            ])

    return output_data


def create_adjective_questions_for_object(text):
    doc = nlp(text)
    output_data = []

    for token in doc:
        conditions = all([
            token.dep_ == 'amod'
        ])
        if conditions:
            question_text = token.head.text
            question_word = change_form("Какой", question_text)

            children = list(token.head.children)
            if len(children) > 0 and children[0].dep_ == 'case':
                question = f"{children[0].text.capitalize()} {question_word.lower()} {question_text}?"
            else:
                question = f"{question_word.capitalize()} {question_text}?"

            answer = change_form(token.text, question_text).capitalize()
            output_data.append([question, answer])

    return output_data


def create_subject_questions_for_object(text):
    doc = nlp(text)
    output_data = []

    for token in doc:
        conditions = all([
            any([
                token.pos_ == "NOUN",
                token.pos_ == "PROPN",
                token.pos_ == "PRON",
            ]),
            any([
                token.dep_ == "nsubj",
                token.dep_ == "nsubj:pass",
                ]),
            token.head.pos_ == "VERB"
        ])
        if conditions:
            def stop(token_):
                condition = any([
                    token == token_
                ])
                return condition

            question = get_all_lefts_and_rights(token.head, [], stop)
            question = list(map(lambda x: x.text, question))
            question = " ".join(question)
            question = f"Кто {question}?"

            answer = token.text.capitalize()

            output_data.append([question, answer])

    return output_data


if __name__ == '__main__':
    sentence = get_input_text()
    result = create_subject_questions_for_object(sentence)
    print(result)
