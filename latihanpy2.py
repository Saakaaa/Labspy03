print("----Latihan 2----")
print("Menampilkan bilangan berhenti ketika bilangan 0dan menampilkan bilangan terbesar")

max=0
while True:
    a=int(input("Masukkan Bilangan: "))
    if max < a :
        max = a
    if a==0:
        break
print("Bilangan Terbesar Adalah = ",max)
