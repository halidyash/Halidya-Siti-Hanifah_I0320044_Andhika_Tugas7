#Soal no 2
#Pengaplikasian fungsi numerik
p = 14759999
g = 4359999
b = 7725999

str = "Toko Alat Musik PAVALON"
s = str.center(40,'-')
print(s)
print("")
print("Available stock = Piano, Gitar, Biola")
print("Discount all product 20%")
print("")

tanya = input('Alat musik apa yang akan anda beli? (Piano/Gitar/Biola)')
if tanya == 'Piano':
    print('Harga Piano = Rp', p)
    import math
    piano1 = math.ceil(p * ((100 - 20) / 100))
    print('Harga Piano setelah diskon = Rp', math.fabs(piano1))
elif tanya == 'Gitar':
    print('Harga Gitar = Rp', g)
    import math
    gitar1 = math.ceil(g * ((100 - 20) / 100))
    print('Harga Gitar setelah diskon = Rp', math.fabs(gitar1))
else :
    print('Harga Biola = Rp', b)
    import math
    biola1 = math.ceil(b * ((100 - 20) / 100))
    print('Harga Biola setelah diskon = Rp', math.fabs(biola1))

print("")
tanya3 = input('Terdapat promo dari toko kami karena anda adalah pembeli pertama, apakah anda ingin mengambilnya? (Y/T)')
if tanya3 == 'Y':
    import random
    a = ["Tumblr", "Totebag", "Piring cantik"]
    print('Selamat! anda mendapatkan', random.choice(a), 'dari toko kami!')
else:
    exit()