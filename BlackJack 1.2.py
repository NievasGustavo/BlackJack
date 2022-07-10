import random

username = input("Username:")
fichas = int(input("Introduce tus fichas: "))
apuesta = 0

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4
suits = ["♣", "♠", "♥", "♦"]
Jugadas = 1
Apuestas = 0
contador_apuestas = 0
Ganadas = 0
Perdidas = 0
Pozo = 0
fichas_inicial = 0
max_fichas = 0
bandera_max = True
racha_mas_larga = 0
racha_actual = 0


# Elegir carta

def tirada():
    mano = []
    for i in range(2):
        random.shuffle(deck)
        carta = deck.pop()
        if carta == 11:
            carta = "J"
        if carta == 12:
            carta = "Q"
        if carta == 13:
            carta = "K"
        if carta == 14:
            carta = "A"
        mano.append(carta)
    return mano


def total(mano):
    total2 = 0
    for card in mano:
        if card == "J" or card == "Q" or card == "K":
            total2 += 10
        elif card == "A":
            if total2 >= 11:
                total2 += 1
            else:
                total2 += 11
        else:
            total2 += card
    return total2


def hit(mano):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    mano.append(card)
    return mano


def hacer_apuesta():
    global fichas_inicial, apuesta, max_fichas, Apuestas, contador_apuestas, bandera_max, fichas
    apuesta = int(input("Cuanto a apostar: "))

    while apuesta != 0 and apuesta % 5 == 0:
        if apuesta <= fichas:
            fichas_inicial = fichas
            if max_fichas < fichas_inicial or bandera_max:
                max_fichas = fichas_inicial
                bandera_max = False
            Apuestas = Apuestas + apuesta
            contador_apuestas += 1
            break
        else:
            print("No es multiplo de 5")
            print("Apuesta invalida, tus fichas son " + str(fichas))


def mostrar_resultados(mano_groupier, mano_jugador):
    print("El groupier tiene " + str(mano_groupier) + " en total es " + str(total(mano_groupier)))
    print("Tu tienes " + str(mano_jugador) + " en total es " + str(total(mano_jugador)))


def blackjack(mano_groupier, mano_jugador):
    global fichas_inicial, apuesta, Ganadas, Perdidas, fichas, racha_mas_larga, racha_actual
    if total(mano_jugador) == 21:
        mostrar_resultados(mano_groupier, mano_jugador)
        Ganadas += 1
        racha_actual += 1
        print("Felicidades ", username, " tu tienes BlackJack!\n")
        fichas += apuesta * 2
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo inicial ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_groupier) == 21:
        mostrar_resultados(mano_groupier, mano_jugador)
        Perdidas += 1
        if racha_actual > racha_actual:
            racha_mas_larga = racha_actual
        racha_actual = 0
        print("Lo siento ", username, ", perdiste el groupier tiene blackjack.\n")
        fichas -= apuesta
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()


def puntaje(mano_groupier, mano_jugador):
    global Ganadas, Perdidas, apuesta, fichas, racha_mas_larga, racha_actual

    if total(mano_jugador) == 21:
        Ganadas = Ganadas + 1
        racha_actual = racha_actual + 1
        mostrar_resultados(mano_groupier, mano_jugador)
        print("Felicidades ", username, " tu tienes BlackJack!\n")
        fichas += apuesta * 2
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_groupier) == 21:
        Perdidas += 1
        if racha_actual > racha_mas_larga:
            racha_mas_larga = racha_actual
        racha_actual = 0
        mostrar_resultados(mano_groupier, mano_jugador)
        print("Lo siento ", username, ", perdiste el groupier tiene blackjack.\n")
        fichas -= apuesta
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_jugador) > 21:
        Perdidas += 1
        if racha_actual > racha_mas_larga:
            racha_mas_larga = racha_actual
        racha_actual = 0
        mostrar_resultados(mano_groupier, mano_jugador)
        print("Lo siento ", username, ", te pasaste. Perdiste\n")
        fichas -= apuesta
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_groupier) > 21:
        Ganadas = Ganadas + 1
        racha_actual = racha_actual + 1
        mostrar_resultados(mano_groupier, mano_jugador)
        print("El groupier se paso. Ganaste!\n")

    elif total(mano_jugador) < total(mano_groupier):
        Perdidas = Perdidas + 1
        if racha_actual > racha_mas_larga:
            racha_mas_larga = racha_actual
        racha_actual = 0
        mostrar_resultados(mano_groupier, mano_jugador)
        print("Lo siento ", username, ". Tu puntaje es mas bajo que el del groupier. Perdiste.\n")
        fichas -= apuesta
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_jugador) > total(mano_groupier):
        Ganadas = Ganadas + 1
        racha_actual = racha_actual + 1
        mostrar_resultados(mano_groupier, mano_jugador)
        print("Felicidades  ", username, ". Tus puntos son mas altos que el del groupier. Ganaste\n")
        fichas += apuesta * 2
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()

    elif total(mano_jugador) < 21 > total(mano_groupier):
        mostrar_resultados(mano_groupier, mano_jugador)
        print(username, "Empataste con el groupier, nadie gana.")
        print("Tu pozo inicial era: ", fichas_inicial)
        print("Tu apuesta fue:", apuesta)
        print("Tu pozo ahora es: ", fichas)
        jugar_de_nuevo()


