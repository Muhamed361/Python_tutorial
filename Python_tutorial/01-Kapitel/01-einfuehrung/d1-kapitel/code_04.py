def main() -> None:
    """
    Variablen, Zuweisungen und Ausgaben.
    """
    x: int = 7
    y: int = 9
    summe: int = x + y


    print(summe)
    print(str(x) + " + " + str(y) + " = " + str(summe))
    print(f"{x} + {y} = {summe}")
    #Die beiden Zahlen 7 und 9 werden als variable gespeichert und berechnet. Das berechnete Ergebnis wird daraufhin in drei unterschiedlichen Arten ausgegeben: einmal nur als Zahl und zweimal als vollständige Rechenaufgabe mit Text


if __name__ == "__main__":
    main()