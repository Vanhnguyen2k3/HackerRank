x = int(input("Nhap so nguyen x: "))
y = int(input("Nhap so nguyen y: "))
z = int(input("Nhap so nguyen z: "))
n = int(input("Nhap so nguyen n: "))
list = []

for x in range(0, x + 1):
    for y in range(0, y + 1):
        for z in range(0, z + 1):
            if (x + y + z) != n:
                list.append([x, y, z])

print(list)