class TruogSonThuy():
    def nhatduongchi(self):
        print("Nhat Duong Chi")
class TaTon():
    def camnathu(self):
        print("Cam Na Thu")
        
class TruongVoKy(TruogSonThuy,TaTon):
    def chitiet(self):
        self.nhatduongchi()
        self.camnathu()
        
obj = TruongVoKy()
obj.chitiet()