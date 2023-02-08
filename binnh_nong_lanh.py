# a la so nguoi o nha
a = int(input())
# b la nhiet do ngoai troi
b = int(input())
if a >= 1 and a < 3:
    if b <= 15:
        print("bat 2 tieng")
    elif b > 15 and b <= 20:
        print("bat 1 tieng 30 phut")
    elif b > 20 and b <= 25:
        print("bat 1 tieng ")
    elif b > 25 and b <= 30:
        print("bat 45 phut")
    elif b > 30 and b <= 50:
        print("bat 30 phut")
elif a >=3 and a <=5:
    if b<= 15:
        print("bat 4 tieng")   
    elif b > 15 and b <= 20:
        print("bat 3 tieng")
    elif b > 20 and b <= 25:
        print("bat 2 tieng")
    elif b > 25 and b <= 30:
        print("bat 1 tieng 30 phut")
    elif b > 30 and b <= 50:
        print("bat 1 tieng")