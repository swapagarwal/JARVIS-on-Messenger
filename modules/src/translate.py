from googletrans import Translator
from googletrans import LANGCODES
from templates.text import TextTemplate


def process(intent, entities):
    output = {}
    output['input'] = intent

    translator = Translator()
    words_to_translate = entities[0]['word']
    src_lang = LANGCODES.get(entities[0]['curr-lang'])
    dest_lang = LANGCODES.get(entities[0]['new-lang'])

    if src_lang is not None:
        translated_text = translator.translate(words_to_translate, src=src_lang, dest=dest_lang)

        if translated_text.text == words_to_translate:
            output['output'] = "fail"
            output['success'] = False
        else:
            output['output'] = TextTemplate(translated_text.text).get_message()
            output['success'] = True
    else:
        translated_text = translator.translate(words_to_translate, dest=dest_lang)

        output['output'] = TextTemplate(translated_text.text).get_message()
        output['success'] = True

    return output
