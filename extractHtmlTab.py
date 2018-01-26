# -*- coding: utf-8 -*-
"""
Manipulation des données foncière issues de tables html normalisées
"""

from bs4 import BeautifulSoup
import os

path='C:\\Users\\Martin Ballot\\Dropbox (PERMAGRO)\\6.PROJETS\\6.1.Plateforme\\Brainstorming\\Script\\ExtractionDonneesFoncieresHTML\\data'
file="RELEVE DE PROPRIETE SC CHATEAU PATACHE D AUX ST CHRISTOLY.html"

os.chdir(path)

def get_soup(file):
    '''Open the html file and transform it into a processible DOM bs'''

    html=open(file,"r").read()
    soup=BeautifulSoup(html, 'html.parser')
    return soup


def get_propTables(soup, typeProp):
    '''extract tables on the criteria: the first cell text match the typeProp string'''
    #We could have selected the table based on there span
    
    tablesList=[]
    for table in soup.find_all('table'):
        if table.td.string == typeProp: #attention aux comparaison trop strictes
            tablesList.append(table)
    print ('numTables',len(tablesList))
    
    return tablesList

def get_Data(tablesList):
    '''extract all the colum data as a dictionaries list'''
    
    data=[]
    for table in tablesList:
        numCols=int(table.attrs['cols'])
        for row in table.find_all('tr'):
            if len(row)>=numCols:
                cel=[c.string for c in row.find_all('td')]
                if row.td.attrs['class']==['TitreC']:
                    col=cel
                else:
                    dic={}
                    for i in range(numCols):
                        dic[col[i]]=cel[i]
                    data.append(dic)
    print([(dic["N°PLAN"],	dic["SECTION"],dic["N°PARC PRIM"],dic["CONTENANCE HA  A  CA"]) for dic in data if dic["N°PLAN"]!='\xa0'])	
    print(len([(dic["N°PLAN"],	dic["SECTION"],dic["N°PARC PRIM"],dic["CONTENANCE HA  A  CA"]) for dic in data if dic["N°PLAN"]!='\xa0']))	

#possibilité de vérifier la somme des surfaces

soup=get_soup(file)
tablesList=get_propTables(soup,'PROPRIETES NON BATIES')
get_Data(tablesList)