def index():
    global Jugadas, fichas
    eleccion = 0
    mano_groupier = tirada()
    mano_jugador = tirada()
    hacer_apuesta()
    while eleccion != "q":
        print("La primera carta del groupier es " + str(mano_groupier[0]))
        print("Tu tienes " + str(mano_jugador) + " el total es  " + str(total(mano_jugador)))
        blackjack(mano_groupier, mano_jugador)
        eleccion = input("Quieres Pedir otra[H], Plantarte[S], o Salir[Q]: ").lower()

        if eleccion == "h":
            hit(mano_jugador)
            if total(mano_jugador) < 21:
                print("La primera carta del groupier es " + str(mano_groupier[0]))
                print("Tu tienes " + str(mano_jugador) + " el total es  " + str(total(mano_jugador)))
                eleccion = input("Quieres Pedir otra[H], Plantarte[S], o Salir[Q]: ").lower()
            else:
                while total(mano_groupier) <= 16:
                    hit(mano_groupier)
                puntaje(mano_groupier, mano_jugador)
                jugar_de_nuevo()

        elif eleccion == "s":
            while total(mano_groupier) <= 16:
                hit(mano_groupier)
            puntaje(mano_groupier, mano_jugador)
            jugar_de_nuevo()

        elif eleccion == "q":
            final()
            menu_principal()


def sumar_fichas():
    global fichas
    print("Tienes: ", fichas, "fichas en total.")
    fichas_a_sumar = int(input("Fichas Para Añadir:"))
    if fichas_a_sumar > 0 and fichas_a_sumar > 10000:
        fichas += fichas_a_sumar
    else:
        print("Numero erroneo, usa un nro mayor a 0")


def final():
    global Jugadas, Apuestas, Ganadas, Perdidas, Pozo, contador_apuestas
    print("Ganaste ", Ganadas, " veces")
    print("Perdiste ", Perdidas, " veces")
    print("Tus fichas son: ", fichas)
    print("El promedio de Apuestas fue: ", Apuestas % contador_apuestas)
    if Ganadas != 0:
        print("Porcentaje de victorias: ", (Ganadas / 100) * Perdidas)
    print("Tu pozo maximo fue: ", max_fichas)
    print("Tu racha mas larga de Ganadas fue:", racha_mas_larga)


def menu_principal():
    global Jugadas
    ans = True
    while ans:
        print("Bienvenido a Blackjack!\n")
        print("""
        1.Jugar 
        2.Apostar
        3.Exit/Quit 
        """)
        ans = input("¿Que queres hacer?:")
        if ans == "1":
            Jugadas += 1
            print("\n")
            index()
        elif ans == "2":
            sumar_fichas()
        elif ans == "3":
            final()
            print("Adios!", username)
            break
        elif ans != "":
            print("\n No es valido lol")
            break


def jugar_de_nuevo():
    global Jugadas
    again = input("Quieres Jugar De Nuevo? (Y/N) : ")
    if again == "y":
        Jugadas = Jugadas + 1
        hacer_apuesta()
        index()
    else:
        print("Adios!", username)
        print("\n")
        menu_principal()


menu_principal()
