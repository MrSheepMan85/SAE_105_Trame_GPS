def genere_page_web(nom_fichier, titre_page, corps):
   pass
  
def main():
    fich = open("chemin_fichier", mode='w', encoding='us-ascii')
    print(fich)
    corps = """
    <!DOCTYPE html>
<html>
<head>
</head>
  <body>  
<h1> Les trames GPS </h1>
    <p>Nous vous présentons comment extraire des informations d'une trame GPS</p>
    <p>Une trame GPS ce divise en plusieurs informations très utilées pour la marine.</p>
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
    <td>22</td>
</tr>
<tr>
    <td>31</td>
    <td>32</td>
</tr>
</table>

   </body> 
</html>"""
    fich.write(corps)
    fich.close()
if __name__=="__main__":
    main() 