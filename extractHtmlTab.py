# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from bs4 import BeautifulSoup
import os

os.chdir('C:\\Users\\Martin Ballot\\Dropbox (PERMAGRO)\\6.PROJETS\\6.1.Plateforme\\Brainstorming\\Script\\ExtractionDonneesFoncieresHTML\\data')

html=open("RELEVE DE PROPRIETE SC CHATEAU PATACHE D AUX ST CHRISTOLY.html","r").read()
soup=BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

title=soup.title.string
print(title)





for table in  soup.find_all('table'):
    #print(table.prettify())
    typeProp=''
    col=[]
    dict_col={}
    for row in table.find_all('tr'):
        if len(row.find_all('td'))==1 : 
            typeProp=row.get_text()
            print(typeProp)
        elif typeProp=='PROPRIETES NON BATIES':
            if len(row.find_all('td'))>len(col):
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
    