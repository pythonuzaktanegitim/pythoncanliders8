class Cokgen():
    def __init__(self,adi,kenar_sayisi):
        self.adi = adi
        self.kenar_sayisi = kenar_sayisi

    def result(self):
        print(self.adi + " : " + str((self.kenar_sayisi -2)* 180) )        

a = Cokgen("Üçgen", 3)
a.result()