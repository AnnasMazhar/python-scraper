# temp = int(input("Enter tenmperature: "))
#
# if temp > 10:
#     print("It's cold. the temp is ", temp)
# if temp > 20:
#     print("its warm {}".format(temp))
# if temp > 30:
#     print("Its hot. The temp is %i" % temp)

#
# l = [x*2 for x in range(20) if x%2==0]
# print(l)

#
# temp = 10
# while temp < 15:
#     temp += 1
#     print(temp)
a, b = 0, 1
while True:
    a += b
    b += a
    print("{0}, {1}".format(a, b))
