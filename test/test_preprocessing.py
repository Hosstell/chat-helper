from preprocessing.preprocessors.preprocessors import get_sub_sentence_standard, get_main_sentence, get_conj_sentence, \
    get_sub_sentence_loc


def test_get_sub_sentence_standard():
    input_text = "Помнил он , что мать ездила в троицу к дому, который стояла на холме"
    output_text = ["Дом стояла на холме."]

    result = get_sub_sentence_standard(input_text)
    assert(result[0] == output_text[0])


def test_get_main_sentence():
    input_text = "В Сан-Франциско рассматривается возможность запрета роботов-курьеров, которые перемещаются по тротуару"
    output_text = ["В сан - франциско рассматривается возможность запрета роботов - курьеров."]

    result = get_main_sentence(input_text)
    assert(result[0] == output_text[0])


def test_get_conj_sentence():
    input_text = "Но тут один из перевозчиков увидел его замешательство, подплыл и переправил его."
    output_text = ['Один из перевозчиков подплыл.', 'Один из перевозчиков переправил его.']

    result = get_conj_sentence(input_text)
    assert(result[0] == output_text[0])
    assert(result[1] == output_text[1])


def test_get_sub_sentence_loc():
    input_text = "Я стоял около пляжа, на котором лежал горячий песок."
    output_text = ['На пляже лежал горячий песок.']

    result = get_sub_sentence_loc(input_text)
    assert(result[0] == output_text[0])
