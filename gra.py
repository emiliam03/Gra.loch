from prints import (
    show_stats,
    show_equipment,
    show_opponents,
    menu_loch,
    during_fight,
)


def player_creator() -> dict:
    return {
    "imie" : "Lucjusz" ,
    "punkty_zycia" : 100 ,
    "punkty_ataku" : 10 ,
    "zloto" : 20 ,
    "ekwipunek" : ["różdżka", "mikstura"]
}


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