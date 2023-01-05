
class Kedi:
    def __init__(self,isim="İsimsiz",yas=0,renk="Gri",cins="sokak kedisi",*rahatsizliklar):
        self.isim = isim
        self.yas = yas
        self.cins = cins
        self.rahatsizliklar = rahatsizliklar
    def Ask_rahatsizlik(self):
        self.liste = ""
        for i in self.rahatsizliklar:
            self.liste = self.liste + i + "\n"
        form = f"""{self.isim}
-----------------
{self.liste}"""
        return form

Kedi1 = Kedi("Pisi",2,"Sarman","Exotic Shorthair","Ciltte yara","Bölgesel tüy Dökülmesi","Kaşıntı")

print(Kedi1.Ask_rahatsizlik())


class Arac:
    ilanDurumu = "Aktif"
    def __init__(self,marka,model,ozellikler):
        self.marka = marka
        self.model = model
        self.ozellik = ozellikler
    def arac_bilgi(self):
        form = f"""Araç Model/Model = {self.marka}/{self.model}
Araç Özellikleri:
{self.ozellik}"""
        return form
    @classmethod
    def ilandurumu(cls):
        cls.ilanDurumu = ilanDurumu
        return cls.ilanDurumu
    