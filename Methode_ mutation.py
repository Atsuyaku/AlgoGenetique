#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:47 2019

@author: mdt2874a
"""

import numpy.random as npr
import math as m
import matplotlib.pyplot as plt

npr.seed(10)

villes = []

villes = npr.rand(250,2)

#nombre d'iterations du processus
const =1000

#print villes


#afficher les coordonnees de toutes les villes   
'''
for i in range(len(villes)):
    print ('ville', i, ':')
    print ('abscisse:', villes[i][0])
    print ('ordonnee:', villes[i][1])
'''
def dist(ville1, ville2):
    return m.sqrt(((villes[ville1][0]-villes[ville2][0])**2)+((villes[ville1][1]-villes[ville2][1])**2))

def ordre():
    #crée un tableau de 10 villes, puis stocke cet ordre dans villesOrdre
    villesOrdre = []
    j = 1
    for j in range (j,len(villes)):
        villesOrdre.append(j)
        
    #print villesTemp
    #print "\r"
    
    return villesOrdre
    

#villesOrdre = ordre()

#calcule la distance totale d'un trajet. Prend le numero du parcours en entree (issu de villesOrdre)
def calculerDistTrajet(villesOrdre):
    distTemp = 0
    i = 0
    for i in range(i,(len(villes)-2)):
        distTemp += dist(villesOrdre[i],villesOrdre[i+1])
        
    return (dist(0,villesOrdre[0]) + distTemp + dist(villesOrdre[len(villes)-2],0))

def afficherOrdre(liste):
    ordre = "0, "
    i = 0
    for i in range(i,len(liste)):
        ordre += str(liste[i])
        ordre += ", "
    ordre += "0"
    return ordre


def meilleurTrajet():
    i = 0
    villesOrdre = ordre()
    mutation = villesOrdre[:]
    #print (mutation)
    #print (villesOrdre)
    meilleur = calculerDistTrajet(villesOrdre)
    for i in range(i,const-1):
 
        #affecte des valeurs aléatoires à rand1 et rand2 (qui s'échangerons ensuite)
        rand1 = npr.randint(1,len(villes))
        
        #print ("rand1:",rand1)
        
        rand2 = npr.randint(1,len(villes))
        
        #print ("rand2:",rand2)
        #print ("\n")
        
        #change la valeur aléatoire 2 si elle est égale a la valeur aléatoire 1 (pour ne pas l'échanger avec elle-même)
        while rand1 == rand2:
            rand2 = npr.randint(1,len(villes))
            #print ("rand2:",rand2)
            #print ("\n")
            
        if rand1 > rand2: #sans définir d'ordre, si la premiere valeur changée est la plus petite, le seconde annulera le changement
            
            #échange la valeur aléatoire 2 à la place de la valeur initialle 1
            c = 0;
            while villesOrdre[c] != rand1:
                c += 1
            villesOrdre[c] = rand2
            
            #échange la valeur aléatoire 1 à la place de la valeur initialle 2
            c = 0;
            while villesOrdre[c] != rand2:
                c += 1
            villesOrdre[c] = rand1
        else:
            #échange la valeur aléatoire 1 à la place de la valeur initialle 2
            c = 0;
            while villesOrdre[c] != rand2:
                c += 1
            villesOrdre[c] = rand1
            
             #échange la valeur aléatoire 2 à la place de la valeur initialle 1
            c = 0;
            while villesOrdre[c] != rand1:
                c += 1
            villesOrdre[c] = rand2
        
        #vérifie si le nouveau trajet est plus court et le remplace en conséquence
        if (meilleur > calculerDistTrajet(villesOrdre)): 
            mutation = villesOrdre[:]
            meilleur = calculerDistTrajet(villesOrdre)
            #print ("Nouvel ordre: ",villesOrdre)
        else:
            villesOrdre = mutation[:]
         
        #print ("Trajet: ",calculerDistTrajet(villesOrdre))
        #print (mutation)
        #print (villesOrdre)
        
    meilleur = calculerDistTrajet(villesOrdre)
    print ("\n")
    print ("Le trajet le plus court est le trajet",afficherOrdre(villesOrdre)," (Distance: ", meilleur ,")")
    
    #affichage graphique du meilleur chemin
    abs = []
    ord = []
    i = 0
    abs.append(villes[0][0])
    ord.append(villes[0][1])
    for i in range(i, len(villes)-1):
        abs.append(villes[villesOrdre[i]][0])
        ord.append(villes[villesOrdre[i]][1])
    abs.append(villes[0][0])
    ord.append(villes[0][1])
      
    
    fig = plt.figure(1, figsize=(14, 12))
    plt.plot(abs,ord, color='darkred', marker='o', linestyle='dashed')
    plt.arrow(villes[0][0],villes[0][1],villes[villesOrdre[0]][0]-villes[0][0],villes[villesOrdre[0]][1]-villes[0][1],head_width= 0.03)
    plt.title("Meilleur chemin : " + afficherOrdre(villesOrdre) + "\n Meilleure distance : " + str(meilleur))
    plt.show
    
    

 

meilleurTrajet()
