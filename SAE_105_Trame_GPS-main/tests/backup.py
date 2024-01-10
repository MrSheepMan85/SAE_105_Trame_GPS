from jinja2 import Environment
import sys
sys.path.append("../analyse_de_trames_NMEA_GPS")
from analyse_de_trames_NMEA_GPS import info_trame


def genere_page_web(nom_fichier, titre_page, corps,trame):
   
    fich = open(nom_fichier, mode='w', encoding='utf-8')
    info = info_trame()
    fich.write(corps.format(titre=titre_page,))
    fich.close()
if __name__=="__main__":
    with open("templates/template.html", mode ="r") as file:
       genere_page_web("site_analyse.html","acceuil",file.read()) 
    
#importer il faut pour un fichier superieur: import "..fichier au dessus" sans .py
#import un fichier en desous: import nomfichierracine.nomfichier   pour une fonction précise faire from nomdufichier import lafonction