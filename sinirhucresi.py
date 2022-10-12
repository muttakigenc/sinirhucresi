class sinirHucresi:
    def __init__(self, A, B):
        self.A=A
        self.B=B
    def isle(self,prmlist):
        toplam=self.B;
        if(len(prmlist)!=len(self.A)):
            raise Exception("Parametre listesi, agirlik listesi ile ayni boyda degil")
        for elem,wg in zip(prmlist,self.A):
            toplam+=elem*wg
        return toplam