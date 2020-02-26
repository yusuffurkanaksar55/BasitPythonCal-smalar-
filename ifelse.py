a=20
b=5
if a>b:
    print("A büyüktür B'den")
else:
    print("B büyüktür A'dan")

şifre="yusuf"
sifrem=input("Şifreyi giriniz :")

if şifre==sifrem:
    print("Sisteme başarılı şekilde giriş yapıldı")
else:
    print("Bir daha deneyin")

vize=float(input("Vize notunuzu girin :"))
final=float(input("Final notunuzu girin :"))
ortalama=vize*0.4+final*0.6

if ortalama<30:
    print("Derslerden kaldınız.")
elif ortalama>30 and ortalama<50:
    print("Ders notunuz->DC")
elif ortalama>50 and ortalama<70:
    print("Ders notunuz-> CC")
elif ortalama>70 and ortalama<100:
    print("Ders notunuz-> AA")
