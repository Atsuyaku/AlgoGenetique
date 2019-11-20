# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 14:37:05 2019

@author: thoma
"""
import math as m

"""
npr.seed(10)

villes = []

villes = npr.rand(10,2)
"""

villes = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9]]
const =10

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
    

villesOrdre = [1,2,3,7,5,6,4,8,9,10]

def calculerDistTrajet():
    distTemp = 0
    i = 0
    for i in range(i,(len(villes)-2)):
        distTemp += dist(villesOrdre[i],villesOrdre[i+1])
        
    return (dist(0,villesOrdre[0]) + distTemp + dist(villesOrdre[len(villes)-2],0))


print (calculerDistTrajet())


def afficherOrdre(liste):
    ordre = "0, "
    i = 0
    for i in range(i,len(liste)):
        ordre += str(liste[i])
        ordre += ", "
    ordre += "0"
    return ordre


print (afficherOrdre(villesOrdre))