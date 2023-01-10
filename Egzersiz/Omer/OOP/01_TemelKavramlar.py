class cokgen:
    def __init__(self,cokgen,kenar):
        self.cokgen = cokgen
        self.kenar = kenar

    def acılartoplam(cokgen,kenar):
        print(f"çokgenin adı : {cokgen.cokgen} açıların toplamı : {(kenar-2)*180}")

üçgen = cokgen("üçgen", 3)
üçgen.acılartoplam(3)




    




