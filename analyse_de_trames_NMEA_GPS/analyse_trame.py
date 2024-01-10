# analyse_trame.py
from genere_html import genere_page_web
from utilis import extract
import calcule

def main():
    trames_infos = extract('trame.txt')

    # On appelle d'autres fonctions d'analyse selon les besoins
    positions_extremes_resultat = calcule.positions_extremes(trames_infos)
    max_altitude = calcule.extract_high_alt(trames_infos)
    resultat_premier_dernier_gga = calcule.premier_dernier_gga(trames_infos)

    genere_page_web("./html/", "Résultats de l'analyse de trame GPS", {
        "positions_extremes": positions_extremes_resultat,
        "max_altitude": max_altitude,
        "premier_gga": resultat_premier_dernier_gga[0],
        "dernier_gga": resultat_premier_dernier_gga[1]
    })

if __name__ == "__main__":
    main()