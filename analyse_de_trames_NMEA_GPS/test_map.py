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
    ctx.add_basemap(ax, crs='EPSG:4326', source=ctx.providers.OpenStreetMap.Mapnik)
    ax.set_extent((min(est), max(est), min(nord), max(nord)))

    plt.savefig(filename)  # Sauvegarde en tant qu'image PNG
    ctx.plot_map(ax, source=ctx.providers.OpenStreetMap.Mapnik)  # Ajout de la carte au tracé
    
    plt.show()

# Exemple de données de coordonnées (à remplacer par vos propres données)
donnees_gps = [
    {'nord': 48.8534, 'est': 2.3488},
    {'nord': 48.8566, 'est': 2.3522},
    {'nord': 48.8584, 'est': 2.3523},
    # ... Ajoutez vos données de coordonnées extraites des trames GPS ici ...
]

# Centre et zoom pour la région que vous souhaitez afficher (ex: Paris)
centre = (48.8566, 2.3522)  # Coordonnées (latitude, longitude) du centre
zoom = 12  # Niveau de zoom

# Nom du fichier HTML de sortie
nom_fichier_html = 'carte_trajet.html'

# Génération du tracé du trajet à partir des données extraites des trames GPS et sauvegarde en HTML
generate_map(donnees_gps, center=centre, zoom=zoom, filename=nom_fichier_html)



