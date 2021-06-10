def add (a, b) :
    return a + b

def substract (a, b) :
    return a - b

def divide (a, b) :
    return a / b

def multiply (a, b) :
    return a * b

print("Pilih Operasi")
print("1. Penjumlahan")
print("2. Penguragan")
print("3. Pembagian")
print("4. Perkalian")

Pilihan_Operasi_Kalkulator = input("Masukkan Pilian Operasis Kalkulator (1/2/3/4) : ")


bilangan_1 = int(input("Masukkan nilai bilangan pertama : "))
bilangan_2 = int(input("Masukkan nilai bilangan kedua : "))

if Pilihan_Operasi_Kalkulator == '1' :
    print(bilangan_1,"+",bilangan_2,"=", add(bilangan_1,bilangan_2))
elif Pilihan_Operasi_Kalkulator == '2' :
    print(bilangan_1,"-",bilangan_2,"=", substract(bilangan_1,bilangan_2))
elif Pilihan_Operasi_Kalkulator == '3' :
    print(bilangan_1,"/",bilangan_2,"=", divide(bilangan_1,bilangan_2))
elif Pilihan_Operasi_Kalkulator == '4' :
    print(bilangan_1,"*",bilangan_2,"=", multiply(bilangan_1,bilangan_2))
else:
    print("Input Salah")