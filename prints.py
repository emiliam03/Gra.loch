def show_stats(player: dict) -> None:
    """Wyświetla statystyki gracza"""

    print(
        "\n"
        "===================\n"
        "    STATYSTYKI\n"
        "===================\n"
        f"  Imię: {player['imie']}\n"
        f"  HP: {player['punkty_zycia']}\n"
        f"  Atak: {player['punkty_ataku']}\n"
        f"  Złoto: {player['zloto']}\n"
        "==================\n"
    )


def show_equipment(player: dict) -> None:
    """Wyświetla ekwipunek gracza"""
    print("\nTwój ekwipunek:")
    if player["ekwipunek"]:
        for element in player["ekwipunek"]:
            print(f"-{element}")
    else:
        print("Twój ekwipunek jest pusty.")

    print()


def menu_loch() -> None:
    """Wyświetla menu lochu"""

    print(
        "\n"
        "~~~~~~~~~~LOCH~~~~~~~~~~\n"
        " 1. Idź dalej\n"
        " 2. Sprawdź statystyki\n"
        " 3. Sprawdź ekwipunek\n"
        " 4. Zakończ grę\n"
        "~~~~~~~~~~~~~~~~~~~~~~~~\n"
        ""
    )


def show_opponents(opponents: list[dict]) -> None:
    """Wyświetla dostępnych przeciwników"""

    print(
        "\n"
        "~~~~~~~~~~~~~~~~~~~~~~~~\n"
        "WALKA! \n"
        "~~~~~~~~~~~~~~~~~~~~~~~~ \n"
    )

    for index, opponent in enumerate(opponents):
        print(f"{index+1}.{opponent['nazwa']}")


def during_fight(player: dict, opponent: dict) -> None:
    print(
        "\n"
        f"    {opponent['nazwa']}: {opponent['punkty_zycia']} HP\n"
        f"    Ty: {player['punkty_zycia']} HP\n"
        "\n"
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        "1. Atakuj\n"
        "2. Uzyj mikstury\n"
        "3. Uciekaj\n"
        "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    )

