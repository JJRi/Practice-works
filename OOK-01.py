#opiskelijan ohjelmointikirja
#Eläinvisa

pisteet = 0


def onko_oikein(guess, answer):
    global pisteet
    viela_arvaa = True
    yritykset = 0
    while viela_arvaa and yritykset < 3:
        if guess.lower() == answer.lower():
            print('Oikein tiedetty!')
            viela_arvaa = False
            pisteet += 1
        else:
            if yritykset < 2:
                guess = input('Väärin meni. Arvaa uudestaan.')
            yritykset += 1
        if yritykset == 3:
            print('Oikea vastaus oli:', answer)

    return


def peli():
    print('Tervetuloa arvaa eläin peliin!')
    print('Aloitetaan.')
# Kaikki pelin kysymykset tulevat alle
    quest1 = input('Mikä karhu elää pohjoisnavalla?')
    onko_oikein(quest1, 'jääkarhu')
    quest2 = input('Mikä elää savannilla ja sillä on pitkä kaula?')
    onko_oikein(quest2, 'kirahvi')
    quest3 = input('Mikä on suurin eläin nykypäivänä?')
    onko_oikein(quest3, 'sinivalas')
    pelin_lopetus()
    return



def pelin_lopetus():
    global pisteet
    print('Kiitos pelaamisesta. Sait {} pistettä.'.format(pisteet))
    answer = ''
    while answer != 'k' or 'e':
        answer = input('Haluatko pelata uudestaan? (k/e)')
        if answer == 'e':
            print('Kiitos pelaamisesta!')
            quit()
        elif answer == 'k':
            print('Selvä, pelataan lisää.')
            pisteet = 0
            peli()
        else:
            continue
    pelaatko_lisaa(answer)
    return



if __name__ == "__main__":
    peli()
