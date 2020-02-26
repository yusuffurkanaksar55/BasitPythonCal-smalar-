sözlük={"computer":"Bilgisayar","Driver":"Sürücü","Software":"Yazılım"}
print(sözlük.keys())
print(sözlük.values())
print(sözlük.items())

kelime=input("Bir kelime giriniz")
sözlük={"computer":"Bilgisayar","Driver":"Sürücü","Software":"Yazılım"}

if kelime in sözlük:
    print(sözlük[kelime])
else:
    print("Girdiğiniz kelime sözlükte bulunmamaktadır")
