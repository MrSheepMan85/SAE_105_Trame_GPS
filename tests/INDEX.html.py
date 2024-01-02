def sep_trame(trame_gps):
    return trame_gps.split(",")

def horaire(time_section):
    heure = time_section[0:2]
    minutes = time_section[2:4]
    secondes = time_section[4:6]
    milli = time_section[7:10]
    return (heure, minutes, secondes, milli)

def date(date_section):
    jour = date_section[0:2]
    mois = date_section[2:4]
    annee = date_section[4:6]
    return (jour, mois, annee)

def parse_coo(section):
    coo = section.split(".")
    deg = coo[0]
    minutes = coo[1]
    return deg, minutes

def info_trame(trame_GPS):
    section = sep_trame(trame_GPS)
    TYPE = section[0][3:]
    if TYPE == "GGA":
        return info_trame_gga(section)
    elif TYPE == "VTG":
        return info_trame_vtg(section)
    elif TYPE == "RMC":
        return info_trame_rmc(section)
    else:
        return None

def info_trame_gga(section):
    infos = {}
    infos["type"] = section[0]
    infos["horaire"] = horaire(section[1])
    infos["nord"] = parse_coo(section[2])
    infos["est"] = parse_coo(section[4])
    infos["nbsat"] = section[7]
    infos["alt"] = section[9]
    return infos

def info_trame_vtg(section):
    infos = {}
    infos["type"] = section[0]
    infos["vit"] = section[7]
    return infos

def info_trame_rmc(section):
    infos = {}
    infos["type"] = section[0]
    infos["date"] = date(section[9])
    return infos

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
     </section>
      <footer>
           <p>Réalisé par CHAILLOU Matthieu et ZORILLA Etienne</p>
        </footer>
    </body>
    </html>

        """
        fichier.write(corps)


def main():
    trame_gps = "$GPGGA,165538.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
    infos = info_trame(trame_gps)
    genere_page_web("exemple.html", "Résultats de l'analyse de trame GPS", infos)

if __name__ == "__main__":
    main()
