class Car:
    marka = "mercedes"
    def __init__(self,vites,renk,motor):
        self.vites = vites
        self.renk = renk
        self.motor = motor
    
    def get(self):
        print(self.vites,self.renk,self.motor)

    @classmethod
    def clsm(cls):
        print(cls.get)

o1 = Car("vites", "renk", "motor")