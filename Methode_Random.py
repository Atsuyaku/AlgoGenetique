#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:37:59 2019

@author: mdt2874a
"""

import numpy.random as npr
import math as m
import matplotlib.pyplot as plt

npr.seed(10)

villes = []

villes = npr.rand(250,2)


const =1000

#print villes


#afficher les coordonnees de toutes les villes   
"""
for i in range(len(villes)):
    print ('ville', i, ':')
    print ('abscisse:', villes[i][0])
    print ('ordonnee:', villes[i][1])
"""

def dist(ville1, ville2):
    return m.sqrt(((villes[ville1][0]-villes[ville2][0])**2)+((villes[ville1][1]-villes[ville2][1])**2))

def melange():
    #crée un tableau de 10 villes et mélange leur ordre i fois, puis stocke ces ordres dans villesOrdre
    i = 0
    villesTemp =[]
    j = 1
    for j in range (j,len(villes)):
        villesTemp.append(j)
        
    #print villesTemp
    #print "\r"
    villesOrdre = []
    l=[]
    for i in range (i,const):
        npr.shuffle(villesTemp)
        #print "post shuffle"
        #print villesTemp
        #print "\r"
        l=villesTemp[:]
        villesOrdre.append(l)
        #print "post append: "
    #print villesOrdre
        #print "\r"
    return villesOrdre
    

villesOrdre = melange()

#calcule la distance totale d'un trajet. Prend le numero du parcours en entree (issu de villesOrdre)
def calculerDistTrajet(numOrdre):
    distTemp = 0
    i = 0
    for i in range(i,(len(villes)-2)):
        distTemp += dist(villesOrdre[numOrdre][i],villesOrdre[numOrdre][i+1])
        
    return (dist(0,villesOrdre[numOrdre][0]) + distTemp + dist(villesOrdre[numOrdre][len(villes)-2],0))


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
    meilleur = calculerDistTrajet(0)
    for i in range(i,const-1):
        #print calculerDistTrajet(i)
        if (meilleur > calculerDistTrajet(i)):
            meilleur = calculerDistTrajet(i)
            idTrajet = i
            
    print ("\n")
    print ("Le trajet le plus court est le trajet",afficherOrdre(villesOrdre[idTrajet])," (Distance: ", meilleur ,")") 
    
    #affichage graphique du meilleur chemin
    abs = []
    ord = []
    i = 0
    abs.append(villes[0][0])
    ord.append(villes[0][1])
    for i in range(i, len(villes)-1):
        abs.append(villes[villesOrdre[idTrajet][i]][0])
        ord.append(villes[villesOrdre[idTrajet][i]][1])
    abs.append(villes[0][0])
    ord.append(villes[0][1])
        
    fig = plt.figure(1, figsize=(14, 12))
    plt.plot(abs,ord, color='darkred', marker='o', linestyle='dashed')
    plt.arrow(villes[0][0],villes[0][1],villes[villesOrdre[idTrajet][0]][0]-villes[0][0],villes[villesOrdre[idTrajet][0]][1]-villes[0][1],head_width= 0.03)
    plt.title("Meilleur chemin : " + afficherOrdre(villesOrdre[idTrajet]) + "\n Meilleure distance : " + str(meilleur))

 

meilleurTrajet()

