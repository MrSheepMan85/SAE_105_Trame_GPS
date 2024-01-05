# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:27:15 2023

@author: zorrilla
"""
from analyse_de_trames_NMEA_GPS import info_trame

#### VITESSES ####
def vit_moyenne(trajet):
    total = 0
    for i in trajet:
        total+= float(i['VTG']['vit'])
    return total/len(trajet)

def vit_min(trajet):
    min= 10000000000000000.0
    for i in trajet:
        vit = float(i['VTG']['vit'])
        if vit < min:
            min = vit
    return min

def vit_max(trajet):
    min= -1.0
    for i in trajet:
        vit = float(i['VTG']['vit'])
        if vit > min:
            vit_max = vit
    return vit_max

    
