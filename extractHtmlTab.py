# -*- coding: utf-8 -*-
"""
Manipulation des données foncière issues de tables html normalisées
"""

from bs4 import BeautifulSoup
import os

path='C:\\Users\\Martin Ballot\\Dropbox (PERMAGRO)\\6.PROJETS\\6.1.Plateforme\\Brainstorming\\Script\\ExtractionDonneesFoncieresHTML\\data'
file="RELEVE DE PROPRIETE SC CHATEAU PATACHE D AUX ST CHRISTOLY.html"

os.chdir(path)

def get_soup(path,file):
    '''ouvre le fichier et tranforme sous forme d'un DOM bs'''
    html=open(file,"r").read()
    soup=BeautifulSoup(html, 'html.parser')
    return soup

soup=get_soup(path,file)

def get_prop(soup):
    '''parse le DOM pour extraire les données pertinente des tableau'''
    for table in  soup.find_all('table'):
        typeProp=''
        col=[]
        dict_col={}
        for row in table.find_all('tr'):
            if len(row.find_all('td'))==1 :#detect the title rows (=the one cell rows)
                typeProp=row.get_text()
                print(typeProp)
            elif typeProp=='PROPRIETES NON BATIES':#select only in "propriétes non baties" tables
                if len(row.find_all('td'))>len(col):#we'll considere that sub-title rows are always shorter (less cells) than real data rows
                    col=[c.text for c in row.find_all('td')]
                    print(col)
                else:
                    i=0
                    print(row.prettify())
                    print(' - '*10)
                    for c in row.find_all('td'):
                        if c.text!='\xa0':
                            dict_col[col[i]]=c.text
                        i+=1
                    if 'N°PLAN' in dict_col.keys():
                        print(dict_col)
    
            #print(row.get_text())
                        print(' - '*33)
        print('-'*100)

get_prop(soup)