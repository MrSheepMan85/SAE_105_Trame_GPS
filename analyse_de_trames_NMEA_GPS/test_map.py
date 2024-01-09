import matplotlib.pyplot as plt
import contextily as ctx

def generate_map(data, center, zoom, filename):
    # Extraction des coordonnées
    nord = [d['nord'] for d in data]
    est = [d['est'] for d in data]

    # Tracer le trajet
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(est, nord, marker='o', linestyle='-', color='blue')
    ax.set_title('Tracé du trajet GPS')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.grid(True)

    # Ajouter la carte OpenStreetMap en arrière-plan avec le centre et le zoom spécifiés
    ctx.add_basemap(ax, crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik, zoom=zoom)
    
    plt.savefig(filename)  # Sauvegarde en tant qu'image PNG
    plt.show()

centre = (48.8566, 2.3522)  # Coordonnées (latitude, longitude) du centre
zoom = 5  # Niveau de zoom
nom_fichier_html = 'carte_trajet.html'  # Nom du fichier HTML de sortie

donnees_gps = [
    {'nord': 48.8534, 'est': 2.3488},
    {'nord': 48.8566, 'est': 2.3522},
    {'nord': 48.8584, 'est': 2.3523},
]

generate_map(donnees_gps, center=centre, zoom=zoom, filename='carte_trajet.PNG')



