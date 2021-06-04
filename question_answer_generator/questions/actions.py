import spacy

from utils.spacy_utils import get_all_children, get_all_lefts_and_rights

nlp = spacy.load("ru_core_news_md")


def create_action_questions_for_object(text):
    doc = nlp(text)
    output_data = []

    for token in doc:

        print(token.text, token.pos_, token.dep_)

        conditions = all([
            any([
                token.pos_ == "NOUN",
                token.pos_ == "PROPN",
                token.pos_ == "PRON",
            ]),
            token.dep_ == "nsubj",
            token.head.pos_ == "VERB"
        ])
        if conditions:

            def fitter_:


            children = get_all_lefts_and_rights(token.head, [])
            children = list(filter(lambda x: x != token, children))
            children = list(map(lambda x: x.text, children))
            children = " ".join(children)

            output_data.append([
                f"Что делает {token.text}?",
                children
            ])

    return output_data