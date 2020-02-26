with open("dosya.txt","r+") as dosya:
    data=dosya.readlines()
    data.insert(1,"Yusuf FUrkan KAsasd")
    dosya.seek(0)
    dosya.writelines(data)
