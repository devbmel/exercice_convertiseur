def convert_cm_to_inch(value_cm: float) -> float:
    """Convert cm to inch. 

    Args:
        value_cm (float): Value in cm to convert.

    Returns:
        float: Value in inch.
    """
    return value_cm * 0.394


def convert_inch_to_cm(value_inch: float) -> float:
    """Convert inch to cm.

    Args:
        value_inch (float): Value in inch to convert.

    Returns:
        float: Value in cm.
    """
    return value_inch * 2.54


def user_menu() -> str:
    """Asks the user for his conversion choice.

    Returns:
        str: User choice.
    """
    user_choice: str = input(
        """
        Menu:
        A - Convertir de pouces vers cm.
        B - Convertir de cm vers pouces.

        Votre choix? 
        """
    )
    user_choice = user_choice.upper()
    if user_choice not in ("A", "B"):
        print("Veuillez saisir A ou B")
        return user_menu()
    return user_choice


def user_value_to_convert() -> float:
    """Ask the user for his value to convert.

    Returns:
        float: Value to convert.
    """
    value_to_convert: str = input("Veuillez rentrer la valeur à convertir: ")
    if not value_to_convert.isnumeric():
        print("Veuillez rentrer un nombre.")
        return user_value_to_convert()
    return float(value_to_convert)


def main() -> None:
    """Main programme for convert value."""
    value_to_convert: float = user_value_to_convert()
    convert_value: str = ""
    
    if user_choice == "A":
        convert_value = f"{convert_inch_to_cm(value_to_convert)}cm"
    else:
        convert_value = f"{convert_cm_to_inch(value_to_convert)}pouces"
    print(convert_value)


def repeat_main() -> None:
    """Ask the user if he want to convert new value.

    Returns:
        Optional[function]: None or loop.
    """
    user_choice: str = input("Voulez vous convertir d'autres valeurs? O/N: ")
    user_choice = user_choice.upper()
    if user_choice not in ("O", "N"):
        print("Veuillez saisir O ou N")
        return repeat_main()
    elif user_choice == "O":
        main()
        return repeat_main()
    return
    

if __name__ == "__main__":
    user_choice: str = user_menu()
    main()
    repeat_main()
    
    