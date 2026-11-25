def main() -> None:
    """
    Das Plus-Zeichen bei Zahlen und Texten.
    """
    print(5 + 5)#Ausgabe: 5
    print("5" + "5")#Ausgabe: 55
    print("Hallo" + " " + "Welt")#Ausgabe: Hallo Welt
    print("5" + 5)#Fehlermeldund,weil man keinen text direkt mit einer zahl addieren kann
    print("Ha" * 3)#Ausgabe: HaHaHa

    # Ein TypeError ist eine Fehlermeldung die erscheint wenn man Aktion mit den Falschen Datentypen ausführen will, da Python nicht weiß was es machen soll

if __name__ == "__main__":
    main()