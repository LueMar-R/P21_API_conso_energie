# -*- coding: utf-8 -*-

import requests 
from flask import jsonify, Flask, render_template, request, url_for, flash, redirect
import json

app= Flask(__name__)

URL_API = "http://127.0.0.1:8000"

@app.route("/")
def root():
	return {"message": "Bonjour, veuillez ajouter à la barre d'adresse le formulaire que vous souhaitez afficher",
	"toutes les infos sur une filière" : "/<string:filiere>",
	"toutes les infos sur une région" : "/<int:code_region>",
	"infos d'une document" : "/record/<string:recordid>",
	"consommations d'une filière par département":"/<string:filiere>/<string:departement>"}

@app.route("/filiere/<string:filiere>")
def get_filiere(filiere):
    reponse = requests.get(URL_API+"/filiere/"+filiere)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("filiere.html", data=content)

@app.route("/region/<string:region>")
def get_region(region):
    reponse = requests.get(URL_API+"/region/"+region)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("region.html", data=content['region'])

@app.route("/filiere_dpt/<string:filiere>/<string:departement>")
def depa(filiere, departement):
    reponse = requests.get(URL_API+"/"+filiere+"/"+departement)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("depa.html",  content=content["filiere"])

@app.route("/record/<string:recordid>")
def get_one(recordid):
    reponse = requests.get(URL_API+"/record/"+recordid)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("record.html", content=content)

@app.route("/update/<string:recordid>", methods=['GET', 'POST'])
def update_one(recordid):
    if request.method == 'POST':
        nconso = str(request.form.get("relev"))
        maj = {'fields.conso': nconso}
        requests.put(URL_API+"/update/"+recordid+"?nconso="+nconso)
        return "relevé de consommation mis-à-jour"

@app.route("/delete/<string:recordid>")
def delete_one(recordid):
    reponse = requests.delete(URL_API+"/delete/"+recordid)	
    return "document supprimé"

if __name__ == "__main__" :
    app.run(debug=True, port=5001)