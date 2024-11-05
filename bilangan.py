import random

n = int(input("Masukkan jumlah bilangan: "))
kenaikan = int(input("Masukkan kenaikan untuk bilangan urut naik: "))
batas_atas = int(input("Masukkan batas atas untuk bilangan acak: "))

def hitung_bilangan_urut(n):
    urut = [i for i in range(1, n+1)]
    return urut

def hitung_bilangan_urut_naik(n, kenaikan):
    urut_naik = [i for i in range(1, (n * kenaikan) + 1, kenaikan)]
    return urut_naik

def hitung_bilangan_acak(n, batas_atas):
    acak = [random.randint(1, batas_atas) for _ in range(n)]
    return acak

print("Bilangan urut:", hitung_bilangan_urut(n))
print("Bilangan urut naik:", hitung_bilangan_urut_naik(n, kenaikan))
print("Bilangan acak:", hitung_bilangan_acak(n, batas_atas))