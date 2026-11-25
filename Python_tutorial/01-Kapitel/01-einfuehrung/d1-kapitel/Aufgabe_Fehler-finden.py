def main() -> None:
    preis: float = 2.50
    anzahl: int = 4

    # Fehler 1: Das schließende Anführungszeichen (") hat gefehlt.
    # Fehlermeldung: SyntaxError: unterminated f-string literal
    print(f"Gesamt: {preis * anzahl} Euro")

    # Fehler 2: Text (str) und Zahl (int) können nicht direkt mit + verbunden werden.
    # Fehlermeldung: TypeError: can only concatenate str (not "int") to str
    print("Anzahl: " + str(anzahl))

    # Fehler 3: Python unterscheidet Groß- und Kleinschreibung (Preis statt preis).
    # Fehlermeldung: NameError: name 'Preis' is not defined
    print(preis)


if __name__ == "__main__":
    main()  # Hinweis: Das Semikolon am Ende ist in Python unüblich, aber kein Fehler.
