#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:32:31 2023

@author: mchail09
"""




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
    infos["est"] = parse_coo(section[4])
    infos["nbsat"] = section[7]
    infos["alt"] = section[9]
    return infos

def info_trame_vtg(trame_GPS):
    infos = {}
    infos["type"] = section[0]
    infos["vit"] = section[7]
    return infos

def info_trame_rmc(trame_GPS):
    infos = {}
    infos["type"] = section[0]
    infos["date"] = date(section[9])
    return infos

def 
#file=open()



if __name__ == "__main__":
    trame_gps= "$GPGGA,165538.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
    info = info_trame(trame_gps)
    print("Type de trame :", info["type"])
    print("Heure de la trame :" , info["horaire"][0] , "heures", info["horaire"][1], "minutes" , info["horaire"][2] , "secondes" ,info["horaire"][3] , "milli-secondes")
    print("Coordonnées Nord :", info["nord"][0],"degrés", info["nord"][1],"minutes" )
    print("Coordonnées Est :", info["est"][0],"degrés", info["est"][1],"minutes" )
    print("satellites en poursuite :" , info["nbsat"])
    print("Altitude :", info["alt"])











