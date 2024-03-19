class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        """
        Legge il file dato come imput creando dizionario (lista di parole corrette)
        :param path:
        :param dict: file testo contentente dizionario
        :return: null
        """

        infile = open(f"resources/{path}.txt", "r")
        contenuto_file = infile.read()
        infile.close()

        parole = contenuto_file.strip().split('\n')
        for p in parole:
            self._dict.append(p)
        pass

    def printAll(self):
        pass


    @property
    def dict(self):
        return self._dict