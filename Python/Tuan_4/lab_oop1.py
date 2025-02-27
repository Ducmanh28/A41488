class Person():
    name = ""
    address = ""
    age = 0
        
    def InputDetails(self):
        self.name = input("Nhap vao ten: ")
        self.address = input("Nhap vao dia chi: ")
        self.age = input("Nhap vao tuoi: ")
    
    def displayDetails(self):
        print("Ten: "+self.name)
        print("Dia chi: "+self.address)
        print("Tuoi: " + str(self.age))
        
nv1 = Person()
nv2 = Person()

nv1.InputDetails()
nv2.InputDetails()

nv1.displayDetails()
nv2.displayDetails()