# input nilai variabel
a=input ("masukan nilai a : ")
b=input ("masukan nilai b : ")

# cetak nilai variabel
print("variabel a = ",a)
print("variabel b = ",b)

#cetak hasil operasi kedua variabel dengan string format
a=a
b=b
print(f"Hasil penggabungan {b}&{a}={b}{a}")
 
#konversi nilai variabel
a=int(a)
b=int(b)
print("Hasil penjumlahan {1}+{0}=%d". format(a,b)%(a+b))
print("Hasil pembagian {1}/{0}=%d". format(a,b)%(a/b))