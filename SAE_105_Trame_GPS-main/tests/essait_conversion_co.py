# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:14:27 2024

@author: Etienne
"""

def convertir_sud_nord_et_ouest_est(lat, long):
    nouvelle_lat = -lat
    nouvelle_long = -long
    
    return nouvelle_lat, nouvelle_long

# Exemple d'utilisation avec des coordonnées négatives :
coordonnees_sud = 10.1234
coordonnees_ouest = -15.6789

inverse_sud_nord = convertir_sud_nord_et_ouest_est(coordonnees_sud, 0)
inverse_ouest_est = convertir_sud_nord_et_ouest_est(0, coordonnees_ouest)

print("Conversion Sud en Nord :", inverse_sud_nord)
print("Conversion Ouest en Est :", inverse_ouest_est)
