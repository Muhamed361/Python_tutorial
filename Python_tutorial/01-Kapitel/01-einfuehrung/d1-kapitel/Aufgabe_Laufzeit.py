def main() -> None:
    """
    Rechnet Sekunden mithilfe von // und % in Minuten und Sekunden um.
    """
    gesamt_sekunden: int = 1455

    minuten: int = gesamt_sekunden // 60
    rest_sekunden: int = gesamt_sekunden % 60

    print(f"{gesamt_sekunden} Sekunden sind {minuten} Minuten und {rest_sekunden} Sekunden")


if __name__ == "__main__":
    main()
