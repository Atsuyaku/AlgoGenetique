# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:30:35 2019

@author: thoma
"""

import numpy.random as npr
import math as m
import matplotlib.pyplot as plt

npr.seed(10)

villes = []
nbVilles = 250
villes = npr.rand(nbVilles,2)


#nombre d'iterations du processus
const =10

def dist(ville1, ville2):
    return m.sqrt(((villes[ville1][0]-villes[ville2][0])**2)+((villes[ville1][1]-villes[ville2][1])**2))

def melange():
    #crée un tableau de nbVilles villes et mélange leur ordre i fois, puis stocke ces ordres dans villesOrdre
    i = 0
    villesTemp =[]
    j = 1
    for j in range (j,nbVilles):
        villesTemp.append(j)
        
    #print villesTemp
    #print "\r"
    villesOrdre = []
    l=[]
    for i in range (i,nbVilles):
        npr.shuffle(villesTemp)
        #print "post shuffle"
        #print villesTemp
        #print "\r"
        l=villesTemp[:]
        villesOrdre.append(l)
        #print "post append: "
    #print (villesOrdre)
        #print "\r"
    return villesOrdre

def calculerDistTrajet(villesOrdre):
    distTemp = 0
    i = 0
    for i in range(i,(nbVilles-2)):
        distTemp += dist(villesOrdre[i],villesOrdre[i+1])
        
    return (dist(0,villesOrdre[0]) + distTemp + dist(villesOrdre[nbVilles-2],0))




def meilleurTrajet():
    i = 0
    villesOrdre = melange()
    nouvelOrdre = []
    mutation = villesOrdre[0]
    #print (mutation)
    #print (nouvelOrdre)
    #print (villesOrdre)
    meilleur = calculerDistTrajet(villesOrdre[0])
    for i in range(i,const-1):
        del nouvelOrdre[:]
        #affecte des valeurs aléatoires à rand1 et rand2 (deux tuples qu'on croisera)
        rand1 = npr.randint(0,nbVilles-1)
        
        #print ("rand1:",rand1)
        
        rand2 = npr.randint(0,nbVilles-1)
        
        #print ("rand2:",rand2)
        #print ("\n")
        
        #change la valeur aléatoire 2 si elle est égale a la valeur aléatoire 1 (pour ne pas l'échanger avec elle-même)
        while rand1 == rand2:
            rand2 = npr.randint(0,nbVilles-1)
            #print ("rand2:",rand2)
            #print ("\n")
        
        #affecte des valeurs aléatoires à dec1 et dec2, les deux extrémités de la découpe
        dec1 = npr.randint(0,nbVilles-1)
        
        #print ("dec1:",dec1)
        
        dec2 = npr.randint(0,nbVilles-1)
        
        #print ("dec2:",dec2)
        #print ("\n")
        
        #print("tuple1", villesOrdre[rand1])
        #print("tuple2", villesOrdre[rand2])
        #change la valeur aléatoire 2 si elle est égale a la valeur aléatoire 1 (pour ne pas l'échanger avec elle-même)
        while dec1 == dec2:
            dec2 = npr.randint(0,nbVilles-1)
            #print ("dec2:",dec2)
            #print ("\n")
        
        if dec1 > dec2:
            decTemp = dec2
            dec2 = dec1
            dec1 = decTemp
            
        #print ("dec1: ", dec1)
        #print ("dec2: ", dec2)    
        
        #découpes des deux tuples
        i = dec1
        dtuple1=[]
        dtuple2=[]
        dtupleTemp1=[]
        dtupleTemp2=[]
        for i in range(i, dec2):
            #print (i)
            if (i <= len(villesOrdre[0])):
                dtupleTemp1.append(villesOrdre[rand1][i])
                dtupleTemp2.append(villesOrdre[rand2][i])
                
        dtuple1.extend(dtupleTemp1)
        dtuple2.extend(dtupleTemp2)
            
        #print ("dtuple1: ", dtuple1)
        #print ("dtuple2: ", dtuple2)
        
        #verification des ville manquantes
        manq2 = dtuple1[:]
        manq1 = dtuple2[:]
        #print(manq1)
        #print(manq2) 
        c = 0
        while (c < len(manq1)):
            #print ("c: ", c)
            e = 0
            while (e < len(manq2)):
                #print ("e: ", e)
                if manq1[c] == manq2[e]:
                    manq1.pop(c)
                    manq2.pop(e)
                    #print(manq1)
                    #print(manq2)
                    e = 0
                    c = 0
                else:
                    e += 1
            else:   
                c+= 1
        #print(manq1)
        #print(manq2)    

        
        
        #séparer les découpes du reste
        unDebut = False
        if (dec1 != 0):
            unDebut = True
            debut1 = []
            debutTemp1 = []
            
            for i in villesOrdre[rand1][0:dec1]:
                debutTemp1.append(i)
            debut1.extend(debutTemp1)
            
            debut2 = []
            debutTemp2 = []
            for i in villesOrdre[rand2][0:dec1]:
                debutTemp2.append(i)
            debut2.extend(debutTemp2)
            
            #print("debut1: ",debut1)
            #print("debut2: ",debut2)
        uneFin = False
        if (dec2 < len(villesOrdre[0])):
            uneFin = True
            fin1 = []
            finTemp1 = []
            
            i = 0
            for i in villesOrdre[rand1][dec2:len(villesOrdre[0])]:
               finTemp1.append(i)
            fin1.extend(finTemp1)
            
            fin2 = []
            finTemp2 = []
            i = 0
            for i in villesOrdre[rand2][dec2:len(villesOrdre[0])]:
               finTemp2.append(i)
            fin2.extend(finTemp2)
            
            #print("fin1: ",fin1)
            #print("fin2: ",fin2)

        
        #remplacer les doublons par les valeurs manquantes si besoin
        #on compare le debut (s'il y en a un) avec dtuple et s'il y a un doublon on le remplace (dans le debut) par un nb manquant (le premier qui passe) puis on le supprime des manquants
        if (unDebut):
            c = 0   
            while (c < len(debut1)):
                #print ("c: ", c)
                e = 0
                while (e < len(dtuple2)):
                    #print ("e: ", e)
                    if debut1[c] == dtuple2[e]:
                        #print(manq2)
                        debut1[c] = manq2[0]
                        #print("debut1: ",debut1)
                        #print(manq2)
                        manq2.pop(0)
                    e += 1
                c+= 1
                
            c = 0   
            while (c < len(debut2)):
                #print ("c: ", c)
                e = 0
                while (e < len(dtuple1)):
                    #print ("e: ", e)
                    if debut2[c] == dtuple1[e]:
                        #print(manq1)
                        debut2[c] = manq1[0]
                        #print("debut2: ",debut2)
                        #print(manq1)
                        manq1.pop(0)
                    e += 1
                c+= 1
                
        #on fait pareil avec la fin(s'il y a une fin)
        if (uneFin):
            c = 0   
            while (c < len(fin1)):
                #print ("c: ", c)
                e = 0
                while (e < len(dtuple2)):
                    #print ("e: ", e)
                    if fin1[c] == dtuple2[e]:
                        fin1[c] = manq2[0]
                        #print ("dtuple2: ", dtuple2)
                        manq2.pop(0)
                        #print("Manq2: ",manq2)
                    e += 1
                c+= 1
            
            c = 0   
            while (c < len(fin2)):
                #print ("c: ", c)
                e = 0
                while (e < len(dtuple1)):
                    #print ("e: ", e)
                    if fin2[c] == dtuple1[e]:
                        fin2[c] = manq1[0]
                        #print ("dtuple1: ", dtuple1)
                        manq1.pop(0)
                        #print("Manq1: ",manq1)
                    e += 1
                c+= 1
        """        
         #normalement quand on a verifie debut et fin on devrait ne plus avoir de manquant
        if (unDebut) :
            print("debut1: ",debut1)
            print("debut2: ",debut2)
        
        print ("dtuple2: ", dtuple2)
        print ("dtuple1: ", dtuple1)
        
        if (uneFin):
            print("fin1: ",fin1)
            print("fin2: ",fin2)
       """
        #reconstruire les deux tuples enfants
        enfant1 = []
        if (unDebut):
            enfant1.extend(debut1)
        enfant1.extend(dtuple2)
        if (uneFin):
            enfant1.extend(fin1)
            
       
        
        enfant2 = []
        if (unDebut):
            enfant2.extend(debut2)
        enfant2.extend(dtuple1)
        if (uneFin):
            enfant2.extend(fin2)
        #print("\n")  
        #print ("Enfant1: ", enfant1)
        #print ("Enfant2: ", enfant2)
            #creer deux nouveaux tuples contenants respectivements dans l'ordre: un debut(s'il y a), un dtuple, une fin (s'il y a)
            
    nouvelOrdre = enfant1

        #print ("nouvelOrdre: ",nouvelOrdre)
        #vérifie si le nouveau trajet est plus court et le remplace en conséquence
    if (meilleur > calculerDistTrajet(nouvelOrdre)): 
        mutation = nouvelOrdre[:]
        meilleur = calculerDistTrajet(nouvelOrdre)
        
    if (calculerDistTrajet(enfant2) < meilleur): 
        mutation = enfant2
        meilleur = calculerDistTrajet(mutation)
        #print ("Nouvel ordre: ",villesOrdre)
            
    #print ("Trajet: ",calculerDistTrajet(villesOrdre))
    #print (mutation)
    #print (villesOrdre)
    print ("\n")
    print ("Le trajet le plus court est le trajet",afficherOrdre(mutation)," (Distance: ", meilleur ,")")
    
    #affichage graphique du meilleur chemin
    abs = []
    ord = []
    i = 0
    abs.append(villes[0][0])
    ord.append(villes[0][1])
    for i in range(i, len(villes)-1):
        abs.append(villes[mutation[i]][0])
        ord.append(villes[mutation[i]][1])
    abs.append(villes[0][0])
    ord.append(villes[0][1])
        
    
    fig = plt.figure(1, figsize=(14, 12))
    plt.plot(abs,ord, color='darkred', marker='o', linestyle='dashed')
    plt.arrow(villes[0][0],villes[0][1],villes[mutation[0]][0]-villes[0][0],villes[mutation[0]][1]-villes[0][1],head_width= 0.03)
    plt.title("Meilleur chemin : " + afficherOrdre(mutation) + "\n Meilleure distance : " + str(meilleur))
    plt.show
        
def afficherOrdre(liste):
    ordre = "0, "
    i = 0
    for i in range(i,len(liste)):
        ordre += str(liste[i])
        ordre += ", "
    ordre += "0"
    return ordre




meilleurTrajet()