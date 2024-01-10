import folium
import analyse_de_trames_NMEA_GPS 


def génération_map(data):
  """
    Génère une carte représentant un trajet à partir des données de coordonnées extraites des trames GPS.

    Paramètres :
    - data (list) : Une liste de dictionnaires contenant les données de coordonnées extraites des trames GPS.
                    Chaque dictionnaire devrait contenir les clés 'nord' et 'est' pour chaque trame GGA.

    Usage :
    génération_map(data)
    
    La fonction crée une carte centrée sur la première coordonnée de la liste fournie, puis trace le trajet
    en utilisant des marqueurs circulaires à chaque point de coordonnées extraites des trames GGA.
    La carte est sauvegardée dans un fichier HTML nommé 'carte_trajet.html'.
    """
    # Création de la carte centrée sur une position de départ (par exemple, première coordonnée)
m = folium.Map(location=[data[0]['nord'], data[0]['est']], zoom_start=12)

    # Traçage du trajet en utilisant les coordonnées extraites des trames GGA
for d in data:
        folium.CircleMarker(location=[d['nord'], d['est']], radius=3, color='blue').add_to(m)

    # Sauvegarde de la carte dans un fichier HTML
m.save('carte_trajet.html')

# Extraction des données des trames GPS depuis un fichier
trames_gps = extract('SAE_105_Trame_GPS/data/trame.txt')

# Génération de la carte avec le trajet à partir des données extraites des trames GPS
génération_map(trames_gps)