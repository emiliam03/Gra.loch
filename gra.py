
def player_creator() -> dict:
    return {
    "imie" : "Lucjusz" ,
    "punkty_zycia" : 100 ,
    "punkty_ataku" : 10 ,
    "zloto" : 20 ,
    "ekwipunek" : ["różdżka", "mikstura"]
}


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

def after_fight(opponent: dict) -> None:
    print("\n"
          "~~~~~~~~~~~~~\n"
          "    (x_x)    \n"
          "~~~~~~~~~~~~~\n"
          "")
    wait_for_continue()
    print("Zwyciestwo! Pokonales przeciwnika \n"
          "*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_* \n"
          f"Otrzymujesz {opponent['nagroda_w_zlocie']} sztuk zlota. Bonus: {opponent['bonus']}"
          )

def opp_creator(name: str, hp: int, att: int, reward: int, bonusrew: str) -> dict:
    """Tworzy strukturę słownika, który przechowuje charakterystyki przeciwnika """

    return {
        "nazwa" : name,
        "punkty_zycia" : hp,
        "punkty_ataku" : att,
        "nagroda_w_zlocie" : reward,
        "bonus": bonusrew
    }

def opp_initiation() -> list[dict]:
    """Tworzy listę przeciwników"""

    smoczatko = opp_creator("Maugus", 15, 5, 20, "mikstura")
    goblin = opp_creator("Goblyn", 20, 10, 30, "mikstura")
    cyklop = opp_creator("Polifem", 100, 25, 100, "miecz")
    return [smoczatko, goblin, cyklop]


def wait_for_continue() -> None:
    """Czeka, aż gracz naciśnie C"""

    while True:
        answer = input("press C to continue: ")

        if answer.lower() == "c":
            break

        else:
            print("Nieprawidłowa opcja")
            continue


def opponent_choice(opponents: list[dict]) -> dict:
    """"""
    while True:
        try:
            opp_choice = int(input("\nWybierz swojego przeciwnika: "))
            przeciwnik = opponents[opp_choice - 1]

        except ValueError:
            print("Wpisz numer przeciwnika")
            continue

        except IndexError:
            print("Indeks poza zakresem!")
            continue

        break
    return przeciwnik



def attack(opponents: list[dict], player: dict) -> None:
    if not opponents:
        print("Pokonałeś już wszystkich przeciwników")
        return

    show_opponents(opponents)
    przeciwnik = opponent_choice(opponents)

    while True:
        during_fight(player, przeciwnik)
        atak = input(f"choose your move: ")
        match atak:
            case "1":
                przeciwnik["punkty_zycia"] -= player["punkty_ataku"]
                print(
                    "\n"
                    f"    {przeciwnik['nazwa']}: -{player['punkty_ataku']} HP \n"
                    ""
                    )
            case "2":
                if "mikstura" not in player["ekwipunek"]:
                    print("\nW twoim ekwipunku nie ma mikstury.")
                    continue
                else:
                    player["punkty_zycia"] += 10
                    player["ekwipunek"].remove("mikstura")
                    print(f"\n+10 HP. Masz {player['punkty_zycia']} HP")
                    continue
            case "3":
                print("Ucieczka")
                break
            case _:
                print("Wybrałeś nieprawidłową opcję.")
                continue

        if przeciwnik["punkty_zycia"] > 0:
            print(
                f"{przeciwnik['nazwa']} atakuje! \n"
                "\n"
                f"    Gracz -{przeciwnik['punkty_ataku']} HP \n"
                ""
            )

            wait_for_continue()

            player["punkty_zycia"] -= przeciwnik["punkty_ataku"]
            if player["punkty_zycia"] <= 0:
                print("Nie zyjesz X0X")
                return
            else:
                continue
        else:

            wait_for_continue()

            after_fight(przeciwnik)
            player["ekwipunek"].append(przeciwnik["bonus"])
            player["zloto"] += przeciwnik["nagroda_w_zlocie"]
            opponents.remove(przeciwnik)

            break





def main():
    opponents = opp_initiation()
    player = player_creator()
    while True:
        menu_loch()
        wybor = input("Wybierz opcje: ")
        match wybor:
            case "4":
                break
            case "3":
                show_equipment(player)
                wait_for_continue()
            case "2":
                show_stats(player)
                wait_for_continue()
            case "1":
                attack(opponents, player)

if __name__ == "__main__":
    main()