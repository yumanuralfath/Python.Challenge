n = int(input("Masukkan jumlah angka yang ingin dimasukkan: "))
numbers = []

for i in range(n):
    number = int(input("Masukkan angka ke-{}: ".format(i+1)))
    numbers.append(number)

print("Angka yang dimasukkan:", numbers)
