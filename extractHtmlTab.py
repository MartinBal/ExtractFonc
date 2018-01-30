# -*- coding: utf-8 -*-
"""
Manipulation des données foncière issues de tables html normalisées
"""

from bs4 import BeautifulSoup
import os

path='C:\\Users\\Martin Ballot\\Dropbox (PERMAGRO)\\2.CLIENTS\\ADV\\3_TRAVAIL\\CADASTRE\\BAUX_PROPRIETE'
file="PAT_RDP_SC_PATACHE_BEGADAN_III.html"

os.chdir(path)

def get_soup(file):
    '''Open the html file and transform it into a processible DOM bs'''
    f=open(file,"r")
    html=f.read()
    soup=BeautifulSoup(html, 'html.parser')
    f.close()
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
    #print([(dic["N°PLAN"],	dic["SECTION"],dic["N°PARC PRIM"],dic["CONTENANCE HA  A  CA"]) for dic in data if dic["N°PLAN"]!='\xa0'])	
    #print(len([(dic["N°PLAN"],	dic["SECTION"],dic["N°PARC PRIM"],dic["CONTENANCE HA  A  CA"]) for dic in data if dic["N°PLAN"]!='\xa0']))	
    return data
#possibilité de vérifier la somme des surfaces



soup=get_soup(file)
tablesList=get_propTables(soup,'PROPRIETES NON BATIES')
data=get_Data(tablesList)


nextCOM= False 
nextDEP=False
for cell in soup.find('table').find_all('td'):
    if nextCOM : 
        com = cell.string
        nextCOM=False
    elif nextDEP: 
        dep = cell.string
        nextDEP=False
    if cell.string=='COM' : 
        nextCOM=True
    elif  cell.string=='DEP DIR':
        nextDEP=True
print(dep,com)


headers=[]
for d in data:
    for k in d.keys():
        if k not in headers : headers.append(k)
print (headers)

f = open('PERM_'+file[:-5]+'.csv', 'w')
f.write('id;'+';'.join(headers)+';MFV_lien\n')
for d in data:
    values=[]
    if 'N°PLAN'in d.keys() and 'SECTION'in d.keys() and d['N°PLAN']!='\xa0' and d['SECTION']!='\xa0':
        ID = dep[:2]+com[:3]+'000'+'{:0>2}'.format(d["SECTION"])+'{:0>4}'.format(d["N°PLAN"])
        values.append(ID)
        for h in headers:
            if h in d.keys():
                values.append(d[h])
            else: values.append('')
        print(d)
        print(values) 
        line= ';'.join(values)+';'+file+'\n'
        print (line)
        f.write(line)
f.close()