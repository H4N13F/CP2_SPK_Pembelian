def menu():
    print ("===========SPK Pembelian===========")
    print ("1.Sepatu")
    print ("==================================")
def sepatu():
    print ("==================================")
    print ("          Pilih Sepatu        ")
    a = input("Jenis Sepatu : ")
    b = input("Ukuran       : ")
    c = input("Material     : ")
    print ("==================================")
    print ("==================================")
    print (" Jenis Sepatu   : ",a)
    print (" Ukuran         : ",b)
    print (" Material       : ",c)
    print ("==================================")
    print (jumlah())
def jumlah():
    print ("===========Jumlah Harga============")
    a = int(input(" Fantofel : "))
    b = int(input(" Sneakers : "))
    c = (a+b)
    print (" Total Harga : ",c)
    print ("==================================")
    print(" Mau coba lagi [Y/N]? ")
    back = input().upper()
    if back == ("Y"):
        menu()
    else:
        exit()
print("Selamat Datang")
print("<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>")
menu()

while 1:

    pilih = input(" Pilih : ")
    if pilih == "1":
        sepatu()
        print("\n:")
    else:
        print ("Maaf pilihan yang anda masukkan tidak terdaftar")
        print ("Coba lagi [Y/N] ? ")
        coba = input().upper()
        if coba == ("Y"):
            menu()
        else:
            exit()