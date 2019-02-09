import csv


bücher = {}
def buch_daten():
    while True:
        autor = input("Bitte den Autor eingeben: ")
        if autor == "":
            break
        while True:
            titel = input("Bitte Titel eingeben: ")
            if titel == "":
                break
            if autor in bücher:
                bücher[autor].append(titel)
            else:
                bücher[autor]=[titel]
    #print(bücher)
    with open('books.csv', 'a', newline='') as csvfile:
        fieldnames = ['Autor', 'Titel']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for key, val in bücher.items():
            writer.writerow({"Autor": key, "Titel": val}) 
        #outputFile = open("books.csv", "a", newline="")
        #fieldnames = [autor, titel]
        #outputWriter = csv.DictWriter(outputFile, fieldnames=fieldnames, delimiter="\t")
        #outputWriter.writerow({autor: autor, titel: titel})
    print(f"Der Autor {key} und der Titel {val} wurden der Datei hinzugefügt.") 
buch_daten()
