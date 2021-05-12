from googletrans import Translator

translator = Translator()


def translateMe(txt, lang):
    output = translator.translate(txt, dest=lang)
    return output.text