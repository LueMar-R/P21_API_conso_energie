"""
endpoints :
    les données pour une filière (soit gaz, soit électricité),
    les données pour une région,
    les données pour une filière et une région,
    la consommation total pour une filière,
    supprimer un document précis,
    modifier un document précis,
    la consommation d'une filière pour un département
"""
from pymongo import MongoClient
from flask_pymongo import PyMongo

CONNECTION_STRING ='mongodb+srv://Aude:coucou@clusterdon.ngy1c.mongodb.net/energie?retryWrites=true&w=majority'

class DataAccess :

    @classmethod 
    def connexion(cls):
        cls.client = MongoClient(CONNECTION_STRING)
        cls.db = cls.client.energie.data

    @classmethod
    def deconnexion(cls):
        cls.client.close()

     #les données pour une filière (soit gaz, soit électricité),

    @classmethod
    def get_filiere(cls, filiere):
        cls.connexion()
        result = cls.db.find({"fields.filiere": filiere}, {"_id":0})
        result = result[:30]
        cls.deconnexion()
        return list(result)

    @classmethod #les données pour une région
    def get_region(cls, region):
        cls.connexion()
        result = cls.db.find({"fields.code_region": region}, {"_id":0})
        cls.deconnexion()
        return list(result)

    @classmethod #la consommation total pour une filière
    def get_total_filiere(cls, filiere):
        cls.connexion()
        result = db.aggregate( [ 
        	{"$match":{"fields.filiere": "Gaz"}},
        	{"$group":{"_id" : "$fields.filiere","total":{"$sum":"$fields.conso"}}} 
        	] )  
        cls.deconnexion()
        return list(result)

    @classmethod #la consommation d'une filière pour un département
    def get_dpt_filiere(cls, filiere, dpt):
        cls.connexion()
        result = cls.db.aggregate( [ 
        	{"$match":{"fields.filiere": filiere, "fields.code_departement": dpt }}, 
        	{"$group":{"_id" : "$fields.code_departement", "total":{"$sum":"$fields.conso"}}} 
        	] )
        cls.deconnexion()
        return list(result)

    @classmethod #rechercher un document précis
    def get_one(cls, recordid):
        cls.connexion()
        doc = cls.db.find({"recordid":recordid}, {"_id":0})
        cls.deconnexion()
        return list(doc)

    @classmethod #modifier un document précis
    def update_one(cls, recordid, dico_doc):
        cls.connexion()
        cls.db.update_one({"recordid": recordid}, {'$set':dico_doc})
        cls.deconnexion()
        return (recordid)
        

    @classmethod #supprimer un document précis
    def delete_one(cls, recordid):
        cls.connexion()
        cls.db.delete_one({"recordid":recordid})
        cls.deconnexion()
        return "suppression"