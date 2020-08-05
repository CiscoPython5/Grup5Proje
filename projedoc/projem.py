#Site Panel Bulucu
import requests
import os

os.system("clear")

turkuaz = "\033[96m"
print(turkuaz +"""

     --------------------------------------
     -                                    -
     -  Web Sitesi          Panel Bulucu  -
     --------------------------------------

""")
try:
    admin = open("list.txt", "r").readlines()
except:
    print("panel listesini bulunamadı! \nlist dosyasını ekleyin")
    exit()
site = input(turkuaz + "site adresini girin: ")
print(turkuaz + "\n==================================")
print(turkuaz + "bulunanlar;")
for i in admin:
      req = requests.get(site+i.replace("\n",""))
      if req.status_code==200:
              print(">> " + req.url)    
print(turkuaz + "\n==================================")
print(turkuaz + "-->Tarama tamamlandı.")
        
        



