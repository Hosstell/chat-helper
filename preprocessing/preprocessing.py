from nlp import nlp
from preprocessing.preprocessors.preprocessors import get_advcl_sentence, get_conj_sentence, get_main_sentence, \
    get_sub_sentence_loc, get_sub_sentence_standard


class Preprocessor:
    methods = [
        get_advcl_sentence,
        get_conj_sentence,
        get_sub_sentence_standard,
        get_main_sentence,
        get_sub_sentence_loc
    ]

    @classmethod
    def generate(cls, text):
        sentences = nlp(text).sents

        output = []
        for sentence in sentences:
            for method in cls.methods:
                question_answer_set = method(sentence.text)
                output.extend(question_answer_set)
        return output