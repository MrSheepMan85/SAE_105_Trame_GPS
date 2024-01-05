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
    return trame_gps.split(",")

def horaire (time_section) :
    heure=time_section[0 : 2]
    minutes=time_section[2 : 4]
    secondes=time_section[4 : 6]
    milli=time_section[7 : 10]
    return (heure, minutes, secondes, milli)

def date(date_section):
    jour=date_section[0 : 2]
    mois=date_section[2 : 4]
    annee = date_section[4 : 6]
    return (jour, mois, annee)



def parse_coo(section):
    coo = section.split(".")
    deg = coo[0]
    minutes =coo[1]
    return(deg, minutes)

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
    
    # Vérification et traitement pour la section 3
    if section[3] == "S":
        infos["nord"] *= -1  # Multiplication par -1 si la section 3 est "S"
    
    infos["est"] = parse_coo(section[4])
    
    # Vérification et traitement pour la section 5
    if section[5] == "W":
        infos["est"] *= -1  # Multiplication par -1 si la section 5 est "W"
    
    infos["nbsat"] = section[7]
    infos["alt"] = section[9]
    return infos


def info_trame_vtg(trame_GPS):
    infos = {}
    infos["type"] = trame_GPS[0]
    infos["vit"] = trame_GPS[7]
    return infos

def info_trame_rmc(trame_GPS):
    infos = {}
    infos["type"] = trame_GPS[0]
    infos["date"] = date(trame_GPS[9])
    return infos

#### EXTRACTION DES TRAMES ####

def extract(path:str):
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

def extract_coo(pos):
    coordinates = []
    for p in pos:
        first_gga = p['gga'][0] if 'gga' in p and len(p['gga']) > 0 else None
        last_gga = p['gga'][-1] if 'gga' in p and len(p['gga']) > 0 else None
        
        coordinates.append({'first': first_gga, 'last': last_gga})
    
    return coordinates

def extremes_use_coo(extract_coo):
    max_nord = float('-inf')
    min_nord = float('inf')
    max_est = float('-inf')
    min_est = float('inf')
    trame_max_nord = None
    trame_min_nord = None
    trame_max_est = None
    trame_min_est = None
    
    for trame in extract_coo:
        first = trame['first']
        last = trame['last']
        
        # Comparaison des premières coordonnées
        if first['nord'] is not None:
            if first['nord'] > max_nord:
                max_nord = first['nord']
                trame_max_nord = first
            if first['nord'] < min_nord:
                min_nord = first['nord']
                trame_min_nord = first
        
        if first['est'] is not None:
            if first['est'] > max_est:
                max_est = first['est']
                trame_max_est = first
            if first['est'] < min_est:
                min_est = first['est']
                trame_min_est = first
        
        # Comparaison des dernières coordonnées
        if last['nord'] is not None:
            if last['nord'] > max_nord:
                max_nord = last['nord']
                trame_max_nord = last
            if last['nord'] < min_nord:
                min_nord = last['nord']
                trame_min_nord = last
        
        if last['est'] is not None:
            if last['est'] > max_est:
                max_est = last['est']
                trame_max_est = last
            if last['est'] < min_est:
                min_est = last['est']
                trame_min_est = last
    
    return {
        "max_nord": trame_max_nord,
        "min_nord": trame_min_nord,
        "max_est": trame_max_est,
        "min_est": trame_min_est
    }


def extract_high_alt(pos):
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



if __name__ == "__main__":
    path_to_data = 'votre_fichier_de_donnees.txt'
    
    alt = extract_high_alt(pos)
    coordinates_gga = extremes_use_coo(extract_coo)
    generate_map(coordinates_gga)
    vitmax = vit_max(max)













