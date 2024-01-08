import folium
from analyse_de_trames_NMEA_GPS import info_trame
from analyse_de_trames_NMEA_GPS import extract_coordinates, parse_coo

def get_coordinates_sections_2_4(pos):
    """
    Extrait et transforme les coordonnées des sections 2 et 4 des trames GPS.

    Auteur : Etienne
    Date de création : 30/12/23
    Dernière modification : 30/12/23

    Paramètres :
    - pos (list) : Liste de dictionnaires contenant les informations extraites des trames GPS.
    
    Bornes d'utilisation :
    - La liste pos doit contenir des dictionnaires conformes à la norme NMEA avec les données des trames GPS.

    Retour :
    - Une liste de dictionnaires, chaque dictionnaire contenant les coordonnées transformées des sections 2 et 4.
      Chaque dictionnaire contient deux clés : 'section_2' et 'section_4', associées aux coordonnées transformées.
      Si aucune information de coordonnées n'est trouvée pour une section, le dictionnaire correspondant est omis.

    Exemple d'utilisation :
    >>> get_coordinates_sections_2_4([
    ...     {'GGA': {'nord': '4836.5375', 'est': '00740.9373'}},
    ...     {'GGA': {'nord': '4837.1234', 'est': '00741.5678'}},
    ... ])
    # [
    #     {'section_2': [48.610625, 7.682288333333333], 'section_4': [48.61872333333333, 7.692796666666667]},
    #     {'section_2': [48.61872333333333, 7.692796666666667], 'section_4': [48.62122333333333, 7.692796666666667]}
    # ]
    """
    coordinates_sections_2_4 = []
    for p in pos:
        if 'gga' in p:
            for trame in p['gga']:
                section_2 = trame.get('nord')  # Changer 'nord' ou 'est' selon la section souhaitée
                section_4 = trame.get('est')   # Changer 'nord' ou 'est' selon la section souhaitée
                
                if section_2 is not None and section_4 is not None:
                    # Appliquer la transformation sur les données
                    coord_section_2 = parse_coo(section_2)
                    coord_section_4 = parse_coo(section_4)
                    
                    # Ajouter les coordonnées transformées à la liste
                    coordinates_sections_2_4.append({'section_2': coord_section_2, 'section_4': coord_section_4})
    
    return coordinates_sections_2_4



pos = extract(path_to_data)

# Récupération des coordonnées de la liste 'gga'
coordinates_gga = get_coordinates_from_gga(pos['gga'])

# Création de la carte centrée sur la première position de la liste 'gga'
if coordinates_gga:
    first_position = coordinates_gga[0]
    carte = folium.Map(location=(first_position['section_2'], first_position['section_4']), zoom_start=12)

    # Création d'une liste pour les coordonnées
    latitude_longitude = [(coord['section_2'], coord['section_4']) for coord in coordinates_gga]

    # Tracé du trajet à partir des coordonnées
    folium.PolyLine(locations=latitude_longitude, color='blue').add_to(carte)

    # Enregistrer la carte dans un fichier HTML
    carte.save('trajet_gps.html')
else:
    print("Aucune donnée de coordonnées 'gga' disponible.")