with open("dosya.txt","r") as dosya:#dosyayı kapatmayı unutursak eğer python kendisi kapatır
    dosya.seek(10)#10.bayttan sonra okumaya başladı
    print(dosya.read())
    dosya.seek(5)#5.bayttan sonra okumaya başladı
    print(dosya.read(4))#5.bayttan sonraki 4 karakter okucak
