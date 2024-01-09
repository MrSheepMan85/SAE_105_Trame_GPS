# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:27:15 2023

@author: zorrilla
"""
import analyse_de_trames_NMEA_GPS

#### VITESSES ####
def vit_moyenne(trajet):
    """
    Calcule la vitesse moyenne d'un trajet à partir des données extraites des trames GPS.

    Auteur : Etienne
    Date de création : 30/12/23
    Dernière modification : 30/12/23

    Paramètres :
    - trajet (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - Le trajet doit contenir des dictionnaires avec les données des trames GPS incluant la vitesse.

    Retour :
    - Un nombre représentant la vitesse moyenne calculée à partir des données du trajet.
      Si le trajet est vide, la fonction retourne 0.

    Exemple d'utilisation :
    >>> vit_moyenne([
    ...     {'VTG': {'vit': '005.5'}},
    ...     {'VTG': {'vit': '010.0'}},
    ...     {'VTG': {'vit': '007.2'}},
    ... ])
    # Résultat : 7.566666666666666
    """ 
    trame = 'analyse_de_trames_NMEA_GPS/trame.txt'  
    trajet = extract(trame)
    total = 0
    for i in trajet:
        total+= float(i['VTG']['vit'])
    return total/len(trajet)



def vit_min(trajet):
    """
    Détermine la vitesse minimale d'un trajet à partir des données extraites des trames GPS.

    Auteur : Etienne
    Date de création : 30/12/23
    Dernière modification : 30/12/23

    Paramètres :
    - trajet (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - Le trajet doit contenir des dictionnaires avec les données des trames GPS incluant la vitesse.

    Retour :
    - Un nombre représentant la vitesse minimale extraite des données du trajet.
      Si le trajet est vide, la fonction retourne 0.

    Exemple d'utilisation :
    >>> vit_min([
    ...     {'VTG': {'vit': '005.5'}},
    ...     {'VTG': {'vit': '010.0'}},
    ...     {'VTG': {'vit': '007.2'}},
    ... ])
    # Résultat : 5.5
    """
    trame = 'analyse_de_trames_NMEA_GPS/trame.txt'  
    trajet = extract(trame)
    min= 10000000000000000.0
    for i in trajet:
        vit = float(i['VTG']['vit'])
        if vit < min:
            min = vit
    return min

def vit_max(trajet):
    """
    Détermine la vitesse maximale d'un trajet à partir des données extraites des trames GPS.

    Auteur : [Nom de l'auteur]
    Date de création : [Date de création]
    Dernière modification : [Date de dernière modification]

    Paramètres :
    - trajet (list) : Une liste de dictionnaires contenant les informations extraites des trames GPS.

    Bornes d'utilisation :
    - Le trajet doit contenir des dictionnaires avec les données des trames GPS incluant la vitesse.

    Retour :
    - Un nombre représentant la vitesse maximale extraite des données du trajet.
      Si le trajet est vide, la fonction retourne 0.

    Exemple d'utilisation :
    >>> vit_max([
    ...     {'VTG': {'vit': '005.5'}},
    ...     {'VTG': {'vit': '010.0'}},
    ...     {'VTG': {'vit': '007.2'}},
    ... ])
    # Résultat : 10.0
    """
    trame = 'analyse_de_trames_NMEA_GPS/trame.txt'  
    trajet = extract(trame)
    min= -1.0
    for i in trajet:
        vit = float(i['VTG']['vit'])
        if vit > min:
            vit_max = vit
    return vit_max

    
