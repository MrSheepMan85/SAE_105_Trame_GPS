# calcule.py
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 7 10:27:15 2023

@author: zorrilla
"""

from analyse_de_trames_NMEA_GPS import extract

#### VITESSES ####
def vit_moyenne(liste_infos):
    """
    Calcule la vitesse moyenne extraite des trames GPS.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - liste_infos (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - La liste d'informations doit contenir des dictionnaires avec les données des trames GPS conformes à la norme NMEA.

    Retour :
    - Un nombre représentant la vitesse moyenne extraite des trames GPS.
      Si aucune information de vitesse n'est trouvée, la valeur retournée est `-inf`.

    Exemple d'utilisation :
    >>> vit_moyenne([
    ...     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'vit': '10.5'}},
    ...     {'GGA': {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'vit': '15.2'}},
    ...     {'VTG': {'type': '$GPVTG', 'vit': '20.0'}},
    ... ])
    # Résultat : vitesse moyenne extraite des trames GPS, par exemple, 15.9
    """
    total_vitesse = 0
    count = 0
    
    for i in liste_infos:
        if 'VTG' in i and 'vit' in i['VTG']:
            try:
                vitesse = float(i['VTG']['vit'])
                total_vitesse += vitesse
                count += 1
            except ValueError:
                continue  # Ignorer les valeurs de vitesse non valides
    
    if count > 0:
        moyenne = total_vitesse / count
        return moyenne
    else:
        return float('-inf')

def vit_min(liste_infos):
    """
    Identifie la vitesse minimale extraite des trames GPS.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - liste_infos (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - La liste d'informations doit contenir des dictionnaires avec les données des trames GPS conformes à la norme NMEA.

    Retour :
    - Un nombre représentant la vitesse minimale extraite des trames GPS.
      Si aucune information de vitesse n'est trouvée, la valeur retournée est `inf`.

    Exemple d'utilisation :
    >>> vit_min([
    ...     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'vit': '10.5'}},
    ...     {'GGA': {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'vit': '15.2'}},
    ...     {'VTG': {'type': '$GPVTG', 'vit': '20.0'}},
    ... ])
    # Résultat : vitesse minimale extraite des trames GPS, par exemple, 10.5
    """
    min_vitesse = float('inf')
    
    for i in liste_infos:
        if 'VTG' in i and 'vit' in i['VTG']:
            try:
                vitesse = float(i['VTG']['vit'])
                if vitesse < min_vitesse:
                    min_vitesse = vitesse
            except ValueError:
                continue  # Ignorer les valeurs de vitesse non valides
    
    if min_vitesse == float('inf'):
        return None  # Aucune vitesse trouvée
    else:
        return min_vitesse

def vit_max(liste_infos):
    """
    Identifie la vitesse maximale extraite des trames GPS.

    Auteur : Etienne
    Date de création : 26/12/23
    Dernière modification : 26/12/23

    Paramètres :
    - liste_infos (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - La liste d'informations doit contenir des dictionnaires avec les données des trames GPS conformes à la norme NMEA.

    Retour :
    - Un nombre représentant la vitesse maximale extraite des trames GPS.
      Si aucune information de vitesse n'est trouvée, la valeur retournée est `-inf`.

    Exemple d'utilisation :
    >>> vit_max([
    ...     {'RMC': {'type': '$GPRMC', 'date': ('19', '11', '94'), 'vit': '10.5'}},
    ...     {'GGA': {'type': '$GPGGA', 'horaire': ('06', '40', '36', '289'), 'vit': '15.2'}},
    ...     {'VTG': {'type': '$GPVTG', 'vit': '20.0'}},
    ... ])
    # Résultat : vitesse maximale extraite des trames GPS, par exemple, 20.0
    """
    max_vitesse = float('-inf')
    
    for i in liste_infos:
        if 'VTG' in i and 'vit' in i['VTG']:
            try:
                vitesse = float(i['VTG']['vit'])
            except ValueError:
                continue  # Ignorer les valeurs de vitesse non valides
            
            if vitesse > max_vitesse:
                max_vitesse = vitesse
    
    return max_vitesse
