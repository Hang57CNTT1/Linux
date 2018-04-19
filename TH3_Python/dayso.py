#a. Nhap day so 1->n
n = input ("Nhap vao n = ")
def printList(n):
	for i in range(1,n+1):
		print i
printList(n)
#b. Tinh tong cac phan tu chan cua day
def Tongchan(n):
	sum = 0
	for i in range(1,n +1):
		if (i%2 == 0):
			sum=sum+i
	print "Tong so chan la: ",sum
Tongchan(n)
