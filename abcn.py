a = []
length = int(input("how many numbers : "))
for i in range(length):
    val = int(input("enter the numbers : "))
    a.append(val)
sum = 0
for i in range(length):
    sum = sum + a[i]   
print("sum of list of the elements : ",sum)     