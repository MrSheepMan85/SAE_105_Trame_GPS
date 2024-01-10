# genere_html.py

import os
from calcule import vit_max, vit_min, vit_moyenne
from analyse_de_trames_NMEA_GPS import extract, premier_dernier_gga, positions_extremes, extract_high_alt

def genere_page_web(nom_fichier, titre_page, infos_trame, premier_GGA, dernier_GGA, max_nord, min_sud, max_est, min_ouest, alt, maxi, moyenne):
    try:
        with open(nom_fichier, mode='w', encoding='utf-8') as fichier:
            fichier.write(generer_html(titre_page, infos_trame, premier_GGA, dernier_GGA, max_nord, min_sud, max_est, min_ouest, alt, maxi, moyenne))
        print("Le fichier HTML a été généré avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la génération du fichier HTML : {str(e)}")

def generer_html(titre_page, infos_trame, premier_GGA, dernier_GGA, max_nord, min_sud, max_est, min_ouest, alt, maxi, moyenne):
    return f"""

    with open('../html/page_html.html', mode='w', encoding='utf-8') as fichier:
        corps = f"""
          <!DOCTYPE html>
          <html lang="fr">
          <head>
              <meta charset="UTF-8">
              <meta name="viewport" content="width=device-width, initial-scale=1.0">
              <title>{titre_page}</title>
              <link rel="stylesheet" href="style.css">
          </head>
          <body>
              <header>
                  <h1>{titre_page}</h1>
              </header>
              <section>
                 <table>
                      <tr>
                         <th>Type de trame</th>
                         <th>Heure de la trame</th>
                         <th>Coordonnées Nord</th>
                         <th>Coordonnées Est</th>
                         <th>Satellites en poursuite</th>
                         <th>Altitude</th>
                         <th>Vitesse</th>
                     </tr>
                     <tr>
                         <td>{infos_trame[0].get("type", "N/A")}</td>
                         <td>{infos_trame["horaire"][0]}:{infos_trame["horaire"][1]}:{infos_trame["horaire"][2]}</td>
                         <td>{infos_trame["nord"][0]}° {infos_trame["nord"][1]}'</td>
                         <td>{infos_trame["est"][0]}° {infos_trame["est"][1]}'</td>
                         <td>{infos_trame["nbsat"]}</td>
                         <td>{infos_trame["alt"]} Mètres</td>
                         <td>{infos_trame.get("vit", "N/A")} m/s</td>
                     </tr>
                </table>
                <table>
                    <tr> 
                        <th>Etat trame</th>
                        <th>trame</th>
                    </tr>
                    <tr>
                        <td>départ</td> 
                        <td>{premier_GGA}</td>
                    </tr>
                    <tr>
                        <td>arrivé</td>
                        <td>{dernier_GGA}</td>
                    </tr>
                </table>

                <table>
                    <tr>
                        <th>Plus au Nord</th>
                        <th>Plus au Sud</th>
                        <th>Plus à l'Ouest</th>
                        <th>Plus à l'Est</th>
                        <th>Plus élevé</th>
                    </tr>
                    <tr>
                        <td>{max_nord}</td>
                        <td>{min_sud}</td>
                        <td>{min_ouest}</td>
                        <td>{max_est}</td>
                        <td>{alt}</td>
                    </tr>
                </table>

                <table>
                    <tr>
                        <th>Vitesse max</th>
                        <th>Vitesse moyenne</th>
                        
                    </tr>
                    <tr>
                        <td>{maxi}</td>
                        <td>{moyenne}</td>
                        
                    </tr>
                </table>
            </section>
            <footer>
                <p>Réalisé par CHAILLOU Matthieu et ZORILLA Etienne</p>
            </footer>
        </body>
        </html>
        """
        fichier.write(corps)

def main():
    chemin_absolu = os.path.abspath('analyse_de_trames_NMEA_GPS/trame.txt')
    print(chemin_absolu)
    infos = extract(chemin_absolu)
    max_vitesse = vit_max(infos)
    moyenne = vit_moyenne(infos)
    min_vitesse = vit_min(infos)
    resultat_positions_extremes = positions_extremes(infos)
    premier = premier_dernier_gga(infos)
    max_nord = resultat_positions_extremes["max_nord"]
    min_sud = resultat_positions_extremes["min_sud"]
    max_est = resultat_positions_extremes["max_est"]
    min_ouest = resultat_positions_extremes["min_ouest"]
    alt = extract_high_alt(infos)
    genere_page_web("..//html/", "Résultats de l'analyse de trame GPS", infos, premier, resultat_positions_extremes["dernier_GGA"],
                    max_nord, min_sud, max_est, min_ouest, alt, max_vitesse, moyenne, min_vitesse)

if __name__ == "__main__":
    main()

print("Le programme s'est exécuté avec succès.")
