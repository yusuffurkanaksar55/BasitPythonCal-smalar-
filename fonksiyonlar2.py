class calısan:
    def __init__(self,ad,soyad,maaş):
        self.isim=ad
        self.soyad=soyad
        self.maaş=maaş
        self.eposta=self.isim+self.soyad+"@gmail.com"
    def tambilgi(self):
        return "Çalışanın adı-> {} soyadı-> {} ve Eposta hesabı-> {}".format(self.isim,self.soyad,self.eposta)
personel1=calısan("yusuffurkan","aksar",2500)
personel2=calısan("gülsüm","keskin",4500)

print(personel1.tambilgi())


class öğrenci:
    def __init__(self,ad,notu,sınıf):
        self.ad=ad
        self.notu=notu
        self.sınıf=sınıf
    def tambilgi2(self):
        return "Öğrencinin adı->{}\n Sınavdan aldığı not->{}\n Öğrenci Kaçıncı Sınıf->{}".format(öğrenci1.ad,öğrenci1.notu,öğrenci1.sınıf)


öğrenci1=öğrenci("Yusuf Furkan",50,3)
print(öğrenci1.tambilgi2())


class calısan:
    zam_oran=1.05
    per_say=0
    
    def __init__(self,ad,soyad,maaş):
        self.isim=ad
        self.soyad=soyad
        self.maaş=maaş
        self.eposta=self.isim+self.soyad+"@gmail.com"
        calısan.per_say=calısan.per_say+1
    def tambilgi(self):
        return "Çalışanın adı-> {} soyadı-> {} ve Eposta hesabı-> {}".format(self.isim,self.soyad,self.eposta)
    def arttır(self):
        self.maaş=(self.maaş*calısan.zam_oran)
        
personel1=calısan("yusuffurkan","aksar",2500)
print(calısan.per_say)
personel2=calısan("gülsüm","keskin",4500)
print(calısan.per_say)

print(personel1.tambilgi())

print(personel1.maaş)
personel1.arttır()
print(personel1.maaş)

print(personel2.maaş)
personel2.zam_oran= 2.5
personel2.arttır()
print(personel2.maaş)


































