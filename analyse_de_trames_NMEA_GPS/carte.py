import folium
from analyse_de_trames_NMEA_GPS import info_trame
from analyse_de_trames_NMEA_GPS import extract_coordinates, parse_coo

def get_coordinates_sections_2_4(pos):
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




path_to_data = 'votre_fichier_de_donnees.txt'
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