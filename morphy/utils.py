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


def get_norm_form(word: str) -> str:
    word = morph.parse(word)[0]
    return word.normalized.word


def is_animated(word: str):
    word = morph.parse(word)[0]
    return word.tag.animacy == 'anim'


def is_inanimate(word: str):
    return not is_animated(word)


def is_pron(word: str):
    word = morph.parse(word)[0]
    return word.tag.POS == "NPRO"


def get_morph(word: str):
    return morph.parse(word)[0]


if __name__ == "__main__":
    # result = get_norm_form("которые")
    # result = change_form("Какой", "ответственность")
    result = is_animated("Бег")
    print(result)
