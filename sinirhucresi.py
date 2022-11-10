import random

class sinirHucresi:
    def __init__(self):
        self.__wgs=[]
    def ağırlıkyap(self,testprmlist):
        for test in testprmlist:
            self.__wgs.append(random.random())
        self.__wgs.append(random.random())
        return self
    def isle(self,prmlist):
        toplam=self.__wgs[-1];
        for elem,wg in zip(prmlist,self.__wgs):
            toplam+=elem*wg
        return toplam