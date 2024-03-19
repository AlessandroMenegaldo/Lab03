import spellchecker
import time


sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!


    results = []
    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input().lower()
        results=sc.handleSentence(txtIn,"Italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input().lower()
        results=sc.handleSentence(txtIn,"English")
        print(f"Numero parole errate: {len(results)}")
        for p in results:
            print(p)
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input().lower()
        results=sc.handleSentence(txtIn,"Spanish")
        print(f"Numero parole errate: {len(results)}")
        for p in results:
            print(p)
        continue

    if int(txtIn) == 4:
        break


