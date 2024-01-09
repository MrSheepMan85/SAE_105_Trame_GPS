import os
import analyse_de_trames_NMEA_GPS
from calcule import vit_max, vit_min, vit_moyenne

def genere_page_web(nom_fichier, titre_page, infos_trame):
    with open(nom_fichier, mode='w', encoding='utf-8') as fichier:
        corps = f"""
          <!DOCTYPE html>
     <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Résultats de l'analyse de trame GPS</title>
       <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <header>
            <h1>Résultats de l'analyse de trame GPS</h1>
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
                 <td>{infos_trame["type"]}</td>
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
        </table>

        <table>
                <tr>
                   <th>Plus au Nord</th>
                   <th>Plus au Sud</th>
                   <th>Plus au Ouest</th>
                   <th>Plus au Est</th>
                   <th>Plus élevé</th>
               </tr>
               <tr>
                 <td>{max_nord}</td>
                    <td>{min_sud}</td>
                    <td>{min_ouest}</td>
                   <td>{ min_ouest}</td>
                   <td>{alt}</td>
                </tr>

          </table>

          <table>
                <tr>
                   <th>Vitesse max</th>
                   <th>vitesse moyenne</th>
                   <th>vitesse minimal</th>
               </tr>
               <tr>
                 <td>{maxi}</td>
                    <td>{moyenne}</td>
                    <td>{mini}</td>
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
    infos = analyse_de_trames_NMEA_GPS.extract(chemin_absolu)
    print(infos)
    maxi = vit_max(infos)
    moyenne = vit_moyenne(infos)
    mini = vit_min(infos)
    resultat_positions_extremes = analyse_de_trames_NMEA_GPS.positions_extremes(infos)
    premier = analyse_de_trames_NMEA_GPS.premier_dernier_gga(infos)
    resultat_positions_extremes = analyse_de_trames_NMEA_GPS.positions_extremes(infos)
    max_nord = analyse_de_trames_NMEA_GPS.resultat_positions_extremes["max_nord"]
    min_sud = analyse_de_trames_NMEA_GPS.resultat_positions_extremes["min_sud"]
    max_est = analyse_de_trames_NMEA_GPS.resultat_positions_extremes["max_est"]
    min_ouest = analyse_de_trames_NMEA_GPS.resultat_positions_extremes["min_ouest"]
    alt = analyse_de_trames_NMEA_GPS.extract_high_alt(infos)
    genere_page_web("..//html/", "Résultats de l'analyse de trame GPS", infos)

if __name__ == "__main__":
    main()
