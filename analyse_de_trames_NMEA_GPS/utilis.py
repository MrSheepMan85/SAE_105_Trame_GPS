# utils.py

def extract(path:str):
    """
    Extrait les informations des trames GPS conformes à la norme NMEA. Pour cela on utilise les fonction info_trame_rmc(), info_trame_vtg() et info_trame_gga()

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - path (str) : Le chemin du fichier contenant les trames GPS à analyser.

    Bornes d'utilisation :
    - Le fichier spécifié par le chemin doit contenir des trames GPS conformes à la norme NMEA.

    Retour :
    - Une liste de dictionnaires contenant les informations extraites des trames GPS.
      Chaque dictionnaire correspond aux informations extraites d'une trame, incluant le type et la date.
      Si aucune trame RMC, GGA ou VTG n'est trouvée, retourne une liste vide.

    Exemple d'utilisation :
    >>> extract('chemin/vers/le/fichier.txt')
    # [
    #     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94')}},
    #     {'GGA': {...}},
    #     {'VTG': {...}},
    # ]
    """
    pos = []
    with open(path, "r+") as f:
        index = 0
        pos.append({})
        for l in f:
            from analyse_de_trames_NMEA_GPS import info_trame 
            r = info_trame(l)
            if not r:
                continue
            pos[index][r['type'][3:]] = r
            if len(pos[index].keys()) == 3:
                index += 1
                pos.append({})
    return pos
