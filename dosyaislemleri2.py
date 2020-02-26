dosya=open("dosya.txt","r")


#read() içinde ne varsa almasını sağlayacak
print(dosya.read())
#readline() tek bir satır okumak için
#print(dosya.readline())

#readlines() tüm satırları liste şeklinde gösterir
#print(dosya.readlines())

dosya.close() #dosya kapatımı
