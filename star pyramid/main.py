# def piramida_bintang(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print("_",end="")
#         for k in range(i):
#             print("*",end="")
#         print()

# def piramida_bintang_terbalik(n):
#     for i in range(n, 0, -1):  # Memulai dari n hingga 1
#         for j in range(n - i):
#             print(" ", end="")
#         for k in range(2 * i - 1):
#             print("*", end="")
#         print()

# piramida_bintang(5)
# piramida_bintang_terbalik(5)

# hasilnya tidak ketengah karna tidak ganjil
# def piramid(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print("_",end="")
#         for k in range(i):
#             print("*",end="")
#         print()
# piramid(5)