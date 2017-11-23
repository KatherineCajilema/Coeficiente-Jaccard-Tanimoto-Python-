import math
from threading import Thread
import threading
import time 
import csv
list=[]
def T(elema,elemb):
    
    elem1={}
    elem2={}
    elem3={}
    NA=0
    NB=0
    NC=0
    tanimoto=0
   
    t1=threading.Thread(target=comparador,args=(elema,elem1,))
    t2=threading.Thread(target=comparador,args=(elemb,elem2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
   
    
    for i in range (0,len(elem1)):
        if elem2.has_key(elem1.keys()[i])==1:
            a=elem1.get(elem1.keys()[i])
            b=elem2.get(elem1.keys()[i])
            c=min(a,b)
            elem3.update({elem1.keys()[i]:c})
   

    for i in range(0,len(elem1.values())):
        NA+=elem1.values()[i]
    for i in range(0,len(elem2.values())):
        NB+=elem2.values()[i]
    for i in range(0,len(elem3.values())):
        NC+=elem3.values()[i]
	
    tanimoto=NC/(float(NA+NB-NC))
 
    return tanimoto


def jaccardTanimoto(elemA, elemB):
     lista=[]
     lista.insert(1,[elemA,elemB,round(T(elemA,elemB),2)])
  
     
    # for i in range (i,len(lista)):
     #   print lista[i]
     #print list
     end=time.time()
     #print end-start	
     return lista
     
     #print end-start
def comparador (compuesto, diccionario):
     for i in range(0,len(compuesto)):
	if compuesto[i]=='@':
		diccionario.update({compuesto[i]:1})
	elif diccionario.get(compuesto[i])>=1:
		diccionario.update({compuesto[i]:1+diccionario[compuesto[i]]})
	else: 
		diccionario.update({compuesto[i]:1}) 
     return diccionario 
     
def main(x,y):
	for i in range(1,y):
		for j in range(i+1,y):
                
	        	#print formula[i],formula[j]
		 jaccardTanimoto(formula[i],formula[j])
                
        
                 list.insert(1,[formula[i],formula[j],round(T(formula[i],formula[j]),2)])
                 csvfin = open('salidakatetrue1.csv', 'w')
                 fin = csv.writer(csvfin)
                 fin.writerow(['COMPONENTE_A', 'COMPONENTE_B','VALUE'])
                 fin.writerows(list)
                 del fin
                 csvfin.close()
doc = open("ZINC_chemicals.tsv", "r")
formula = []
start=time.time()
for linea in doc.readlines():
	lineas = doc.readlines()
	formula.append((linea.split('\t'))[1].strip('\n'))
doc.close() 




			
t3=threading.Thread(target=main,args=(1,6072,))
t4=threading.Thread(target=main,args=(6073,8587,))
t5=threading.Thread(target=main,args=(8588,10517,))
t6=threading.Thread(target=main,args=(10518,12144,))
t3.start()
t4.start()
t5.start()
t6.start()
t3.join()
t4.join()
t5.join()
t6.join()
