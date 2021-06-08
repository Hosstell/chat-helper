import spacy

from morphy.utils import get_norm_form


def get_all_children(token, first_time=True):
    output = []
    if not first_time:
        output.append(token)
    for child_token in token.children:
        output.extend(get_all_children(child_token, first_time=False))
    return output


def get_all_lefts_and_rights(token, state, stop = None):
    for left in token.lefts:
        state = get_all_lefts_and_rights_with_check(left, state, stop)

    state.append(token)

    for right in token.rights:
        state = get_all_lefts_and_rights_with_check(right, state, stop)

    return state


def get_all_lefts_and_rights_with_check(token, state, stop = None):
    if stop and stop(token):
        return state

    return get_all_lefts_and_rights(token, state, stop)


def get_which_word(token):
    if get_norm_form(token.text) == "который":
        return token.head.head
    return token


if __name__ == '__main__':
    nlp = spacy.load("ru_core_news_md")
    doc = nlp("Я сделал это просто так")
    print(get_all_lefts_and_rights(doc[1], []))
