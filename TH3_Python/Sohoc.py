#Phep toan so hoc
a= input("Nhap vao a =  ")
b= input("Nhap vao b = ")

def tong(a,b):
	return a + b
def hieu(a,b):
	return a - b
def tich(a,b):
	return a*b
def thuong (a,b):
	return a/b
def luythua(a,b):
	return a**b	
print "a+b =  %d" %tong(a,b)
print "a-b = %d" %hieu(a,b)
print "a*b = %d" %tich(a,b)
print "a/b = %f" %thuong(a,b)
print "a^b = %d" %luythua(a,b)
