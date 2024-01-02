from greets import greetings
from translate import Translator

translator = Translator(to_lang='ru')

for g in greetings:
    print(translator.translate(g).title())