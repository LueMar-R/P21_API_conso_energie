from fastapi import FastAPI
import uvicorn
from data import DataAccess as da

api = FastAPI()

@api.get("/")
async def root():
    return {"message": "Bonjour, veuillez ajouter à la barre d'adresse le formulaire que vous souhaitez afficher"}

# obtenir toutes les infos d'une filière OKOKOK
@api.get("/filiere/{filiere}")
def read_item(filiere: str):
    result4 =da.get_filiere(filiere)
    return result4

# obtenir toutes les infos concernant une région OKOKOK
@api.get("/region/{region}")
def get(region: int):
    result3 = da.get_region(region)
    return result3

# obtenir les infos sur un document OKOKOK
@api.get("/record/{recordid}")
def get(recordid: str):
    result1 = da.get_one(recordid)
    return result1

# obtenir les infos d'un document OKOKOK
@api.put("/update/{recordid}")
def update_one(recordid: str, nconso : str):
    dico_doc={"fields.conso": nconso}
    result2 = da.update_one(recordid, dico_doc)
    return "mise à jour", 200

# supprimer un document précis OKOKOK
@api.delete("/delete/{recordid}")
def delete_one(recordid: str):
    da.delete_one(recordid)
    return "suppression ok", 204


@api.get("/filiere_dpt/{filiere}/{dpt}")
def filiere_dpt(filiere: str, dpt:str):
    result = da.get_dpt_filiere(filiere, dpt)
    return {"filiere": result}


@api.get("/all_region")
def all_region():
    da.connexion()
    result = da.get_all_region()
    da.deconnexion()
    return {"all_region": result}

@api.get("/conso/{region}")
def conso(region: str):
    da.connexion()
    result = da.get_elec_gaz(region)
    info_region = da.info_region(region)
    da.deconnexion()
    return {"conso": result, "info_region": info_region}





if __name__ == '__main__':
    uvicorn.run(api, debug=True)