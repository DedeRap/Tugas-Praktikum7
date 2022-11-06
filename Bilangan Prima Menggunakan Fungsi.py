print("===== Bilangan Prima Menggunakan Fungsi =====")


def Prima(n):
    if (n % 2 == 0):
        ok = "bukan bilangan prima."
    elif (n % 3 == 0):
        ok = "bukan bilangan prima."
    elif (n % 5 == 0):
        ok = "bukan bilangan prima."
    elif (n % 7 == 0):
        ok = "bukan bilangan prima."
    else :
        ok = "adalah bilangan prima."
    
    return ok

y = int(input("Masukkan bilangan = "))

print("Bilangan", y , Prima(y))