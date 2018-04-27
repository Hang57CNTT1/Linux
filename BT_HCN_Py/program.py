from Chunhat import HCN
n = input("Nhap so luong hinh chu nhat: ")
a = []
for i in range(0,n):
    ten=str(input("Nhap ten:"))
    dai=input("Chieu dai = ")
    rong=input("Chieu rong = ")
    HCN=HCN(ten,dai,rong)
    a.append(HCN)
for item in a:
    print ("Hinh chu nhat: ")
    cv = item.getChuVi()
    dt = item.getDienTich()
    print(item.toString())
    print ("Chu vi = " + str(cv) + "\n" + "Dien tich = "+str(dt))
#Cho biet ten HCN Co dien tich lon nhat
dt_max = a[0].getDienTich()
ten_max = a[0].getTen()
for item in a:
    if(dt_max < item.getDienTich()):
        dt_max = item.getDienTich()
        ten_max = item.getTen()
    print ("Hinh chu nhat co dien tich lon nhat la: " + ten_max + "co dien tich: " +str(dt_max))
#Luu file
o = open("DSHCN.txt","w+")
for item in a:
    o.write(item.getTen() + "\n" + item.getDienTich + "\n" + item.getChuVi)