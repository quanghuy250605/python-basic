a= [111,222,333,444,555]
for x in a:
    print(x)
#loop through string
for x2 in "huy":
    print(x2)
#break
for x in a:
    print(x)
    if x== 222:
        break
#continue
for x in a:
    if x ==333:
        continue
    print(x)
#range
for x1 in range(3,7):
    print(x1)
#cấp số cộng
for i in range(2,10,2):
    print(i)
#lồng for
i1=["chó","mèo","gà"]
i2=["xanh","đỏ","tím"]
for z in i1:
    for z1 in i2:
        print(z,z1)