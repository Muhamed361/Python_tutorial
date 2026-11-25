def main() -> None:
    """
    Rechnen und Datentypen.
    """
    print(7 + 3)#10
    print(7 - 3)#4
    print(7 * 3)#21
    print(7 / 3)#2,33
    print(7 // 3)#2; das zeichen berechnet ganzzahldivisionen also zahlen ohne rest
    print(7 % 3)#0,21; das zeichen berechnet den rest einer Division 
    print(7 ** 3)#343

    print(type(5))#eine ganzzahl,da kein punkt vorhanden ist
    print(type(5.0))#kommazahl, da ein dezimalpunkt verwendet wird
    print(type("5"))#Zeichenkette,weil die zahl in anführiungsstrichen steht und somit als text gilt
    print(type(7 > 3))#Wahreitswert, weil der Vergeich ausgewertet wird 


if __name__ == "__main__":
    main()