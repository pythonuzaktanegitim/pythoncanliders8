liste = ["AliEmre","AliKurt","Ayse","Baha","Burak","Edanur","Emin","Hakan","Hedayah","Kaan",
"Melike","Metehan","Andac","Esra","Omer","Sonay","Tarik","Turan","Cagan","OmerA","Irfancan","Ediz","Samet"]
import os
dosya_ismi = "01_TemelKavramlar.py"
# os.mkdir("Egzersiz")
for item in liste:
    try:
        os.makedirs(f"Egzersiz/{item}/OOP")
        open(f"Egzersiz/{item}/OOP/{dosya_ismi}","a+")
    except:
        pass