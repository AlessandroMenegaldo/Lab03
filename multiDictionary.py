import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionario=d.Dictionary()
        pass

    def printDic(self, language):
        self.dizionario.loadDictionary(language)
        return self.dizionario.dict

    def searchWord(self, words, language):

        """
        cerca la parola nel dizionario giusto e poi crea RichWord indicando True o False
        :param words: 
        :param language: 
        :return: 
        """
        diz=self.printDic(language)

        listaRichWords = []
        for p in words:
            nuovaparola = rw.RichWord(p)
            if diz.__contains__(p):
                nuovaparola.corretta = True
            else:
                nuovaparola.corretta = False
            listaRichWords.append(nuovaparola)

        return listaRichWords

    def searchWordLinear(self, words, language):

        """
        DA RIVEDEREEEEEEEEEEEEE
        cerca la parola nel dizionario giusto e poi crea RichWord indicando True o False
        :param words:
        :param language:
        :return:
        """
        diz=self.printDic(language)

        listaRichWords = []
        for p in words:
            nuovaparola = rw.RichWord(p)
            for istanza in diz:

                if  istanza == diz:
                    nuovaparola.corretta = True
                else:
                    nuovaparola.corretta = False
            listaRichWords.append(nuovaparola)

        return listaRichWords

