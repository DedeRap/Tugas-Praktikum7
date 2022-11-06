print("===== Ordinal Number =====")

print("Ketik angka 0 untuk menghentikan")

def Ordinal(n):
    if (n == 1):
        s = 'st'
    elif (n == 2):
        s = 'nd'
    elif (n == 3):
        s = 'rd'
    else :
        s = 'th'
    
    return s

u = 1

while (u != 0):
    a = int(input("Masukkan angka = "))
    print(a, Ordinal(a))
    
    if (a == 0):
        u = 0
    