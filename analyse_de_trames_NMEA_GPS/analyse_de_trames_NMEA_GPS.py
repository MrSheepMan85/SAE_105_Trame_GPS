#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:32:31 2023

@author: mchail09
"""
import calcule
import carte 

#### TRAITEMENT DES TRAMES ####
def sep_trame(trame_gps):
    """
    Permet de séparer les trames en section de données qui sont séparées par des virgules.
    
    Auteur : Matthieu
    Date de création : 30/10/23
    Dernière modification : 30/10/23
    
    Paramètres :
    - trame_gps (str) : La trame dans laquelle nous voulons séparer les informations.
    
    Bornes d'utilisation :
    - La trame doit être une trame de la norme NMEA.
    
    Retour :
    - Renvoie une liste d'éléments correspondant à la trame de la norme NMEA sous la forme de différentes sections.
    
    Exemple d'utilisation :
    >>> sep_trame('$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E')
    ['$GPGGA', '064036.289', '4836.5375', 'N', '00740.9373', 'E', '1', '04', '3.2', '200.2', 'M', '', '', '', '0000*0E']
    """
    return trame_gps.split(",")


def horaire(time_section):
    """
    Permet de récupérer l'heure dans une section de temps d'une trame GPS précédemment découpée en sections.

    Auteur : Matthieu (version originale) puis retravaillée par Etienne
    Date de création : 30/10/23
    Dernière modification : 16/11/23

    Paramètres :
    - time_section (str) : La section temporelle de la trame GPS dans laquelle récupérer l'heure.

    Bornes d'utilisation :
    - La section temporelle doit être extraite d'une trame conforme à la norme NMEA.

    Retour :
    - Un tuple contenant l'heure, les minutes, les secondes et les millisecondes extraits de la section temporelle.

    Exemple d'utilisation :
    >>> horaire('064036.289')
    ('06', '40', '36', '289')
    """
    heure = time_section[0:2]
    minutes = time_section[2:4]
    secondes = time_section[4:6]
    millisecondes = time_section[7:10]
    return (heure, minutes, secondes, millisecondes)


def date(date_section):
    """
    Permet de récupérer la date dans une section temporelle d'une trame GPS précédemment découpée en sections.

    Auteur : Etienne
    Date de création : 30/10/23
    Dernière modification : 16/11/23

    Paramètres :
    - date_section (str) : La section temporelle de la trame GPS dans laquelle récupérer la date.

    Bornes d'utilisation :
    - La section temporelle doit être extraite d'une trame conforme à la norme NMEA.

    Retour :
    - Un tuple contenant le jour, le mois et l'année extraits de la section temporelle.

    Exemple d'utilisation :
    >>> date('061123')
    ('06', '11', '23')
    """
    jour = date_section[0:2]
    mois = date_section[2:4]
    annee = date_section[4:6]
    return (jour, mois, annee)



def parse_coo(section):
    """
    Permet de séparer une section de coordonnées d'une trame GPS précédemment découpée en sections.

    Auteur : Matthieu (version originale) puis retravaillée par Etienne
    Date de création : 30/10/23
    Dernière modification : 16/11/23

    Paramètres :
    - section (str) : La section de coordonnées de la trame GPS à séparer.

    Bornes d'utilisation :
    - La section de coordonnées doit être extraite d'une trame conforme à la norme NMEA.

    Retour :
    - Un tuple contenant les degrés et les minutes extraites de la section de coordonnées.

    Exemple d'utilisation :
    >>> parse_coo('4836.5375')
    ('4836', '5375')
    """
    coo = section.split(".")
    deg = coo[0]
    minutes = coo[1]
    return (deg, minutes)

def info_trame(trame_GPS):
    """
    Analyse et extrait les informations d'une trame GPS conformément à la norme NMEA.

    Auteur :  Matthieu (version originale) puis retravaillée par Etienne
    Date de création : 30/10/23
    Dernière modification : 26/12/23

    Paramètres :
    - trame_GPS (str) : La trame GPS à analyser pour extraire les informations.

    Bornes d'utilisation :
    - La trame GPS doit être conforme à la norme NMEA.

    Retour :
    - Les informations extraites de la trame GPS selon son type (GGA, VTG, RMC) ou None si le type n'est pas pris en charge.

    Exemple d'utilisation :
    >>> info_trame('$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E')
    # (Résultat dépendra du type de trame et de la fonction correspondante utilisée: 
    si la trame est une gga alors on return info_trame_gga(section) 
    si c'est une vtg on return info_trame_vtg(section)
    si c'est une rmc on returninfo_trame_rmc(section)
    sinon on ne return rien 
