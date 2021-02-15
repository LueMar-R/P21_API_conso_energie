# -*- coding: utf-8 -*-

import requests 
from flask import jsonify, Flask, render_template, request, url_for, flash, redirect
import json
import plotly.express as px
from graph import Graph
import plotly

app= Flask(__name__)

URL_API = "http://127.0.0.1:8000"

@app.route("/")
def root():
	return {"Bienvenue": "Veuillez ajouter à la barre d'adresse le formulaire que vous souhaitez afficher",
	"toutes les infos sur une filière" : "/filiere/<string:filiere>",
	"toutes les infos sur une région" : "/region/<int:code_region>",
	"infos d'une document" : "/record/<string:recordid>",
    "modifier un document" : "/update/<string:recordid>",
    "supprimer un document" : "/delete/<string:recordid>",
	"consommations d'une filière par département":"/filiere_dpt/<string:filiere>/<string:departement>"}

@app.route("/filiere/<string:filiere>")
def get_filiere(filiere):
    reponse = requests.get(URL_API+"/filiere/"+filiere)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("filiere.html", data=content)

@app.route("/region/<string:region>")
def get_region(region):
    reponse = requests.get(URL_API+"/region/"+region)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("region.html", data=content)

@app.route("/filiere_dpt/<string:filiere>/<string:departement>")
def depa(filiere, departement):
    reponse = requests.get(URL_API+"/filiere_dpt/"+filiere+"/"+departement)
    content = json.loads(reponse.content.decode("utf-8"))
    return render_template("depa.html", data=content)

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


@app.route("/dashboard/<string:dpt>",methods=('GET','POST'))
def html(dpt):
    if request.method =='POST':
        dpt = str(request.values.get('dep'))
        reponse = requests.get(URL_API+"/all_region")
        all_region = json.loads(reponse.text)

        reponse = requests.get(URL_API+"/conso/"+dpt)
        conso = json.loads(reponse.text)["conso"]
        graphJSON = Graph().graph_bar_conso(conso["elec"], conso["gaz"])
        total = conso["elec"] + conso["gaz"]

        info_region = json.loads(reponse.text)["info_region"]
        graphJSON2 = Graph().graph_sunburst_info_region(info_region)

        return render_template("index.html", region=all_region["all_region"], plot=graphJSON, plot2=graphJSON2, total=total, reg=dpt)

    reponse = requests.get(URL_API+"/all_region")
    all_region = json.loads(reponse.text)

    reponse = requests.get(URL_API+"/conso/"+dpt)
    conso = json.loads(reponse.text)["conso"]
    graphJSON = Graph().graph_bar_conso(conso["elec"], conso["gaz"])
    total = conso["elec"] + conso["gaz"]

    info_region = json.loads(reponse.text)["info_region"]
    graphJSON2 = Graph().graph_sunburst_info_region(info_region)

    return render_template("index.html", region=all_region["all_region"], plot=graphJSON, plot2=graphJSON2, total=total, reg=dpt)


if __name__ == "__main__" :
    app.run(debug=True, port=5001)