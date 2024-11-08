# menambahkan ada urutan baris
def piramida(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print(f"{' ' * (n-i)} baris ke {i}")

# menambahkan ada urutan baris
def piramida_terbalik(n):
    baris = 2 * n 
    for i in range(5,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for k in range(2*i-1):
            print("*",end="")
        print(f"{' ' * (n-i)} baris ke {baris - i + 1}")

piramida(5)
print()
piramida(5)
piramida_terbalik(5)

# hasilnya tidak ketengah karna tidak ganjil
# def piramid(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print("_",end="")
#         for k in range(i):
#             print("*",end="")
#         print()
# piramid(5)