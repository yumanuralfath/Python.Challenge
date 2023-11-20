from logo import logo, ERROR, REWARD
import random

print(" SELAMAT DATANG DI TEBAK ANGKA")
print(" Created By Yumana ")


#Angka Acak 1-100
def Tebakan():
    print(" SELAMAT DATANG DI TEBAK ANGKA")
    #Tampilkan Gambar
    print(logo)
    
    #ACAK ANGKA 1-100
    AngkaAcak = random.randrange(1,100)
    print("Aku memikirkan sebuah angka 1-100. ")
    
    #Pilih level Kesulitan
    Hati = 0
    print("Pilih Tingkat Kesulitan ")
    Level = int(input("Silahkan pilih  1.Mudah 2.Sulit 3.Beban Hidup: "))
    if Level == 1:
        print("Kesempatan Menebak 15x , dasar noob! ")
        Hati = 15
    if Level == 2:
        print("Kesempatan Menebak 10x , Bolehlah! ")    
        Hati = 10
    if Level == 3:
        print("Ampun Sepuh , percobaan hanya 5x")
        Hati = 5
    if Level not in [1,2,3]:
        print(ERROR)
        print("Ketik Yang Benar Bujang")
    
    #MULAI TEBAKAN
    while Hati > 0:
        Tebak = int(input("Silahkan masukan tebakan : "))
        if Tebak not in range(1, 100):
            print(ERROR)
        
        if Tebak  == AngkaAcak:
            print("Selamat, selamat silahkan dinikmati hadiahmu")
            print(REWARD[random.randrange(0,4)])
            break
        
        if Tebak > AngkaAcak:
            print("Hadeh Tinggi amat ekspektasimu")
            Hati -= 1
            print(f"Nyawa ente tinggal {Hati}, Coba lagi")
            
        if Tebak < AngkaAcak:
            print("Ayolah rendah amat nilai nya")
            Hati -= 1
            print(f"Nyawa ente tinggal {Hati}, Coba lagi")
        
        if Hati == 0 :
            print(f"kamu kalah karena nyawamu {Hati}")
            break
        
Tebakan()

main = input("Ingin main ulang (y/n)")
if main == "y":
    Tebakan()

else:
    print(ERROR)
    print("Bye")