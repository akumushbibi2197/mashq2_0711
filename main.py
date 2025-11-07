#6-misol
def teskari(royxat):
    return royxat[::-1]

r = input("Elementlarni bo‘sh joy bilan kiriting: ").split()
print("Teskari ro‘yxat:", teskari(r))

#7-misol
def kalkulyator(a, b, amal):
    if amal == '+':
        return a + b
    elif amal == '-':
        return a - b
    elif amal == '*':
        return a * b
    elif amal == '/':
        return a / b if b != 0 else "Bo‘lish mumkin emas!"
    else:
        return "Noto‘g‘ri amal!"

a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")
print("Natija:", kalkulyator(a, b, amal))

#8-misol
def sozlar_soni(satr):
    return len(satr.split())

satr = input("Gap kiriting: ")
print("So‘zlar soni:", sozlar_soni(satr))

#9-misol
def juft_ikki_barobar(royxat):
    return [x * 2 for x in royxat if x % 2 == 0]

r = [int(x) for x in input("Sonlarni kiriting: ").split()]
print("Natija:", juft_ikki_barobar(r))

#10-misol
def kalitlar_royxati(lugat):
    return list(lugat.keys())

lugat = {}
n = int(input("Nechta element kiritasiz? "))
for i in range(n):
    k = input(f"{i+1}-kalit: ")
    v = input(f"{i+1}-qiymat: ")
    lugat[k] = v

print("Kalitlar ro‘yxati:", kalitlar_royxati(lugat))
