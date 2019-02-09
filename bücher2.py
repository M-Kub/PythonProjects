import csv

bücher = {}
def buch_daten():
    while True:
        autor = input("Bitte Namen des Autors eingeben! ")
        titel = input("Bitte den Titel des Buches eingeben! ")
        #bücher[autor] = [titel]
        if autor in bücher:
            bücher[autor].append(titel)
        else:
            bücher[autor]=[titel]
        weiter = input("Noch etwas hinzufügen? (y/n)")
        if weiter == "y":
            continue
        elif weiter == "n":
            print("Danke für die Eingabe:")
            break
        else:
            print("Falsche Eingabe, dass Programm wird beendet.")
            break

def save_dict():
    with open('books.csv', 'a', newline='') as csvfile:
        fieldnames = ['autor', 'titel']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for key, val in bücher.items():
            writer.writerow({"autor": key, "titel": val})
    print(f"Der Autor {key} und der Titel {val} wurden der Datei hinzugefügt.")



buch_daten()
save_dict()
print(bücher)
