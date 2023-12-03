
corps = """
    <!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titre}</title>
</head>
  <body>  
<h1> Les trames GPS </h1>
    <p>Nous vous présentons comment extraire des informations d'une trame GPS</p>
    <p>Une trame GPS ce divise en plusieurs informations très utilises pour la marine.</p>
    <p>Dans cette trame, on y retrouve l'équipement qui a généré, la trame, un code d'identification de la trame 
    et les donnÃ©es qui consernent la trame.</p>
    <p>Nous vous proposons donc un lecture plus facile d'une trame GPS de type de la norme NMEA 0183</p>
    <table>
<tr>
    <td> positions de la trame</td>
    <td> positions de départ</td>
    <td> position d’arrivée</td>
    <td>positions les plus au nord</td>
    <td>position les plus au sud</td>
    <td> position les plus à l'est </td>
    <td> la position la plus élevée</td>
    <td> la distance parcourue</td>
    <td> la vitesses moyenne </td>
    <td> la vitesses minimal </td>
    <td> la vitesses maximal</td>
</tr>
<tr>
    <td>{a}</td>
</tr>
<tr>
    <td>{b}</td>
</tr>
<tr>
    <td>{c}</td>
    <td>{test}</td>
</tr>
<tr>
    <td>{d}</td>
    <td>{e}</td>
</tr>
</table>

   </body> 
</html>"""
def genere_page_web(nom_fichier, titre_page, corps):
   
    fich = open(nom_fichier, mode='w', encoding='utf-8')
    fich.write(corps.format(titre=titre_page, a= ,b= ,))
    fich.close()
if __name__=="__main__":
    main() 
    
#importer il faut pour un fichier superieur: import "..fichier au dessus" sans .py
#import un fichier en desous: import nomfichierracine.nomfichier   pour une fonction précise faire from nomdufichier import lafonction