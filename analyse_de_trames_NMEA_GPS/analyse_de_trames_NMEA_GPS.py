#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:32:31 2023

@author: mchail09
"""

trame_gps= "$GPGGA,165538.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E"
list_split=trame_gps.split(",")


print(list_split)


def horaire (trame_gps) :
    temps=list_split[1]
    heure=temps[0 : 2]
    minutes=temps[2 : 4]
    secondes=temps[4 : 6]
    milli=temps[7 : 10]
    return(heure, minutes, secondes, milli)
(h, m, s, ms)=horaire(trame_gps)


def nord (trame_gps):
    co_nord=list_split[2]
    co_nord=co_nord.split(".")
    deg_n=co_nord[0]
    minutes_n=co_nord[1]
    return(deg_n, minutes_n)
(deg_n, minutes_n)=nord(trame_gps)


def est (trame_gps):
    co_est=list_split[4]
    co_est=co_est.split(".")
    deg_e=co_est[0]
    minutes_e=co_est[1]
    return(deg_e, minutes_e)
(deg_e, minutes_e)=est(trame_gps)

def sat (trame_gps):
    nbsat=list_split[7]
    return (nbsat)
(nbsat)=sat(trame_gps)

def alt (trame_gps):
    altitude=list_split[9]
    return (altitude)
(altitude)=alt(trame_gps)

file=open()














print("Type de trame :", list_split[0])
print("Heure de la trame :" , h , "heures", m, "minutes" , s , "secondes" , ms , "milli-secondes")
print("Coordonnées Nord :", deg_n,"degrés", minutes_n,"minutes" )
print("Coordonnées Est :", deg_e,"degrés", minutes_e,"minutes" )
print("satellites en poursuite :" , nbsat)
print("Altitude :", altitude)
