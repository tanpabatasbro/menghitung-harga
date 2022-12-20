print('''menghitung harga diskon suatu produk
''')

while True:
    nama = input("Masukkan Nama Produk : ")
    harga = int(input("Masukkan Harga Produk : "))
    diskon = int(input("Masukkan Diskon (tanpa%): "))

    total = (diskon /100 * harga)

    print(f"nama produk : {nama}\nharga produk : {total}")
    
    bayar = input("Mau Bayar Bro (y/n)0?")
    if bayar == "y":
        uang = int(input("Masukkan jumlah uang : "))
        jummlah = uang - total

    else:        
        break