"""
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
    """
    Analyse et extrait les informations d'une trame GPS conforme à la norme NMEA de type GGA.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - section (list) : Une liste des éléments de la trame GPS à analyser pour extraire les informations.

    Bornes d'utilisation :
    - La section doit être conforme à la norme NMEA et correspondre au type GGA.

    Retour :
    - Un dictionnaire contenant les informations extraites de la trame GPS GGA, incluant le type, l'heure, 
      les coordonnées nord et est, le nombre de satellites, et l'altitude. 
      Si la section ne correspond pas au type GGA, retourne None.

    Exemple d'utilisation :
    >>> info_trame_gga(['$GPGGA', '064036.289', '4836.5375', 'N', '00740.9373', 'E', '1', '04', '3.2', '200.2', 'M', '', '', '', '0000*0E'])
    {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'nord': ('4836', '5375'), 'est': ('00740', '9373'), 'nbsat': '1', 'alt': '200.2'}
    """
    infos = {}
    infos["type"] = section[0]
    infos["horaire"] = horaire(section[1])
    infos["nord"] = parse_coo(section[2])
    
    # Vérification et traitement pour la section 3
    if section[3] == "S":
        infos["nord"] *= -1  # Inversion si la section 3 est "S"
    
    infos["est"] = parse_coo(section[4])
    
    # Vérification et traitement pour la section 5
    if section[5] == "W":
        infos["est"] *= -1  # Inversion si la section 5 est "W"
    
    infos["nbsat"] = section[7]
    infos["alt"] = section[9]
    return infos


def info_trame_vtg(trame_GPS):
    """
    Analyse et extrait les informations d'une trame GPS conforme à la norme NMEA de type VTG.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - trame_GPS (list) : Une liste des éléments de la trame GPS à analyser pour extraire les informations.

    Bornes d'utilisation :
    - La trame GPS doit être conforme à la norme NMEA et correspondre au type VTG.

    Retour :
    - Un dictionnaire contenant les informations extraites de la trame GPS VTG, incluant le type et la vitesse. 
      Si la trame ne correspond pas au type VTG, retourne None.

    Exemple d'utilisation :
    >>> info_trame_vtg(['$GPVTG', '054.7', 'T', '034.4', 'M', '005.5', 'N', '...', 'E*68'])
    {'type': '$GPVTG', 'vit': '005.5'}
    """
    infos = {}
    infos["type"] = trame_GPS[0]
    infos["vit"] = trame_GPS[7]
    return infos


def info_trame_rmc(trame_GPS):
    """
    Analyse et extrait les informations d'une trame GPS conforme à la norme NMEA de type RMC.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - trame_GPS (list) : Une liste des éléments de la trame GPS à analyser pour extraire les informations.

    Bornes d'utilisation :
    - La trame GPS doit être conforme à la norme NMEA et correspondre au type RMC.

    Retour :
    - Un dictionnaire contenant les informations extraites de la trame GPS RMC, incluant le type et la date.
      Si la trame ne correspond pas au type RMC, retourne None.

    Exemple d'utilisation :
    >>> info_trame_rmc(['$GPRMC', '225446', 'A', '4916.45', 'N', '12311.12', 'W', '000.5', '054.7', '191194', '020.3', 'E*68'])
    {'type': '$GPRMC', 'date': ('19', '11', '94')}
    """
    infos = {}
    infos["type"] = trame_GPS[0]
    infos["date"] = date(trame_GPS[9])
    return infos

#### EXTRACTION DES TRAMES ####

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
            r = info_trame(l)
            if not r:
                continue
            pos[index][r['type'][3:]] = r
            if len(pos[index].keys()) == 3:
                index += 1
                pos.append({})
    return pos


def positions_extremes(liste_infos):
    """
    Identifie les coordonnées extrêmes Nord, Sud, Est et Ouest à partir d'une liste d'informations de trames GPS.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - liste_infos (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - La liste d'informations doit contenir des dictionnaires avec les données des trames GPS conformes à la norme NMEA.

    Retour :
    - Un dictionnaire contenant les coordonnées les plus au Nord, au Sud, à l'Est et à l'Ouest.
      Chaque clé du dictionnaire correspond à une direction cardinale, associée aux coordonnées extrêmes.
      Si aucune information de coordonnées n'est trouvée, les valeurs correspondantes sont None.

    Exemple d'utilisation :
    >>> positions_extremes([
    ...     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'nord': 50, 'est': -100}},
    ...     {'GGA': {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'nord': 60, 'est': -80}},
    ...     {'VTG': {'type': '$GPVTG', 'vit': '005.5', 'nord': 70, 'est': -120}},
    ... ])
    # {
    #     'max_nord': {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'nord': 50, 'est': -100}},
    #     'min_sud': None,
    #     'max_est': None,
    #     'min_ouest': {'VTG': {'type': '$GPVTG', 'vit': '005.5', 'nord': 70, 'est': -120}}
    # }
    """
    max_nord = float('-inf')
    min_sud = float('inf')
    max_est = float('-inf')
    min_ouest = float('inf')
    coord_nord = None
    coord_sud = None
    coord_est = None
    coord_ouest = None
    
    for infos in liste_infos:
        nord = infos.get("nord")
        est = infos.get("est")
        
        if nord is not None:
            if nord > max_nord:
                max_nord = nord
                coord_nord = infos
        
            if nord < min_sud:
                min_sud = nord
                coord_sud = infos
        
        if est is not None:
            if est > max_est:
                max_est = est
                coord_est = infos
            
            if est < min_ouest:
                min_ouest = est
                coord_ouest = infos
    
    return {
        "max_nord": coord_nord,
        "min_sud": coord_sud,
        "max_est": coord_est,
        "min_ouest": coord_ouest
    }

def extract_high_alt(pos):
    """
    Identifie l'altitude maximale extraite des trames GPS.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - pos (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - La liste d'informations doit contenir des dictionnaires avec les données des trames GPS conformes à la norme NMEA.

    Retour :
    - Un nombre représentant l'altitude maximale extraite des trames GPS.
      Si aucune information d'altitude n'est trouvée, la valeur retournée est `-inf`.

    Exemple d'utilisation :
    >>> extract_high_alt([
    ...     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'nord': 50, 'est': -100}},
    ...     {'GGA': {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'nord': 60, 'est': -80}},
    ...     {'VTG': {'type': '$GPVTG', 'vit': '005.5', 'nord': 70, 'est': -120}},
    ... ])
    # Résultat : altitude maximale extraite des trames GPS, par exemple, 70.0
    """
    max_altitude = float('-inf')
    
    for p in pos:
        if 'gga' in p:
            for trame in p['gga']:
                altitude = trame.get('alt')
                
                if altitude is not None:
                    altitude = float(altitude)  # Convertir l'altitude en nombre
                    
                    if altitude > max_altitude:
                        max_altitude = altitude
    
    return max_altitude
















