from question_answer_generator.questions.actions import create_action_questions_for_object, \
    create_adjective_questions_for_object, create_subject_questions_for_object


class QuestionAnswerGenerator:
    methods = [
        # create_action_questions_for_object,
        # create_adjective_questions_for_object,
        create_subject_questions_for_object
    ]

    @classmethod
    def generate(cls, sentences):
        output = []
        for sentence in sentences:
            for method in cls.methods:
                question_answer_set = method(sentence)
                output.extend(question_answer_set)
        return output
