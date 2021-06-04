import spacy


def get_all_children(token, first_time=True):
    output = []
    if not first_time:
        output.append(token)
    for child_token in token.children:
        output.extend(get_all_children(child_token, first_time=False))
    return output


def get_all_lefts_and_rights(token, state, filter_ = None):
    if filter_ and not filter_(token):
        return state

    for left in token.lefts:
        state = get_all_lefts_and_rights(left, state)

    state.append(token)

    for right in token.rights:
        state = get_all_lefts_and_rights(right, state)

    return state


if __name__ == '__main__':
    nlp = spacy.load("ru_core_news_md")
    doc = nlp("Я сделал это просто так")
    print(get_all_lefts_and_rights(doc[1], []))