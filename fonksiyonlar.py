def fibonacci(sayı):
    if sayı==0:
        return 0
    if sayı==1:
        return 1
    return fibonacci(sayı-1)+fibonacci(sayı-2)
x=int(input("Bir sayı giriniz"))
print(fibonacci(x))

#VERİLEN SAYIDAN 0 DAN BERİ GERİ SAYMA 
def gerisay(sayı):
    while sayı>0:
        sayı=sayı-1
        print("Sayınız {}, geri kalanlar {}".format(sayı,sayı-1))
x=int(input("Geri saymasını istediginiz sayıyı giriniz"))
print(gerisay(x))

#KENAR UZUNLUĞU VERİLEN KARENİN ALANI BULMA

def alan(kenar):
    return kenar*kenar
x=int(input("Karenin kenarını giriniz"))
print(alan(x))

#ALINAN SAYIDAN 0'A KADAR OLAN TÜM SAYILARI TOPLA
#def toplama(sayı):
#    return sayı+toplama(sayı-1)
#x=int(input("Sayıyı giriniz"))
#print(toplama(x))

#Çift bir sayıyı parametre olarak alan ve aldığı sayıdan 0'a kadar olan çift sayıların toplamını yazdıran bir recursive fonksiyonu yazalım. 

def ciftsayı(sayı):
    if sayı==0:
        return 0
    else:
        return sayı+ciftsayı(sayı-2)

x=int(input("Sayıyı giriniz->"))
if x%2==0:
    print(ciftsayı(x))
else:
    print("Lütfen çift sayı giriniz")

#ALINAN NEGATİF BİR SAYIDAN 0'A KADAR OLAN SAYILARI TOPLAYALIM 
def negatif_toplama(sayı):
    if sayı==-1:
        return -1
    else:
        return sayı+negatif_toplama(sayı+1)
x=int(input("Negatif sayı giriniz"))
if x>0:
    print("Lütfen negatif sayı giriniz")
else:
    print(negatif_toplama(x))

