class HCN:
    dai = 0
    rong = 0
    ten = ""
    def __init__(self,ten,dai,rong):
        self.ten = ten
        self.dai = dai
        self.rong = rong

    def getTen(self):
        return self.ten

    def getDai(self):
        return self.dai

    def getRong(self):
        return self.rong

    def toString(self):
        return  "HCN" + self.ten + "(" +str(self.dai) + "," +str(self.rong) + ")"
    def getChuVi(self):
        return (self.dai + self.rong)*2
    def getDientich(self):
        return self.dai + self.rong

