class cokgen():
    def __init__(self,ad,kenar_sayisi):
        self.adi = ad
        self.kenar=kenar_sayisi
    def hesap(self):
        self.ic_acı_toplamı=self.kenar_sayisi*180-360
        
sekil = cokgen("üçgen", 3)
sekil.hesap()
print(sekil.ic_acı_toplamı)