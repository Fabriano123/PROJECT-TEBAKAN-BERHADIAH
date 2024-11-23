import random
import os
class tebaktebakan:
    def __init__(self):
        angkadiskon = random.randrange(100)
        kesempatan = 0
        os.system("cls")
        while True:
            print(f" {'\t-TEBAKAN BERHADIAH-\t':$^43}")
            print("Berkesempatan mendapatkan diskon sampai di atas 50% loh !!!")
            print("Kesempatan tebakan anda hanya 5x")
            print(f"Jumlah tebakan anda sekarang : {kesempatan}")
            tebakan = int(input("Masukkan Tebakan Anda : "))
            if tebakan != angkadiskon and kesempatan == 5:
                print("MAAF... TEBAKAN ANDA SALAH! SILAHKAN COBA DI LAIN WAKTU :)")
                break
            elif tebakan < angkadiskon:
                print("Angka yang kamu jawab lebih kecil dari angka tebakan")
                kesempatan += 1
            elif tebakan > angkadiskon:
                print("Angka yang kamu jawab lebih besar dari angka tebakan")
                kesempatan += 1 
            elif angkadiskon == tebakan:
                print(f"SELAMAT ANDA MENDAPATKAN DISKON SEBESAR {tebakan}% !")
                print(f"Anda dapat menggunakan voucher ini untuk berbelanja di alfamart atau indomaret terdekat.")
                break
            print(f"※"*60)
def main():
    run = tebaktebakan()

if __name__ == "__main__":
    main()
