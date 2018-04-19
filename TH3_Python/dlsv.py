#dlsv.py
class sinhvien:
	MSSV = " ",
	Hoten = "",
	MaKhoa = " "
	def __init__(self,MSSV,Hoten,Makhoa):
		self.MSSV = MSSV
		self.Hoten = Hoten
		self.Makhoa = Makhoa
	def setTen(self,MSSV):
		self.MSSV = MSSV
	def getTen(self):
		return self.MSSV
	def setTen(self,Hoten):
		self.Hoten = Hoten
	def getTen(self):
		return self.Hoten
	def setTen(self,Makhoa):
		self.Makhoa = Makhoa
	def getTen(self):
		return self.Makhoa
	def toString(self):
		print( self.MSSV +"\t"+self.Hoten +"\t" + self.Makhoa)
	
class khoa:
	Makhoa = "",
	Tenkhoa = "",
	def __init__(self,Makhoa,Tenkhoa):
		self.Makhoa = Makhoa
		self.Tenkhoa = Tenkhoa
	def setMakhoa(self,Makhoa):
		self.Makhoa = Makhoa
	def getMakhoa(self):
		return self.Makhoa
	def setTenkhoa(self,Tenkhoa):
		self.Tenkhoa = Tenkhoa
	def getTenkhoa(self):
		return self.Tenkhoa
	def toString(self):
		print(self.Makhoa+"\t\t"+self.Tenkhoa)
a= []
a.append(sinhvien('001','Mai A','01'))
a.append(sinhvien('002','Tran B','01'))
a.append(sinhvien('003','Van C','02'))
a.append(sinhvien('004','Thi K','01'))
print ("MSSV"+"\t"+"Ho Ten"+"\t"+"Ma khoa"+"\n")
for i in a:
	i.toString()

b = []
b.append(khoa('01','CNTT'))
b.append(khoa('02','KeToan'))
b.append(khoa('03','CoKhi'))
b.append(khoa('04','Nuoi'))
print ("Ma khoa"+"\t\t"+"Ten khoa"+"\n")
for i in b:
	i.toString()

#b. In ds sv khoa CNTT
print ("Danh sach sinh vien khoa CNTT la:")
for i in b:
	if(i.Tenkhoa == "CNTT"):
		s=i.Makhoa
for i in a:
	if(i.Makhoa == s):
		i.toString()
