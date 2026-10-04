
def wait_for_continue() -> None:
    """Czeka, aż gracz naciśnie C"""

    while True:
        answer = input("press C to continue: ")

        if answer.lower() == "c":
            break

        else:
            print("Nieprawidłowa opcja")
            continue