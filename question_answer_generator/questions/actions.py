from morphy.utils import change_form, is_animated, is_pron
from nlp import nlp
from utils.data_utils import get_input_text, get_input_sentences
from utils.spacy_utils import get_all_lefts_and_rights, get_which_word, get_all_parents


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
            question_suffix = get_all_parents(token, lambda x: x == token.head)
            if len(question_suffix) and question_suffix[-1].text == '.':
                question_suffix.pop()
            question_suffix = list(map(lambda x: x.text, question_suffix))
            question_suffix = " ".join(question_suffix)
            question_suffix = question_suffix.lower()

            question_text = token.head.text
            question_word = change_form("Какой", question_text)

            children = list(token.head.children)
            if len(children) > 0 and children[0].dep_ == 'case':
                case = children[0].text.capitalize()
                question = f"{case} {question_word.lower()} {question_text} {question_suffix}?"
                answer = change_form(token.text, question_text)
                answer = f"{case} {answer}".capitalize()
            else:
                question = f"{question_word.capitalize()} {question_text} {question_suffix}?"
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
                    token == token_,
                    token.dep_ == 'mark'
                ])
                return condition

            question_word = "Кто" if is_animated(token.text) or is_pron(token.text) else "Что"
            question = get_all_lefts_and_rights(token.head, [], stop)
            if len(question) and question[-1].text == '.':
                question.pop()

            question = list(map(lambda x: x.text, question))
            question = " ".join(question)
            question = question.lower()
            question = f"{question_word} {question}?"

            answer = get_all_lefts_and_rights(token, [])
            answer = list(map(lambda x: x.text, answer))
            answer = " ".join(answer)
            answer = answer.capitalize()

            output_data.append([question, answer])

    return output_data


if __name__ == '__main__':
    # sentences = get_input_sentences()
    sentences = ["Его взгял упал на стол"]
    result = create_subject_questions_for_object(sentences[0])
    print(result)
