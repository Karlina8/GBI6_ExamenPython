# NOMBRE (Sevillano,Karla):

from Bio import Entrez 
from Bio import SeqIO 

def download_pubmed(D): 
    """
    Mi keyword es Diabetes, esta es la entrada para descargar la data.txt 
    """
    Entrez.email = "karla.sevillano@est.ikiam.edu.ec"
    handle = Entrez.esearch(db="pubmed", 
                        term="DIABETES [Title/Abstract]",
                        usehistory="y")
    record = Entrez.read(handle)
    """
    Se genera una lista de python con todos lo IDs de PUBMED de los articulos de DIABETES y se genera el codigo para la descarga con el         nombre diabetes.txt
    """
    id_list = record["IdList"]
    record["Count"] 
    webenv = record["WebEnv"]
    query_key = record["QueryKey"]
    handle = Entrez.efetch(db="pubmed",
                       rettype="medline", 
                       retmode="text", 
                       retstart=0,
    retmax=613881, webenv=webenv, query_key=query_key)
    out_handle = open("data/diabetes_ec.txt", "w")
    data = handle.read()
    handle.close()
    out_handle.write(data)
    out_handle.close()
    return id_list
   
def science_plots(K):
    
    """
    Conecto la funcion 1 para generar un pie_plot 
    """ 
    
    with open(data, errors="ignore") as l: 
        texto = l.read()
    texto = re.sub(r"\n\s{6}", " ", texto)
    countries_1 = re.findall (r"AD\s{2}-\s[A-Za-z].,\s([A-Za-z])\.\s", texto)
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
    plt.show()

    
