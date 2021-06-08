import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang="ru")


def change_form(target: str, source: str) -> str:
    fields = [
        "animacy",
        "aspect",
        "case",
        "gender",
        "involvement",
        "mood",
        "number",
        "person",
        "tense",
        "transitivity",
        "voice"
    ]
    source = morph.parse(source)[0]
    target = morph.parse(target)[0]

    props = []
    for field in fields:
        source_field_value = getattr(source.tag, field, None)
        if source_field_value:
            props.append(source_field_value)

    props.sort(key=lambda x: str(x) == "plur" or str(x) == "sing" or str(x) == "perf")
    for prop in props:
        t = target.inflect({prop})
        if t:
            target = t

    return target.word


def get_norm_form(word: str):
    word = morph.parse(word)[0]
    return word.normalized.word


if __name__ == "__main__":
    # result = get_norm_form("которые")
    result = change_form("Какой", "ответственность")
    print(result)
    # result = change_form("Какой", "ответственность")
    # print(result)
    # result = change_form("Какой", "ответственность")
    # print(result)
    # result = change_form("Какой", "ответственность")
    # print(result)
    # result = change_form("Какой", "ответственность")
    # print(result)
