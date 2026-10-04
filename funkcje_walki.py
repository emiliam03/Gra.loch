
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