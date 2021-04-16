#Soal no 1
#Pengaplikasian fungsi string

judul = "Program Pengaplikasian Fungsi String"
judul2 = judul.center(40,'-')
print(judul2)

#input kalimat
print("Masukkan kalimat")
kalimat = str(input(">> "))
print()

#proses
def menu():
    choice = int(input('''Pilih opsi pengaplikasian
    (1) Menghitung jumlah huruf vokal
    (2) Mengubah jadi huruf kapital
    (3) Mengubah jadi huruf kecil
    (4) Menghitung jumlah string
    (5) Keluar dari program
    >> '''))
    if choice ==1:
        print("Menghitung jumlah huruf vokal")
        a = kalimat.count("a")
        i = kalimat.count("i")
        u = kalimat.count("u")
        e = kalimat.count("e")
        o = kalimat.count("o")
        print("Jumlah seluruh huruf vokal dalam kalimat tersebut ialah \n>>", a + i + u + e + o)
        menu()
    elif choice == 2:
        print("Mengubah kalimat menjadi huruf kapital")
        kapital = kalimat.upper()
        print("Hasil kalimat tersebut setelah diubah adalah \n>>", kapital)
        print()
    elif choice == 3:
        print("Mengubah kalimat menjadi huruf kecil")
        kecil = kalimat.lower()
        print("Hasil kalimat tersebut setelah diubah adalah \n>>", kecil)
        print()
    elif choice == 4:
        print("Menghitung jumlah string")
        string = kalimat.count(kalimat)
        print("Jumlah sting dalam kalimat tersebut adalah \n>>", string)
        print()
    else:
        exit()

# Main Loop Program
if __name__ == "__main__":
    while True :
        menu()



