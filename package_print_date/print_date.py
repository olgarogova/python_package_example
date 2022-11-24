from datetime import date


def main():
    """
    функция для распечатки текущей даты
    """
    today = date.today()
    # dd/mm/YY
    d = today.strftime("%d/%m/%Y")
    print("date =", d)


if __name__ == '__main__':
    main()
