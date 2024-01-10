# main.py
import sys
import os
from utilis import extract
from calcule import vit_max, vit_moyenne, vit_min
from analyse_de_trames_NMEA_GPS import positions_extremes, premier_dernier_gga, extract_high_alt
from genere_html import genere_page_web


current_script_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_script_path)

def main():
    chemin_absolu = os.path.abspath('trame.txt')
    print(chemin_absolu)
    infos = extract(chemin_absolu)
    print(infos)
    maxi = vit_max(infos)
    moyenne = vit_moyenne(infos)
    mini = vit_min(infos)
    resultat_positions_extremes = positions_extremes(infos)
    premier = premier_dernier_gga(infos)
    max_nord = resultat_positions_extremes["max_nord"]
    min_sud = resultat_positions_extremes["min_sud"]
    max_est = resultat_positions_extremes["max_est"]
    min_ouest = resultat_positions_extremes["min_ouest"]
    alt = extract_high_alt(infos)
    positions_extremes_resultat = positions_extremes(infos)

    genere_page_web("../html/", "Résultats de l'analyse de trame GPS", infos, premier,
                positions_extremes_resultat["max_nord"], positions_extremes_resultat["min_sud"],
                positions_extremes_resultat["max_est"], positions_extremes_resultat["min_ouest"],
                alt, maxi, moyenne, mini)
    

if __name__ == "__main__":
    main()

print("Le programme s'est exécuté avec succès.")
