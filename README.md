# P21_API_conso_energie

Aude Guillaume Ludivine


#### Mise à disposition, à travers une API REST codée en python, des données sur la consommation d'énergie (Electricité et Gaz Naturel) en France.


Cette API a été réalisée en untilisant les données du portail opendata de [l'agence ORE](https://opendata.agenceore.fr/explore/dataset/conso-elec-gaz-annuelle-par-naf-agregee-iris/information/)

Pour la partie serveur :
- Fast API
- uvicorn
- MongoAtlas pour lhébergement des données, et pymongo pour la communication avec la base de données.

Pour la partie client :
- Flask
- Plotly pour la visualisation graphique

### Endpoints

- toutes les infos sur une filière : /filiere/<string:filiere>
- toutes les infos sur une région" : /region/<int:code_region>
- infos d'une document : /record/<string:recordid>
- modifier un document : /update/<string:recordid>
- supprimer un document : /delete/<string:recordid>
- consommations d'une filière par département: /filiere_dpt/<string:filiere>/<string:departement>


[Capture1.PNG](images/Capture1.PNG)
[Capture2.PNG](images/Capture2.PNG)
[Capture3.PNG](images/Capture3.PNG)


______

Requirements :
* `pip install plotly`
* `pip install Flask`
* `pip install Flask-PyMongo`
* `pip install fastapi`
* `pip install uvicorn`
* `pip install plotly`
______

Lien vers le tableau Trello : https://trello.com/b/Q6TWe6fp/energie

