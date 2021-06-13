from question_answer_generator.questions.actions import create_subject_questions_for_object


def test_create_subject_questions_for_object():
    input_text = "Мать ездила в троицу к обедне."
    output_text = [
        ['Кто ездила в троицу к обедне?', 'Мать']
    ]

    result = create_subject_questions_for_object(input_text)
    assert(result[0][0] == output_text[0][0])
    assert(result[0][1] == output_text[0][1])


def test_create_subject_questions_for_object_1():
    input_text = "На столе лежало два яблока."
    output_text = [
        ['Что на столе лежало?', 'Два яблока']
    ]

    result = create_subject_questions_for_object(input_text)
    assert(result[0][0] == output_text[0][0])
    assert(result[0][1] == output_text[0][1])

