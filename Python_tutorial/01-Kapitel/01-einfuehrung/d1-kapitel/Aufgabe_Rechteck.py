def main() -> None:
    """
    Berechnet Umfang und Flächeninhalt eines Rechtecks.
    """
    laenge: int = 8
    breite: int = 5

    umfang: int = 2 * (laenge + breite)
    flaecheninhalt: int = laenge * breite

    print(f"Das Rechteck hat einen Umfang von {26} und einen Flächeninhalt von {40}.")


if __name__ == "__main__":
    main()
