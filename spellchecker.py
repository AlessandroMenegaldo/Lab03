import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multidiz=md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        """
        Testo in ingresso, ripulisce il testo e crea lista parole con indicativi di correttezza
        a questo  punto conta parola sbagliate e le stampa
        :param txtIn: testo in input
        :param language: lingua scelta
        :return: lista parola sbagliate
        """


        clearText= replaceChars(txtIn)
        parole=clearText.strip().split(' ')

        print("Using Contains")
        start = time.time()
        words=self.multidiz.searchWord(parole, language)
        print("Parole errate: ")
        for w in words:
            if not w.corretta:
                print(w)

        end = time.time()
        print(f"Time elapsed: {end - start} \n")

        print("Using Linear Research")
        start2 = time.time()
        words = self.multidiz.searchWordLinear(parole, language)
        print("Parole errate: ")
        for w in words:
            if not w.corretta:
                print(w)

        end2 = time.time()
        print(f"Time elapsed: {end2 - start2}")
        pass

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    """
    Ripulisce testo in input
    :param text: testo da pulire
    :return: testo pulito
    """
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text