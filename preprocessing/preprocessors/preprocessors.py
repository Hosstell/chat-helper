from morphy.utils import get_morph, change_form
from nlp import nlp
from utils.data_utils import get_input_text
from utils.spacy_utils import get_all_lefts_and_rights


def stop_another_sentence(token):
    return any([
        token.dep_ == "acl:relcl"
    ])

# def get_sub_sentence(sentence):
#     doc = nlp(sentence)
#     output = []
#
#     for token in doc:
#         conditions = all([
#             token.pos_ == "VERB",
#             token.dep_ == "acl:relcl",
#         ])
#
#         print(token.text, token.morph.to_dict().get("Case"))
#
#         if conditions:
#             def stop(token_):
#                 return any([
#                     token_.dep_ == 'nsubj',
#                     token_.dep_ == 'obl',
#                     token_.dep_ == "acl:relcl" and token_ != token
#                 ])
#
#             subj = token.head.text
#             new_sentence = get_all_lefts_and_rights(token, [], stop)
#             new_sentence = list(filter(lambda x: x.dep_ != 'punct', new_sentence))
#             new_sentence = list(map(lambda x: x.text, new_sentence))
#             new_sentence = " ".join(new_sentence)
#             new_sentence = f"{subj.capitalize()} {new_sentence}."
#             output.append(new_sentence)
#
#     return output

def get_sub_sentence_standard(sentence):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            get_morph(token.text).normalized.word == "который",
            token.morph.to_dict().get("Case") == "Nom"
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ == "acl:relcl" and token_ != token,
                    token_ == token
                ])

            # subj = get_all_lefts_and_rights(token.head.head, [], lambda x: x == token.head)
            # subj = list(map(lambda x: x.text, subj))
            # subj = " ".join(subj)
            subj = change_form(token.head.head.text, token.text)

            new_sentence = get_all_lefts_and_rights(token.head, [], stop)
            new_sentence = list(filter(lambda x: x.dep_ != 'punct', new_sentence))
            new_sentence = list(map(lambda x: x.text, new_sentence))
            new_sentence = " ".join(new_sentence)
            new_sentence = f"{subj.capitalize()} {new_sentence}."
            output.append(new_sentence)

    return output


def get_main_sentence(sentence):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            token.dep_ == "ROOT"
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ == "acl:relcl",
                    token_.dep_ == "advcl",
                    token_.dep_ == "conj",
                ])

            new_sentence = get_all_lefts_and_rights(token.head, [], stop)
            if new_sentence and  new_sentence[-1].dep_ == 'punct':
                new_sentence.pop()
            new_sentence = list(map(lambda x: x.text, new_sentence))
            new_sentence = " ".join(new_sentence)
            new_sentence = new_sentence.strip().capitalize() + '.'
            output.append(new_sentence)

    return output


def get_sub_sentence_loc(sentence):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            get_morph(token.text).normalized.word == "который",
            token.morph.to_dict().get("Case") == "Loc"
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ == "acl:relcl" and token_ != token,
                    token_ == token
                ])

            subj = token.head.head.text
            new_sentence = get_all_lefts_and_rights(token.head, [])
            new_sentence = list(filter(lambda x: x.dep_ != 'punct', new_sentence))

            for i in range(len(new_sentence)):
                if new_sentence[i].dep_ == 'obl':
                    new_sentence[i] = change_form(subj, new_sentence[i].text)
                else:
                    new_sentence[i] = new_sentence[i].text

            new_sentence = " ".join(new_sentence)
            new_sentence = f"{new_sentence.capitalize()}."
            output.append(new_sentence)

    return output


# Деепричастие
def get_advcl_sentence(sentence):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            token.dep_ == 'advcl',
            token.head.dep_ == "ROOT",
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ != 'nsubj',
                    token_.head != token.head
                ])

            subj = get_all_lefts_and_rights(token.head, [], stop)
            subj = list(filter(lambda x: x != token.head, subj))
            subj = list(map(lambda x: x.text, subj))
            subj = " ".join(subj)

            new_sentence = get_all_lefts_and_rights(token, [])
            if new_sentence and  new_sentence[-1].dep_ == 'punct':
                new_sentence.pop()
            new_sentence = list(map(lambda x: x.text, new_sentence))
            for i in range(len(new_sentence)):
                if new_sentence[i] == token.text:
                    new_sentence[i] = change_form(new_sentence[i], token.head.text)
            new_sentence = " ".join(new_sentence)

            new_sentence = f"{subj} {new_sentence}.".capitalize()
            output.append(new_sentence)

    return output

# Сложно сочиненные
def get_conj_sentence(sentence: str):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            token.dep_ == 'conj',
            token.head.dep_ == "ROOT",
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ != 'nsubj',
                    token_.head != token.head
                ])

            subj = get_all_lefts_and_rights(token.head, [], stop)
            subj = list(filter(lambda x: x != token.head, subj))
            subj = get_all_lefts_and_rights(subj[0], [])
            subj = list(map(lambda x: x.text, subj))
            subj = " ".join(subj)


            new_sentence = get_all_lefts_and_rights(token, [])
            if new_sentence and  new_sentence[-1].dep_ == 'punct':
                new_sentence.pop()
            new_sentence = list(filter(lambda x: x.dep_ != 'punct', new_sentence))
            new_sentence = list(filter(lambda x: x.dep_ != 'cc', new_sentence))
            new_sentence = list(map(lambda x: x.text, new_sentence))
            new_sentence = " ".join(new_sentence)

            new_sentence = f"{subj} {new_sentence}.".capitalize()
            output.append(new_sentence)

    return output

# Сложно сочиненное. Пример: Помнил он, что мать ездила в троицу к обедне.
def get_ccomp_sentence(sentence):
    doc = nlp(sentence)
    output = []

    for token in doc:
        conditions = all([
            token.dep_ == 'ccomp',
            token.head.dep_ == "ROOT",
        ])

        if conditions:
            def stop(token_):
                return any([
                    token_.dep_ == 'mark',
                    token_.dep_ == 'punct',
                    stop_another_sentence(token_)
                ])

            new_sentence = get_all_lefts_and_rights(token, [], stop)
            new_sentence = list(map(lambda x: x.text, new_sentence))
            new_sentence = " ".join(new_sentence).capitalize()
            output.append(new_sentence)
    return output

if __name__ == '__main__':
    sentences = nlp(get_input_text()).sents
    # sentences = nlp("Но пока он об этом размышлял, перевозчик заметил другого путника, который не мог перебраться через реку, бросился к нему и переправил этого тоже.").sents
    sentences = nlp("Яблоко оказалось вкусным, так как в нем был червяк.").sents

    for sentence in sentences:
        sentence = sentence.text
        result = []
        print(sentence)
        result.extend(get_advcl_sentence(sentence))
        # result.extend(get_ccomp_sentence(sentence))
        # result.extend(get_conj_sentence(sentence))
        # result.extend(get_sub_sentence_standard(sentence))
        # result.extend(get_main_sentence(sentence))
        # result.extend(get_sub_sentence_loc(sentence))
        print(result)
        print()

