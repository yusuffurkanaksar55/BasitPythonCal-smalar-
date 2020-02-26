for sayı in range(0,20,2):
    print(sayı)

for sayı in range(0,20):
    if sayı%2==0:#ÇİFT SAYILARI YAZDIRMAK İÇİN
        print(sayı)
toplam=0
sayı1=int(input("İlk sayıyı giriniz"))
sayı2=int(input("İkinci sayıyı giriniz"))
for i in range(sayı1,sayı2):
    toplam=toplam+i
print("{} ve {} toplamı-> {}".format(sayı1,sayı2,toplam))

sonuc=1
s1=int(input("İlk sayıyı giriniz"))

for i in range(1,s1+1):
    sonuc=sonuc*i
print("{} sayısını faktöriyeli {}".format(s1,sonuc))

meyveler=['elma','muz','çilek']
for meyve in meyveler:
    print("meyveler: ",meyve)




