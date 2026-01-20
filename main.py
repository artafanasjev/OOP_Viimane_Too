import easygui
from klassid import Karakter, Vaenlane
import sys

nimi = easygui.enterbox("Sisesta oma tegelase nimi: ")
elud = easygui.enterbox("Sisesta elude arv: ")
tugevus = int(easygui.enterbox("Sisesta tugevus: "))

mangija = Karakter(nimi, elud, tugevus)

lubatud_kohad = [
    (0,0), (1,0), (2,0),
    (0,1), (1,1), (2,1),
    (1,2), (2,2)
]

vaenlane1 = Vaenlane(10, 2)
vaenlane2 = Vaenlane(8, 3)

vaenlased = {
    (2,1): vaenlane1,
    (1,2): vaenlane2
}

asukoht = (0, 0)

asukoht = (0, 0)

while True:
    valik = easygui.buttonbox(
        f"Asukoht: {asukoht}\nElud: {mangija.elud}",
        choices=["Edasi", "Tagasi", "Vasakule", "Paremale"]
    )

    uus_asukoht = liiguta(asukoht, valik)

    if uus_asukoht not in lubatud_kohad:
        easygui.msgbox("Sinna suunas ei saa liikuda!")
        continue

    asukoht = uus_asukoht

    if asukoht in vaenlased:
        vaenlane = vaenlased[asukoht]

        mangija.kaotaElusi(vaenlane.tugevus)
        vaenlane.kaotaElusi(mangija.tugevus)

        easygui.msgbox(
            f"Võitlus!\n"
            f"Sinu elud: {mangija.elud}\n"
            f"Vaenlase elud: {vaenlane.elud}"
        )

        if mangija.elud <= 0:
            easygui.msgbox("Sa surid")
            sys.exit()

        if vaenlane.elud <= 0:
            easygui.msgbox("Vaenlane suri")
            del vaenlased[asukoht]