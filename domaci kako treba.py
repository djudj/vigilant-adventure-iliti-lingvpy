# -*- coding: utf-8 -*-
"""
DOMAĆI ZADATAK 1:

Izmenite priču tako što ćete poslednju rečenicu obrisati i umesto nje dodati
vaših nekoliko rečenica kojima ćete promeniti ishod priče.

Nakon toga podelite priču na rečenice funkcijom .split() (Hint: Razmislite koji
kriterijum za razdvajanje vam je sada potreban umesto dosadašnjeg " "). i
funkcijom len() proverite koliko rečenica sada ima priči.

"""

prica = "Živele u jednoj bari tri žabe. Svađale su se oko toga koja od njih najbolje peva, čiji je glas najlepši. Njihovoj svađi nikad ne bi došao kraj da nisu odlučile da organizuju takmičenje da se vidi ko je najbolji. To je za stanovnike bare i okoline bio veliki događaj. Sve žabe, i velike i male, su došle da svojim prisustvom pomognu odluku žirija. Ali pred sam početak svi shvatiše da nisu izabrali žiri. Mnogo njih je želelo da odlučuju koja od tri žabe najlepše peva i zato je bila takva galama da niko nikog nije čuo šta govori. Roda, patka i zmija čuju kreketanje (a taj zvuk ih je neodoljivo privlačio) i požure da vide šta se događa. Žabe, ne razmišljajući mnogo, zamole rodu, patku i zmiju da budu članovi žirija. One pristanu i takmičenje poče. Tri žabe su naizmenično pevale sve dok nisu iscrple svoj bogati repertoar i dok nisu promukle. Publika je bila oduševljena. Članovi žirija zamoliše za tišinu i rekoše takmičarkama da priđu bliže da im čestitaju i proglase pobednicu. I žabe priđoše umorne i sretne. Možemo zamisliti šta se dogodilo takmičarkama. A i publici iz prvih redova. Te večeri su roda, patka i zmija imale obilnu večeru. Žabama nije bilo do pesme. Celu noć su razmišljale i šaputale. Nikad više nisu se svađale koja najlepše peva." 
recenice = prica.split(". ")

print(recenice)

recenice_prvi_deo = recenice [:-1]
print(recenice_prvi_deo)


r = "Trebalo  je pokrenuti ustanak i osvetiti žabe pevaljke. Narod se podelio jer su jedni smatrali da žabe koje samo žele da privuku pažnju ne treba spašavati, dok su drugi smatrali da se treba boriti za svoju vrstu. Ništa se na kraju nije desilo jer su u ovoj priči žabe zaboravne životinje."
recenice_prvi_deo.append(r)
print(recenice_prvi_deo)

recenica_bez_tacke = recenice_prvi_deo[-1][0:-1]
print(recenice_prvi_deo)

recenice_prvi_deo[-1] = recenica_bez_tacke


ponovo_niska = ". ".join(recenice_prvi_deo)
print(ponovo_niska)