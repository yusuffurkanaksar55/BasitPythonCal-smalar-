liste=[2,"Python",5.4,[2,3],("Java",0,'a')]
print(liste[0])
print(liste[1])
print([liste[3]])#[2,3]
print(liste[3][0])#2

#APPEND (EKLEME)
meyveler=['elma','muz','çilek']
meyveler.append("karpuz")
print(meyveler)
#INSERT (İSTEDİĞİN İNDEKSE EKLEME)
meyveler=['elma','muz','çilek']
meyveler.insert(2,"ayva")
print(meyveler)
#EXTEND (GENİŞLETME OLARAK KULLANILIR)
meyveler=['elma','muz','çilek']
meyveler2=['ayva','portakal']
meyveler.extend(meyveler2)
print(meyveler)
#REMOVE (SİLMEK METHODU)
meyveler=['elma','muz','çilek']
meyveler.remove("muz")
print(meyveler)
#POP (LİSTEDEN ELEMAN ÇEKMEK)
meyveler=['elma','muz','çilek']
meyveler.pop#ÇEKİLEN ELEMAN ÇİLEK. ÇÜNKÜ EN SONDA
#SORT(ALFABEYE GÖRE SIRALAMAYA YARAYAN BİR METHOD)
meyveler=['elma','çilek','muz']
meyveler.sort()
print(meyveler)
#REVERSE (TERS ÇEVİRME METHODU)
meyveler=['elma','muz','çilek']
meyveler.reverse()
print(meyveler)
#COPY (BAŞKA LİSTEYE KOPYALAMA İŞLEMİ)
meyveler=['elma','muz','çilek']
meyveler2=[]
meyveler2=meyveler.copy()
#meyveler2=meyveler
print(meyveler2)
#CLEAR (LİSTEYİ TEMİZLEMEK)
meyveler=['elma','muz','çilek']
meyveler.clear()
print(meyveler)
