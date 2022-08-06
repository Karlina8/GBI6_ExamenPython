# NOMBRE (Sevillano,Karla):
import Bio
from Bio.Seq import Seq
from Bio import Entrez
import re

def download_pubmed (keyword):
    """
    Se inicia con una funcion con un parametro de entrada llamado, keyword, esta funcion hace que se guarde la data para el llamado en otras     funciones
    """ 
    Entrez.email = "karla.sevillano@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term=keyword+"[Title]",
                        usehistory="y")
    record = Entrez.read(handle)
    id_list = record["IdList"]
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text", 
                       retstart=0,
                       retmax=543, 
                       webenv=webenv,
                       query_key=query_key)

    out_handle = open(keyword+".txt", "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list 

import re 
import matplotlib.pyplot as plt
from collections import Counter

def science_plots(data):
    """
    Se genera una funcion que se conecte con la funcion un 1, y pueda ayudar a descargar la data y se refleje en un grafico tipo pastel con     los autores de los paises 
    """ 
    with open(data, errors="ignore") as p: 
        text = p.read()
    text = re.sub(r"\n\s{6}", " ", text)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].*,\s([A-Za-z]*)\.\s", text)
    unique_countries = list(set(countries_1))
    conteo=Counter(countries_1)
    resultado={}
    for clave in conteo:  
        valor=conteo[clave]
        if valor > 1:
            resultado[clave] = valor
    ordenar = (sorted(resultado.values()))
    ordenar.sort(reverse=True)
    import operator
    pais = []
    contador = []
    
    reverse = sorted(resultado.items(), key=operator.itemgetter(1), reverse=True)   
    for name in enumerate(reverse):
        pais.append(name[1][0])
        contador.append(resultado[name[1][0]])
    five_p = pais[0:5] 
    five_c = contador [0:5]
    fig = plt.figure(figsize =(10, 7))
    plt.pie(five_c, labels = five_p)
    (plt.savefig(data +'.jpg', dpi=300, bbox_inches='tight'))
    plt.show()

    