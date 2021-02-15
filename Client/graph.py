import plotly
import plotly.express as px
import json
import pandas as pd

class Graph:

    def graph_bar_conso(self, elec, gaz):
        data_encode = px.bar(y=[elec,gaz],color=["Electricité","Gaz"])
        graphJSON = json.dumps(data_encode, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON

    def graph_sunburst_info_region(self, data):
        d = {"filiere":[],"operateur":[] ,"conso":[], "libelle_departement":[]}
        for i in data:
            for y in i["fields"].keys():
                d[y].append(i["fields"][y])
        df = pd.DataFrame(d)
        # df = pd.DataFrame(list(data))
        # df2 = pd.DataFrame(list(df['fields']))
        fig = px.sunburst(df, path=['filiere', 'operateur', 'libelle_departement'], values='conso')
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    
