# genere_html.py

import os
from calcule import vit_max, vit_min, vit_moyenne
from analyse_de_trames_NMEA_GPS import extract, premier_dernier_gga, positions_extremes, extract_high_alt

def generer_html(titre_page, infos_trame, premier_GGA, dernier_GGA, max_nord, min_sud, max_est, min_ouest, alt, maxi, moyenne):
    

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
   chemin_absolu = "$GNGGA,180844.000,4635.0198,N,00020.0347,E,1,24,0.62,69.9,M,48.4,M,,*49;$GNRMC,180844.000,A,4635.0198,N,00020.0347,E,0.000,207.28,070124,,,A,V*32;$GNVTG,207.28,T,,M,0.000,N,0.000,K,A*2C;$GNGGA,180845.000,4635.0203,N,00020.0343,E,1,25,0.61,69.7,M,48.4,M,,*41;$GNRMC,180845.000,A,4635.0203,N,00020.0343,E,0.000,207.28,070124,,,A,V*36;$GNVTG,207.28,T,,M,0.000,N,0.000,K,A*2C;$GNGGA,180846.000,4635.0206,N,00020.0342,E,1,25,0.61,69.5,M,48.4,M,,*44;$GNRMC,180846.000,A,4635.0206,N,00020.0342,E,0.000,207.28,070124,,,A,V*31;$GNVTG,207.28,T,,M,0.000,N,0.000,K,A*2C"
   liste_chemin_absolu = chemin_absolu.split(';')
   infos = extract(liste_chemin_absolu)
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
   generer_html("../html/", "Résultats de l'analyse de trame GPS", infos, premier, resultat_positions_extremes["dernier_GGA"],
                    max_nord, min_sud, max_est, min_ouest, alt, max_vitesse, moyenne, min_vitesse)

if __name__ == "__main__":
    main()

print("Le programme s'est exécuté avec succès.")
