# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 09:38:34 2017

@author: Korisnik
"""

"""
DOMAĆI ZADATAK 2:

Napravite mini rečnik sinonima i antonima pod promenljivom "rečnik" tako što
ćete odabrati 3 reči i pronaći uz njih barem 2 antonima i 2 sinonima.

Strukura koju napišete treba da omogući da:
    - Komanda print(rečnik["reč"]["sinonimi"]) ispiše sve sinonime reči.
    - Komanda print(rečnik["reč"]["antonimi"]) ispiše sve antonime reči.
    - Komanda print(rečnik["reč"]["sinonimi"][0]) ispiše prvi sinonim reči.
    - Komanda print(rečnik["reč"]["antonimi"][1]) ispiše drugi antonim reči.
    - Pokretanje postojećih linija koda ispiše reč, zatim njene sinonime,
      zatim njene antonime.

Nisku "reč" u gornjim primerima zamenite svojim rečima, a termine "sinonimi" i
"antonimi" koristite u postojećoj formi.

O tome šta postojeće linije koda rade razgovaraćemo na sledećem predavanju.
"""

# ovde dodajte svoj kod

rečnik = {"mršav" : { "sinonimi" : ["žigljast", "žgoljav"], "antonimi" : ["debeo", "buckast"]}, "šareno": {"sinonimi" : ["živopisno", "raznobojno"], "antonimi" : ["jednobojno", "bezbojno"] }, "dobar" : {"sinonimi" : ["fin", "okej"], "antonimi" : ["loš", "zao"]} }

print(rečnik["mršav"]["sinonimi"])
print(rečnik["mršav"]["antonimi"])
print(rečnik["mršav"]["sinonimi"][0])
print(rečnik["mršav"]["antonimi"][1])

print(rečnik["šareno"]["sinonimi"])
print(rečnik["šareno"]["antonimi"])
print(rečnik["šareno"]["sinonimi"][0])
print(rečnik["šareno"]["antonimi"][1])

print(rečnik["dobar"]["sinonimi"])
print(rečnik["dobar"]["antonimi"])
print(rečnik["dobar"]["sinonimi"][0])
print(rečnik["dobar"]["antonimi"][1])

# ispod ove linije nemojte dodavati svoj kod niti menjati postojeći

for reč in rečnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in rečnik[reč]["sinonimi"]:
       sin += sinonim + ", "
    print(sin[:-2])
    for antonim in rečnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n") 